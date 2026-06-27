from utils.config import load_config

config = load_config("configs/config.yaml")

print(config)
print()
print("Batch Size :", config["dataloader"]["batch_size"])
print("Epochs :", config["training"]["epochs"])
print("Learning Rate :", config["training"]["learning_rate"])