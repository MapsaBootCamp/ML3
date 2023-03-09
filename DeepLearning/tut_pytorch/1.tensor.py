import torch


data = [[1, 2], [3, 4]]
x_data = torch.tensor(data)
print(x_data)
x_data.add_(2)
print(x_data)
