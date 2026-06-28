from torch.utils.data import DataLoader
from ir_dataset import IRDataset

dataset = IRDataset("../../baseline/output/patches")

print("Total Samples:", len(dataset))

sample = dataset[0]

print("Low Resolution Thermal :", sample["lr_tir"].shape)
print("High Resolution Thermal:", sample["hr_tir"].shape)
print("RGB :", sample["rgb"].shape)

loader = DataLoader(dataset, batch_size=2, shuffle=True)

batch = next(iter(loader))

print("\nBatch Shapes")

print(batch["lr_tir"].shape)
print(batch["hr_tir"].shape)
print(batch["rgb"].shape)