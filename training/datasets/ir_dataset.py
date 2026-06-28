import os
import numpy as np
import torch
from torch.utils.data import Dataset


class IRDataset(Dataset):
    """
    Dataset for IR Colorization.

    Each sample contains:
        - Low Resolution Thermal (256x256)
        - High Resolution Thermal (512x512)
        - RGB Ground Truth (512x512)
    """

    def __init__(self, root_dir):
        self.samples = []

        for product in sorted(os.listdir(root_dir)):

            # Ignore the demo folder from the official baseline
            if product.lower() == "demo":
                continue

            product_path = os.path.join(root_dir, product)

            if not os.path.isdir(product_path):
                continue

            for sample in sorted(os.listdir(product_path)):
                sample_path = os.path.join(product_path, sample)

                if os.path.isdir(sample_path):
                    self.samples.append(sample_path)

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):

        sample = self.samples[idx]

        lr_tir = np.load(os.path.join(sample, "tir_200m.npy"))
        hr_tir = np.load(os.path.join(sample, "tir_100m_512.npy"))
        rgb = np.load(os.path.join(sample, "rgb_100m_512.npy"))

        lr_tir = torch.from_numpy(lr_tir).float()
        hr_tir = torch.from_numpy(hr_tir).float()
        rgb = torch.from_numpy(rgb).float()

        # Normalize to [0,1]
        lr_tir = (lr_tir - lr_tir.min()) / (lr_tir.max() - lr_tir.min() + 1e-8)
        hr_tir = (hr_tir - hr_tir.min()) / (hr_tir.max() - hr_tir.min() + 1e-8)
        rgb = (rgb - rgb.min()) / (rgb.max() - rgb.min() + 1e-8)

        return {
            "lr_tir": lr_tir,
            "hr_tir": hr_tir,
            "rgb": rgb,
        }