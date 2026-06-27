import torch
from model import ColorizationNet

model = ColorizationNet()

x = torch.randn(2, 1, 512, 512)

y = model(x)

print("Input :", x.shape)
print("Output:", y.shape)

assert y.shape == (2, 3, 512, 512)

print("\nColorization Model OK ✅")