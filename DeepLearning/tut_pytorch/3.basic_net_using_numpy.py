import numpy as np


#### y = 3 * x + 2

X = np.array([[2], [3], [4], [5], [6], [8], [12], [-2]], dtype=np.float32)
y = np.array([8, 11, 14, 17, 20, 26, 38, -4], dtype=np.float32).reshape(-1, 1)


w = np.random.randn(1)
b = np.random.randn(1)


def forward(x, w, b):
    return x * w + b


def _loss(y, y_predict):
    return ((y_predict - y)**2).mean()


def gradient(x, y, w, b):
    return 2 * np.multiply((x * w + b) - y, x).mean(), 2 * ((x * w + b) - y).mean()


learning_rate = 0.01
epochs = 200


for epoch in range(epochs):
    y_predict = forward(X, w, b)

    loss = _loss(y, y_predict)

    dw, db = gradient(X, y, w, b)

    w -= learning_rate * dw
    b -= learning_rate * db
    if (epoch % 10 == 0):
        print(f"in epoch {epoch} loss: {loss} w: {w} b: {b}")

print(f"prediction x = 9 ===> {forward([[9]], w, b)}")
