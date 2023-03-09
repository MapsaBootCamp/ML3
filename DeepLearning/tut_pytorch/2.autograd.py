import torch

x = torch.tensor([1, 2, 3, 4], dtype=torch.float32, requires_grad=True)
w = torch.tensor([2, 3, 4, 6], dtype=torch.float32, requires_grad=True)
y = torch.zeros(4)

# y = w * x
# z = 5 * y ** 2
# z = z.mean()
# z.backward()

# print(x.grad)
# print(w.grad)


for epoch in range(2):
    y = w * x
    z = 5 * y ** 2
    z = z.mean()
    z.backward()
    print(x.grad)
    x.grad.data.zero_()
