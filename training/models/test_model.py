import torch

from colorization_net import ColorizationNet

model = ColorizationNet()

x = torch.randn(2, 1, 512, 512)

y = model(x)

print("Input Shape :", x.shape)
print("Output Shape:", y.shape)

print("\nModel Loaded Successfully ✅")