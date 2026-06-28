import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
import torch
import numpy as np
from pathlib import Path

from model_loader import get_models
from logger import logger
from utils import save_rgb_image


from config import DEVICE

# Load models once
sr_model, color_model = get_models()


def predict_image(input_path: Path, output_path: Path):

    # -----------------------------
    # Load .npy thermal image
    # -----------------------------
    image = np.load(input_path)

    # Remove batch dimension if present
    if image.ndim == 3:
        image = image.squeeze(0)

    image = image.astype(np.float32)

    # -----------------------------
    # Normalize safely
    # -----------------------------
    max_val = image.max()

    if max_val > 0:
        image = image / max_val

    # -----------------------------
    # Convert to Tensor
    # -----------------------------
    tensor = torch.from_numpy(image)

    tensor = tensor.unsqueeze(0).unsqueeze(0)

    tensor = tensor.to(DEVICE)

    # -----------------------------
    # AI Inference
    # -----------------------------
    logger.info("Running AI inference...")
    # Super Resolution
    sr = sr_model(tensor)

    # Colorization
    rgb_output = color_model(sr)

    # -----------------------------
    # Convert Output
    # -----------------------------
    rgb_output = rgb_output.squeeze(0)

    rgb_output = rgb_output.permute(1, 2, 0)

    rgb_output = rgb_output.detach().cpu().numpy()

    rgb_output = np.clip(rgb_output, 0, 1)

    # -----------------------------
    # Save Image
    # -----------------------------
    save_rgb_image(rgb_output, str(output_path))

    return output_path

logger.info("Prediction saved successfully.")