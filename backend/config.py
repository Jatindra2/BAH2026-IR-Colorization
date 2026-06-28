from pathlib import Path
import torch

# --------------------------------------------------
# Project Paths
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

ARTIFACTS_DIR = PROJECT_ROOT / "artifacts"

CHECKPOINT_DIR = ARTIFACTS_DIR / "checkpoints"

UPLOAD_DIR = PROJECT_ROOT / "backend" / "uploads"

OUTPUT_DIR = PROJECT_ROOT / "backend" / "outputs"

TEMP_DIR = PROJECT_ROOT / "backend" / "temp"

LOG_DIR = PROJECT_ROOT / "backend" / "logs"

# --------------------------------------------------
# Checkpoints
# --------------------------------------------------

SR_CHECKPOINT = (
    CHECKPOINT_DIR
    / "super_resolution"
    / "best_sr_model.pth"
)

COLOR_CHECKPOINT = (
    CHECKPOINT_DIR
    / "colorization"
    / "best_color_model.pth"
)

# --------------------------------------------------
# Device
# --------------------------------------------------

DEVICE = torch.device(
    "cuda"
    if torch.cuda.is_available()
    else "cpu"
)

# --------------------------------------------------
# API
# --------------------------------------------------

API_TITLE = "IRVision AI Backend"

API_VERSION = "1.0.0"

# --------------------------------------------------
# Upload Settings
# --------------------------------------------------

MAX_UPLOAD_SIZE = 100 * 1024 * 1024

SUPPORTED_EXTENSIONS = [".npy"]

# --------------------------------------------------
# Create Directories
# --------------------------------------------------

for directory in [
    UPLOAD_DIR,
    OUTPUT_DIR,
    TEMP_DIR,
    LOG_DIR,
]:
    directory.mkdir(
        parents=True,
        exist_ok=True,
    )

# --------------------------------------------------
# CORS
# --------------------------------------------------

ALLOWED_ORIGINS = [
    "http://localhost:5173",
]