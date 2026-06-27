import torch

from models.colorization_net import ColorizationNet
from losses.losses import ColorizationLoss


model = ColorizationNet()
criterion = ColorizationLoss()

x = torch.randn(2, 1, 512, 512)
target = torch.rand(2, 3, 512, 512)

prediction = model(x)

loss = criterion(prediction, target)

print("Prediction :", prediction.shape)
print("Target     :", target.shape)
print("Loss       :", loss.item())

print("\nLoss Module Working Successfully ✅")