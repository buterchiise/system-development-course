import torch
from torch import nn

pred = torch.tensor([[0.2, 0.8]])
target = torch.tensor([1])

mse = nn.MSELoss()(pred, torch.tensor([[0.0, 1.0]]))
ce = nn.CrossEntropyLoss()(pred, target)

print("MSE:", mse.item())
print("CrossEntropy:", ce.item())