import os
import sys
import cv2

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
import torch
import numpy as np
from pathlib import Path

from backend.model_loader import get_models
from backend.logger import logger
from backend.utils import save_rgb_image


from backend.config import DEVICE

# Load models once
sr_model, color_model = get_models()


def predict_image(input_path: Path, output_path: Path):

    # -----------------------------
    # Load .npy thermal image
    # -----------------------------
    image = np.load(input_path)

    if image.ndim == 3:
        image = image.squeeze(0)

    image = image.astype(np.float32)

    min_val = image.min()
    max_val = image.max()

    if max_val > min_val:
        image = (image - min_val) / (max_val - min_val + 1e-8)
    elif max_val > 0:
        image = image / max_val

    tensor = torch.from_numpy(image).unsqueeze(0).unsqueeze(0).to(DEVICE)

    logger.info("Running AI inference...")

    # -----------------------------
    # MEMORY OPTIMIZATION
    # -----------------------------
    with torch.no_grad():

        # Super Resolution
        sr = sr_model(tensor)

        # Colorization
        ab_output = color_model(sr)

    # -----------------------------
    # Convert LAB → RGB
    # -----------------------------
    sr_np = sr.squeeze(0).squeeze(0).detach().cpu().numpy()
    ab_np = ab_output.squeeze(0).detach().cpu().numpy()
    L = sr_np * 100.0
    a = (ab_np[0] * 255.0 - 128.0) * 10.0
    b = (ab_np[1] * 255.0 - 128.0) * 10.0

    lab = np.stack([L, a, b], axis=-1).astype(np.float32)

    rgb_output = cv2.cvtColor(lab, cv2.COLOR_LAB2RGB)
    rgb_output = np.clip(rgb_output, 0, 1)

    save_rgb_image(rgb_output, str(output_path))

    import base64
    import io
    from PIL import Image
    import gc

    # SR image
    sr_uint8 = (sr_np * 255).clip(0,255).astype(np.uint8)
    sr_img = Image.fromarray(sr_uint8)
    sr_buffer = io.BytesIO()
    sr_img.save(sr_buffer, format="PNG")
    sr_base64 = base64.b64encode(sr_buffer.getvalue()).decode()

    # RGB image
    rgb_uint8 = (rgb_output * 255).clip(0,255).astype(np.uint8)
    rgb_img = Image.fromarray(rgb_uint8)
    rgb_buffer = io.BytesIO()
    rgb_img.save(rgb_buffer, format="PNG")
    rgb_base64 = base64.b64encode(rgb_buffer.getvalue()).decode()

    # -----------------------------
    # FREE MEMORY
    # -----------------------------
    del tensor
    del sr
    del ab_output
    del image
    del sr_np
    del ab_np
    del lab
    del rgb_output
    del sr_buffer
    del rgb_buffer

    gc.collect()

    if torch.cuda.is_available():
        torch.cuda.empty_cache()

    return {
        "sr": f"data:image/png;base64,{sr_base64}",
        "colorized": f"data:image/png;base64,{rgb_base64}",
    }
logger.info("Prediction saved successfully.")
