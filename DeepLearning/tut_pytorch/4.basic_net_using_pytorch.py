import torch
import torch.nn as nn

X = torch.tensor([[2], [3], [4], [5], [6], [8], [12],
                 [-2], [20], [17]], dtype=torch.float32)
y = torch.tensor([8, 11, 14, 17, 20, 26, 38, -4, 62, 53],
                 dtype=torch.float32).view(-1, 1)

w = torch.tensor(0, dtype=torch.float32, requires_grad=True)
b = torch.tensor(0, dtype=torch.float32, requires_grad=True)
c = torch.tensor(0, dtype=torch.float32, requires_grad=True)


# def forward(x, w, b):
#     return x * w + b

# model = nn.Linear(1, 1)


class MyModel(nn.Module):

    def __init__(self, in_feature, out_feature) -> None:
        super().__init__()
        self.lr = nn.Linear(in_feature, out_feature)

    def forward(self, x):
        return self.lr(x)


model = MyModel(1, 1)

# def _loss(y, y_predict):
#     return ((y_predict - y)**2).mean()

learning_rate = 0.1
epochs = 2000

criterion = nn.MSELoss()
# optimizer = torch.optim.SGD([w, b], lr=learning_rate)
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

for epoch in range(epochs):
    # y_predict = forward(X, w, b)
    y_predict = model(X)
    loss = criterion(y, y_predict)

    loss.backward()

    optimizer.step()
    optimizer.zero_grad()
    # with torch.no_grad():
    #     w -= learning_rate * w.grad
    #     b -= learning_rate * b.grad

    # w.grad.zero_()
    # b.grad.zero_()
    [w, b] = model.parameters()
    if (epoch % 2 == 0):
        print(f"in epoch {epoch} loss: {loss} w: {w.item()} b: {b.item()}")

print(
    f"prediction x = 9 ===> {model(torch.tensor([[9]], dtype=torch.float32))}")
