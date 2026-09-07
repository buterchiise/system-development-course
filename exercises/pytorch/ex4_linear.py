import torch
from torch import nn

layer = nn.Linear(2, 3)
x = torch.tensor([[1.0, 2.0]])
out = layer(x)
print("输出形状:", out.shape)
print("输出:", out)