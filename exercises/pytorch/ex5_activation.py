import torch
from torch import nn

x = torch.tensor([-1.0, 0.0, 1.0])
relu = nn.ReLU()
sigmoid = nn.Sigmoid()

print("ReLU:", relu(x))
print("Sigmoid:", sigmoid(x))