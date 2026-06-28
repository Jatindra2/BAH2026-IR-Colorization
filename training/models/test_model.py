import torch

from super_resolution_net import SuperResolutionNet


model = SuperResolutionNet()

x = torch.randn(1, 1, 256, 256)

y = model(x)

print("Input :", x.shape)

print("Output:", y.shape)