import os
import numpy as np
import matplotlib.pyplot as plt
import torch


def save_rgb_image(rgb_tensor, save_path):

    if isinstance(rgb_tensor, torch.Tensor):

        rgb = rgb_tensor.detach().cpu()

        if rgb.ndim == 4:
            rgb = rgb.squeeze(0)

        if rgb.ndim == 3:
            rgb = rgb.permute(1, 2, 0)

        rgb = rgb.numpy()

    else:
        rgb = rgb_tensor

    rgb = np.clip(rgb, 0, 1)

    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    plt.imsave(save_path, rgb)