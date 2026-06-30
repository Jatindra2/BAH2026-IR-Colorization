import os
import sys
import cv2

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

    min_val = image.min()
    max_val = image.max()
    if max_val > min_val:
        image = (image - min_val) / (max_val - min_val + 1e-8)
    elif max_val > 0:
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

    # Colorization (predict ab channels)
    ab_output = color_model(sr)

    # -----------------------------
    # Convert LAB to RGB
    # -----------------------------
    sr_np = sr.squeeze(0).squeeze(0).detach().cpu().numpy() # Shape: (512, 512), range: [0, 1]
    ab_np = ab_output.squeeze(0).detach().cpu().numpy()     # Shape: (2, 512, 512), range: [0, 1]

    # Rescale to native LAB values and amplify colors
    L = sr_np * 100.0
    a = (ab_np[0] * 255.0 - 128.0) * 10.0
    b = (ab_np[1] * 255.0 - 128.0) * 10.0

    # Stack to (512, 512, 3) LAB image
    lab = np.stack([L, a, b], axis=-1).astype(np.float32)

    # Convert to RGB using cv2
    rgb_output = cv2.cvtColor(lab, cv2.COLOR_LAB2RGB)
    rgb_output = np.clip(rgb_output, 0, 1)

    # -----------------------------
    # Save Image
    # -----------------------------
    save_rgb_image(rgb_output, str(output_path))

    # Convert both SR and colorized outputs to base64 PNG data URLs
    import base64
    import io
    from PIL import Image

    # Grayscale SR image conversion
    sr_uint8 = np.clip(sr_np * 255.0, 0, 255).astype(np.uint8)
    sr_img = Image.fromarray(sr_uint8)
    sr_io = io.BytesIO()
    sr_img.save(sr_io, format="PNG")
    sr_base64 = base64.b64encode(sr_io.getvalue()).decode("utf-8")

    # RGB colorized image conversion
    rgb_uint8 = np.clip(rgb_output * 255.0, 0, 255).astype(np.uint8)
    rgb_img = Image.fromarray(rgb_uint8)
    rgb_io = io.BytesIO()
    rgb_img.save(rgb_io, format="PNG")
    rgb_base64 = base64.b64encode(rgb_io.getvalue()).decode("utf-8")

    return {
        "sr": f"data:image/png;base64,{sr_base64}",
        "colorized": f"data:image/png;base64,{rgb_base64}"
    }

logger.info("Prediction saved successfully.")