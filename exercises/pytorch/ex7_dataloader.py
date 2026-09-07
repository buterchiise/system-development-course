import torch
from torch.utils.data import TensorDataset, DataLoader

x = torch.arange(8).reshape(4, 2)
y = torch.tensor([0, 1, 0, 1])

dataset = TensorDataset(x, y)
loader = DataLoader(dataset, batch_size=2, shuffle=False)

for batch_x, batch_y in loader:
    print("x shape:", batch_x.shape, "y:", batch_y)