import os
import sys
import torch

# --------------------------------------------------
# Add project root to Python path
# --------------------------------------------------
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from training.super_resolution.model import SuperResolutionNet
from training.colorization.model import ColorizationNet

# --------------------------------------------------
# Device
# --------------------------------------------------
device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)


def load_models():
    """
    Load the trained Super Resolution and Colorization models.
    """

    # --------------------------------------------------
    # Initialize Models
    # --------------------------------------------------
    sr_model = SuperResolutionNet().to(device)
    color_model = ColorizationNet().to(device)

    # --------------------------------------------------
    # Checkpoint Paths
    # --------------------------------------------------
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

    # --------------------------------------------------
    # Verify checkpoints exist
    # --------------------------------------------------
    if not os.path.exists(sr_checkpoint):
        raise FileNotFoundError(
            f"Super Resolution checkpoint not found:\n{sr_checkpoint}"
        )

    if not os.path.exists(color_checkpoint):
        raise FileNotFoundError(
            f"Colorization checkpoint not found:\n{color_checkpoint}"
        )

    # --------------------------------------------------
    # Load Weights
    # --------------------------------------------------
    sr_model.load_state_dict(
        torch.load(sr_checkpoint, map_location=device)
    )

    color_model.load_state_dict(
        torch.load(color_checkpoint, map_location=device)
    )

    # --------------------------------------------------
    # Evaluation Mode
    # --------------------------------------------------
    sr_model.eval()
    color_model.eval()

    print("✅ Models Loaded Successfully")

    return sr_model, color_model