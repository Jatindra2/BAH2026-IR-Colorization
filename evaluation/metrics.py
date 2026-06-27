import numpy as np
from skimage.metrics import peak_signal_noise_ratio
from skimage.metrics import structural_similarity


def calculate_psnr(prediction, target):

    return peak_signal_noise_ratio(
        target,
        prediction,
        data_range=1.0,
    )


def calculate_ssim(prediction, target):

    return structural_similarity(
        target,
        prediction,
        channel_axis=2,
        data_range=1.0,
    )