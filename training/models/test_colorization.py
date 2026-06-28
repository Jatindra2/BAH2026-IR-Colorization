import torch

from colorization_net import ColorizationNet

model = ColorizationNet()

x = torch.randn(1, 1, 512, 512)

y = model(x)

print("Input :", x.shape)

print("Output:", y.shape)