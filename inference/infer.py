import os
import sys
import numpy as np
import torch

# --------------------------------------------------
# Add project root to Python path
# --------------------------------------------------
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from training.super_resolution.model import SuperResolutionNet
from training.colorization.model import ColorizationNet
from inference.utils import normalize, save_rgb_image


# --------------------------------------------------
# Device
# --------------------------------------------------
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print("=" * 60)
print("IRVision AI Inference")
print("=" * 60)
print("Using Device:", device)


# --------------------------------------------------
# Load Models
# --------------------------------------------------
sr_model = SuperResolutionNet().to(device)
color_model = ColorizationNet().to(device)

sr_checkpoint = os.path.join(
    PROJECT_ROOT,
    "artifacts",
    "checkpoints",
    "super_resolution",
    "best_sr_model.pth",
)

color_checkpoint = os.path.join(
    PROJECT_ROOT,
    "artifacts",
    "checkpoints",
    "colorization",
    "best_color_model.pth",
)

sr_model.load_state_dict(torch.load(sr_checkpoint, map_location=device))
color_model.load_state_dict(torch.load(color_checkpoint, map_location=device))

sr_model.eval()
color_model.eval()

print("Models Loaded Successfully")


# --------------------------------------------------
# Input Sample
# --------------------------------------------------
sample = os.path.join(
    PROJECT_ROOT,
    "baseline",
    "output",
    "patches",
    "LC09",
    "sample_000",
    "tir_200m.npy",
)

thermal = np.load(sample)
thermal = normalize(thermal)

print("Original shape:", thermal.shape)

thermal = torch.from_numpy(thermal).float()

print("Tensor shape:", thermal.shape)

# Add dimensions only if necessary
if thermal.ndim == 2:
    thermal = thermal.unsqueeze(0).unsqueeze(0)

elif thermal.ndim == 3:
    thermal = thermal.unsqueeze(0)

print("Final input shape:", thermal.shape)

thermal = thermal.to(device)


# --------------------------------------------------
# Inference
# --------------------------------------------------
with torch.no_grad():

    sr = sr_model(thermal)

    rgb = color_model(sr)


# --------------------------------------------------
# Save Prediction
# --------------------------------------------------
save_path = os.path.join(
    PROJECT_ROOT,
    "results",
    "predictions",
    "sample_000_prediction.png",
)

save_rgb_image(rgb, save_path)

print("\nInference Completed Successfully.")