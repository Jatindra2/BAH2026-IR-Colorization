import torch.nn as nn
import segmentation_models_pytorch as smp


class SuperResolutionNet(nn.Module):
    def __init__(self):
        super().__init__()

        self.unet = smp.Unet(
            encoder_name="resnet18",
            encoder_weights=None,
            in_channels=1,
            classes=1,
            activation=None,
        )

        self.upsample = nn.Upsample(
            scale_factor=2,
            mode="bilinear",
            align_corners=False,
        )

    def forward(self, x):
        x = self.unet(x)      # (B,1,256,256)
        x = self.upsample(x)  # (B,1,512,512)
        return x