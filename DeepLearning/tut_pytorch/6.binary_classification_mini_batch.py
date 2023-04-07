import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


class LoadBreastCancerDataSet(Dataset):
    def __init__(self, train=True, transform=None, target_transform=None) -> None:
        self.train = train
        self.transform = transform
        self.X, self.y = self.get_data()
        self.input_feature = self.X.shape[1]
        self.target_transform = target_transform

    def get_data(self):
        data = load_breast_cancer()
        X, y = data.data, data.target
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=42)
        if self.train:
            self.transform.fit(X_train)
            return torch.from_numpy(X_train.astype(np.float32)), torch.from_numpy(
                y_train.astype(np.float32)).view(y_train.shape[0], 1)
        else:
            return torch.from_numpy(X_test.astype(np.float32)), torch.from_numpy(
                y_test.astype(np.float32)).view(y_test.shape[0], 1)

    def __len__(self):
        return len(self.X)

    def __getitem__(self, index):

        features = self.X[index]
        label = self.y[index]

        if self.transform:
            features = torch.from_numpy(self.transform.transform(
                features.reshape(1, -1)).reshape(-1).astype(np.float32))
        if self.target_transform:
            label = self.target_transform(label)
        return features, label


scaler = StandardScaler()
train_dataset = LoadBreastCancerDataSet(transform=scaler)
test_dataset = LoadBreastCancerDataSet(transform=scaler, train=False)


train_data_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
test_data_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)


input_feature = train_dataset.input_feature
print(input_feature)
out_feature = 1


# HyperParameters
epochs = 100
hidden_feature = 50
learning_rate = 0.01


class BinaryClassification(nn.Module):
    def __init__(self, input_feature, hidden_feature, out_feature):
        super().__init__()
        self.lr1 = nn.Linear(input_feature, hidden_feature)
        self.relu = nn.ReLU()
        self.hidden = nn.Linear(hidden_feature, out_feature)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.lr1(x)
        x = self.relu(x)
        x = self.hidden(x)
        return self.sigmoid(x)


model = BinaryClassification(input_feature, hidden_feature, out_feature)
criterion = nn.BCELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)


for epoch in range(epochs):
    loss_epoch = 0
    for i, (raw_data, label) in enumerate(train_data_loader):
        y_predict = model(raw_data)
        loss = criterion(y_predict, label)

        with torch.no_grad():
            loss_epoch += loss.item() * raw_data.size(0)
        loss.backward()

        optimizer.step()
        optimizer.zero_grad()

        # if (i % 5 == 0):
        #     print(f"epoch: {epoch} in batch {i+1}")

    if (epoch % 1 == 0):
        print(
            f"in epoch {epoch} loss: {loss_epoch / len(train_data_loader.dataset)}")

model.eval()
test_loss = 0.0
correct = 0
with torch.no_grad():
    for data, target in test_data_loader:
        output = model(data)
        loss = criterion(output, target)
        test_loss += loss.item() * data.size(0)
        pred = output.round()
        correct += torch.sum(pred == target)
test_loss /= len(test_data_loader.dataset)
accuracy = (correct/len(test_data_loader.dataset)) * 100
print(f'Test Loss: {test_loss:.6f}, Test Accuracy: {accuracy:.2f}%')
