import torch
from model import SuperResolutionNet

model = SuperResolutionNet()

x = torch.randn(2, 1, 256, 256)

y = model(x)

print("Input :", x.shape)
print("Output:", y.shape)

assert y.shape == (2, 1, 512, 512)

print("\nSuper Resolution Model OK ✅")