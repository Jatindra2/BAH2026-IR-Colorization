import torch.nn as nn
import segmentation_models_pytorch as smp


class ColorizationNet(nn.Module):
    def __init__(self):
        super().__init__()

        self.unet = smp.Unet(
            encoder_name="resnet18",
            encoder_weights=None,
            in_channels=1,
            classes=2,
            activation="sigmoid",
        )

    def forward(self, x):
        return self.unet(x)