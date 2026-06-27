import os
import yaml
import torch
from torch.utils.data import DataLoader

from datasets.ir_dataset import IRDataset
from models.colorization_net import ColorizationNet
from losses.losses import ColorizationLoss
from trainers.trainer import Trainer


# -----------------------------------
# Load Configuration
# -----------------------------------
CONFIG_PATH = os.path.join("configs", "config.yaml")

with open(CONFIG_PATH, "r") as file:
    config = yaml.safe_load(file)


# -----------------------------------
# Device
# -----------------------------------
device = torch.device(
    "cuda"
    if torch.cuda.is_available()
    and config["training"]["device"] == "cuda"
    else "cpu"
)

print("=" * 60)
print("IR Colorization Training")
print("=" * 60)
print(f"Using Device : {device}")


# -----------------------------------
# Dataset
# -----------------------------------
dataset = IRDataset(config["dataset"]["root"])

print(f"Dataset Loaded Successfully")
print(f"Total Samples : {len(dataset)}")

dataloader = DataLoader(
    dataset,
    batch_size=config["dataloader"]["batch_size"],
    shuffle=config["dataloader"]["shuffle"],
    num_workers=config["dataloader"]["num_workers"],
)


# -----------------------------------
# Model
# -----------------------------------
model = ColorizationNet()

print("Model Created Successfully")


# -----------------------------------
# Loss Function
# -----------------------------------
criterion = ColorizationLoss()


# -----------------------------------
# Optimizer
# -----------------------------------
optimizer = torch.optim.Adam(
    model.parameters(),
    lr=config["training"]["learning_rate"],
)


# -----------------------------------
# Trainer
# -----------------------------------
trainer = Trainer(
    model=model,
    dataloader=dataloader,
    criterion=criterion,
    optimizer=optimizer,
    device=device,
    config=config,
)


# -----------------------------------
# Start Training
# -----------------------------------
print("\nStarting Training...\n")

trainer.fit()

print("\nTraining Completed Successfully!")