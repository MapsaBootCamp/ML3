import numpy as np
import torch
import torch.nn as nn
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

data = load_breast_cancer()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train, y_train)
X_test = scaler.transform(X_test)

X_train_t = torch.from_numpy(X_train.astype(np.float32))
X_test_t = torch.from_numpy(X_test.astype(np.float32))

y_train_t = torch.from_numpy(
    y_train.astype(np.float32)).view(y_train.shape[0], 1)
y_test_t = torch.from_numpy(
    y_test.astype(np.float32)).view(y_test.shape[0], 1)

input_feature = X_test.shape[1]
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

    y_predict = model(X_train_t)
    loss = criterion(y_predict, y_train_t)

    loss.backward()

    optimizer.step()
    optimizer.zero_grad()

    if (epoch % 1 == 0):
        print(f"in epoch {epoch} loss: {loss}")

# print(
#     f"prediction x = 9 ===> {model(torch.tensor([[9]], dtype=torch.float32))}")

with torch.no_grad():
    y_predict = model(X_test_t)
    acc = y_predict.round().eq(y_test_t).sum() / y_test_t.shape[0]
    print("accuracy: ", acc.item())
