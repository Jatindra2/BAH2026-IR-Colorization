import os
import sys
import numpy as np
import torch

# ----------------------------------------------------
# Project Root
# ----------------------------------------------------
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from training.super_resolution.model import SuperResolutionNet
from training.colorization.model import ColorizationNet
from inference.utils import normalize
from metrics import calculate_psnr, calculate_ssim

# ----------------------------------------------------
# Device
# ----------------------------------------------------
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print("=" * 60)
print("Evaluation")
print("=" * 60)
print("Device :", device)

# ----------------------------------------------------
# Load Models
# ----------------------------------------------------
sr_model = SuperResolutionNet().to(device)
color_model = ColorizationNet().to(device)

sr_model.load_state_dict(
    torch.load(
        os.path.join(
            PROJECT_ROOT,
            "artifacts",
            "checkpoints",
            "super_resolution",
            "best_sr_model.pth",
        ),
        map_location=device,
    )
)

color_model.load_state_dict(
    torch.load(
        os.path.join(
            PROJECT_ROOT,
            "artifacts",
            "checkpoints",
            "colorization",
            "best_color_model.pth",
        ),
        map_location=device,
    )
)

sr_model.eval()
color_model.eval()

print("Models Loaded Successfully")

# ----------------------------------------------------
# Dataset
# ----------------------------------------------------
patch_root = os.path.join(
    PROJECT_ROOT,
    "baseline",
    "output",
    "patches",
    "LC09",
)

samples = sorted(os.listdir(patch_root))

psnr_scores = []
ssim_scores = []

print(f"Found {len(samples)} samples\n")

# ----------------------------------------------------
# Evaluation Loop
# ----------------------------------------------------
for sample in samples:

    sample_dir = os.path.join(patch_root, sample)

    lr = np.load(os.path.join(sample_dir, "tir_200m.npy"))
    rgb_gt = np.load(os.path.join(sample_dir, "rgb_100m_512.npy"))

    lr = normalize(lr)
    rgb_gt = normalize(rgb_gt)

    # Convert CHW -> HWC if needed
    if rgb_gt.ndim == 3 and rgb_gt.shape[0] == 3:
        rgb_gt = np.transpose(rgb_gt, (1, 2, 0))

    lr = torch.from_numpy(lr).float()

    if lr.ndim == 2:
        lr = lr.unsqueeze(0).unsqueeze(0)
    elif lr.ndim == 3:
        lr = lr.unsqueeze(0)

    lr = lr.to(device)

    with torch.no_grad():

        sr = sr_model(lr)
        pred = color_model(sr)

    pred = (
        pred.squeeze(0)
        .permute(1, 2, 0)
        .cpu()
        .numpy()
    )

    psnr = calculate_psnr(pred, rgb_gt)
    ssim = calculate_ssim(pred, rgb_gt)

    psnr_scores.append(psnr)
    ssim_scores.append(ssim)

    print(
        f"{sample:12s} "
        f"PSNR = {psnr:.2f} "
        f"SSIM = {ssim:.4f}"
    )

# ----------------------------------------------------
# Average
# ----------------------------------------------------
print("\n" + "=" * 60)

print(f"Average PSNR : {np.mean(psnr_scores):.2f}")

print(f"Average SSIM : {np.mean(ssim_scores):.4f}")

print("=" * 60)