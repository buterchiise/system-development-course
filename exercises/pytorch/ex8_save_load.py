import torch
from torch import nn

model = nn.Linear(1, 1)
print("保存前 weight:", model.weight.item(), "bias:", model.bias.item())

torch.save(model.state_dict(), "model.pth")

new_model = nn.Linear(1, 1)
new_model.load_state_dict(torch.load("model.pth"))
print("加载后 weight:", new_model.weight.item(), "bias:", new_model.bias.item())