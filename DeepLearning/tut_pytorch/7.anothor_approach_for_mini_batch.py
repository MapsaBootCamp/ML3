import numpy as np
import torch
from sklearn.datasets import load_breast_cancer
import torch.nn.functional as F
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# load data
data = load_breast_cancer()

# prepare data
X = data.data
y = data.target

# split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# standardize the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# convert data to tensors
X_train = torch.Tensor(X_train)
X_test = torch.Tensor(X_test)
y_train = torch.LongTensor(y_train)
y_test = torch.LongTensor(y_test)

# set batch size
batch_size = 32

# create data loaders
train_loader = torch.utils.data.DataLoader(torch.utils.data.TensorDataset(X_train, y_train),
                                           batch_size=batch_size, shuffle=True)
test_loader = torch.utils.data.DataLoader(torch.utils.data.TensorDataset(X_test, y_test),
                                          batch_size=batch_size, shuffle=False)


# define the model
class Net(torch.nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = torch.nn.Linear(30, 16)
        self.fc2 = torch.nn.Linear(16, 8)
        self.fc3 = torch.nn.Linear(8, 2)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.softmax(self.fc3(x), dim=1)
        return x


model = Net()

# define the loss function and optimizer
criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# train the model
n_epochs = 100
for epoch in range(n_epochs):
    train_loss = 0.0
    for data, target in train_loader:
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()
        with torch.no_grad():
            train_loss += loss.item() * data.size(0)

    train_loss /= len(train_loader.dataset)
    print(f'Epoch: {epoch+1}, Training Loss: {train_loss:.6f}')

# test the model
model.eval()
test_loss = 0.0
correct = 0
with torch.no_grad():
    for data, target in test_loader:
        output = model(data)
        loss = criterion(output, target)
        test_loss += loss.item() * data.size(0)
        pred = torch.argmax(output, dim=1)
        correct += torch.sum(pred == target)

test_loss /= len(test_loader.dataset)
accuracy = (correct/len(test_loader.dataset))*100
print(f'Test Loss: {test_loss:.6f}, Test Accuracy: {accuracy:.2f}%')
