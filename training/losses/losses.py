import torch
import torch.nn as nn


class ColorizationLoss(nn.Module):
    """
    Basic L1 reconstruction loss for RGB prediction.
    """

    def __init__(self):
        super().__init__()
        self.l1 = nn.L1Loss()

    def forward(self, prediction, target):
        return self.l1(prediction, target)