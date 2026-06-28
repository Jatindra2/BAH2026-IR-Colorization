import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
from pathlib import Path
import torch

from training.super_resolution.model import SuperResolutionNet
from training.colorization.model import ColorizationNet

ROOT = Path(__file__).resolve().parent.parent

SR_CHECKPOINT = (
    ROOT
    / "artifacts"
    / "checkpoints"
    / "super_resolution"
    / "best_sr_model.pth"
)

COLOR_CHECKPOINT = (
    ROOT
    / "artifacts"
    / "checkpoints"
    / "colorization"
    / "best_color_model.pth"
)

DEVICE = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)


def load_super_resolution_model():

    model = SuperResolutionNet()

    if SR_CHECKPOINT.exists():

        checkpoint = torch.load(
            SR_CHECKPOINT,
            map_location=DEVICE,
        )

        if isinstance(checkpoint, dict):

            if "model_state_dict" in checkpoint:
                checkpoint = checkpoint["model_state_dict"]

            elif "state_dict" in checkpoint:
                checkpoint = checkpoint["state_dict"]

        model.load_state_dict(checkpoint)

        print("✓ Loaded Super Resolution model")

    else:

        print("⚠ Super Resolution checkpoint not found.")

    model.to(DEVICE)
    model.eval()

    return model


def load_colorization_model():

    model = ColorizationNet()

    if COLOR_CHECKPOINT.exists():

        checkpoint = torch.load(
            COLOR_CHECKPOINT,
            map_location=DEVICE,
        )

        if isinstance(checkpoint, dict):

            if "model_state_dict" in checkpoint:
                checkpoint = checkpoint["model_state_dict"]

            elif "state_dict" in checkpoint:
                checkpoint = checkpoint["state_dict"]

        model.load_state_dict(checkpoint)

        print("✓ Loaded Colorization model")

    else:

        print("⚠ Colorization checkpoint not found.")

    model.to(DEVICE)
    model.eval()

    return model

# --------------------------------------------------
# Cache Loaded Models
# --------------------------------------------------

_sr_model = None
_color_model = None


def get_models():

    global _sr_model
    global _color_model

    if _sr_model is None:
        _sr_model = load_super_resolution_model()

    if _color_model is None:
        _color_model = load_colorization_model()

    return _sr_model, _color_model