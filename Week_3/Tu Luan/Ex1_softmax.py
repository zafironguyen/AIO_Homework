import torch
import torch.nn as nn
import torch.nn.functional as F


class Softmax(nn.Module):
    def forward(self, x):
        return F.softmax(x, dim=0)


class SoftmaxStable(nn.Module):
    def forward(self, x):
        x_exp = torch.exp(x - torch.max(x))
        return x_exp / x_exp.sum(dim=0)


data = torch.Tensor([1, 2, 3])
softmax = Softmax()
output = softmax(data)
print(output)


data = torch.Tensor([1, 2, 3])
softmax_stable = SoftmaxStable()
output = softmax_stable(data)
print(output)
