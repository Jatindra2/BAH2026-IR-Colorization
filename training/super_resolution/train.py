import os
import sys
import yaml
import torch
import torch.nn as nn
from torch.utils.data import DataLoader

# Allow importing from training/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from datasets.ir_dataset import IRDataset
from super_resolution.model import SuperResolutionNet
from super_resolution.trainer import Trainer


# --------------------------------------------------
# Load Configuration
# --------------------------------------------------
CONFIG_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "configs",
    "config.yaml"
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
print("Super Resolution Training")
print("=" * 60)

print(f"Using Device : {device}")


# --------------------------------------------------
# Dataset
# --------------------------------------------------
dataset = IRDataset(config["dataset"]["root"])

print(f"Dataset Loaded Successfully")
print(f"Total Samples : {len(dataset)}")


dataloader = DataLoader(
    dataset,
    batch_size=config["dataloader"]["batch_size"],
    shuffle=config["dataloader"]["shuffle"],
    num_workers=config["dataloader"]["num_workers"],
)


# --------------------------------------------------
# Model
# --------------------------------------------------
model = SuperResolutionNet()

print("Super Resolution Model Created")


# --------------------------------------------------
# Loss
# --------------------------------------------------
criterion = nn.L1Loss()


# --------------------------------------------------
# Optimizer
# --------------------------------------------------
optimizer = torch.optim.Adam(
    model.parameters(),
    lr=config["training"]["learning_rate"],
)


# --------------------------------------------------
# Trainer
# --------------------------------------------------
trainer = Trainer(
    model=model,
    dataloader=dataloader,
    criterion=criterion,
    optimizer=optimizer,
    device=device,
    config=config,
)


# --------------------------------------------------
# Train
# --------------------------------------------------
trainer.fit()