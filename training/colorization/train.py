import os
import sys
import yaml
import torch
from torch.utils.data import DataLoader

# Allow imports from training/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from datasets.ir_dataset import IRDataset
from losses.losses import ColorizationLoss
from super_resolution.model import SuperResolutionNet
from colorization.model import ColorizationNet
from colorization.trainer import Trainer


# --------------------------------------------------
# Config
# --------------------------------------------------
CONFIG_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "configs",
    "config.yaml",
)

with open(CONFIG_PATH, "r") as f:
    config = yaml.safe_load(f)


# --------------------------------------------------
# Device
# --------------------------------------------------
device = torch.device(
    "cuda"
    if torch.cuda.is_available()
    and config["training"]["device"] == "cuda"
    else "cpu"
)

print("=" * 60)
print("Colorization Training")
print("=" * 60)
print(f"Using Device : {device}")


# --------------------------------------------------
# Dataset
# --------------------------------------------------
dataset = IRDataset(config["dataset"]["root"])

print("Dataset Loaded Successfully")
print(f"Total Samples : {len(dataset)}")

dataloader = DataLoader(
    dataset,
    batch_size=config["dataloader"]["batch_size"],
    shuffle=config["dataloader"]["shuffle"],
    num_workers=config["dataloader"]["num_workers"],
)


# --------------------------------------------------
# Load Super Resolution Model
# --------------------------------------------------
sr_model = SuperResolutionNet()

checkpoint = os.path.join(
    "..",
    "..",
    "artifacts",
    "checkpoints",
    "super_resolution",
    "best_sr_model.pth",
)

sr_model.load_state_dict(
    torch.load(checkpoint, map_location=device)
)

print("Super Resolution Model Loaded")


# --------------------------------------------------
# Colorization Model
# --------------------------------------------------
color_model = ColorizationNet()

print("Colorization Model Created")


# --------------------------------------------------
# Loss
# --------------------------------------------------
criterion = ColorizationLoss()


# --------------------------------------------------
# Optimizer
# --------------------------------------------------
optimizer = torch.optim.Adam(
    color_model.parameters(),
    lr=config["training"]["learning_rate"],
)


# --------------------------------------------------
# Trainer
# --------------------------------------------------
trainer = Trainer(
    sr_model=sr_model,
    color_model=color_model,
    dataloader=dataloader,
    criterion=criterion,
    optimizer=optimizer,
    device=device,
    config=config,
)


trainer.fit()