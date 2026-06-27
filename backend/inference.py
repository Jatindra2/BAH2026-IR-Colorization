import os
import sys

import numpy as np
import torch

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from inference.utils import normalize, save_rgb_image


def predict_image(
    image_path,
    sr_model,
    color_model,
):

    device = next(sr_model.parameters()).device

    thermal = np.load(image_path)

    thermal = normalize(thermal)

    thermal = torch.from_numpy(
        thermal
    ).float()

    if thermal.ndim == 2:
        thermal = thermal.unsqueeze(0).unsqueeze(0)

    elif thermal.ndim == 3:
        thermal = thermal.unsqueeze(0)

    thermal = thermal.to(device)

    with torch.no_grad():

        sr = sr_model(thermal)

        prediction = color_model(sr)

    prediction = (
        prediction.squeeze(0)
        .permute(1, 2, 0)
        .cpu()
        .numpy()
    )

    os.makedirs(
        "temp",
        exist_ok=True,
    )

    output_path = os.path.join(
        "temp",
        "prediction.png",
    )

    save_rgb_image(
        prediction,
        output_path,
    )

    return output_path