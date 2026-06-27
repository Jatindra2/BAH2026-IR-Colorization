import torch
import torch.nn as nn


class AttentionGate(nn.Module):
    """
    Attention Gate for skip connections.
    """

    def __init__(self, gate_channels, skip_channels, inter_channels):
        super().__init__()

        self.gate = nn.Sequential(
            nn.Conv2d(gate_channels, inter_channels, kernel_size=1, bias=False),
            nn.BatchNorm2d(inter_channels),
        )

        self.skip = nn.Sequential(
            nn.Conv2d(skip_channels, inter_channels, kernel_size=1, bias=False),
            nn.BatchNorm2d(inter_channels),
        )

        self.psi = nn.Sequential(
            nn.ReLU(inplace=True),
            nn.Conv2d(inter_channels, 1, kernel_size=1),
            nn.Sigmoid(),
        )

    def forward(self, gate, skip):

        g = self.gate(gate)
        x = self.skip(skip)

        alpha = self.psi(g + x)

        return skip * alpha