import torch

t = torch.arange(9).reshape(3, 3)
print("t =", t)
print("第二行:", t[1])
print("第一列:", t[:, 0])
print("对角线:", t.diag())