import torch


class Trainer:
    def __init__(
        self,
        model,
        dataloader,
        criterion,
        optimizer,
        device,
        config,
    ):
        self.model = model.to(device)
        self.dataloader = dataloader
        self.criterion = criterion
        self.optimizer = optimizer
        self.device = device
        self.config = config

    def train_one_epoch(self):
        self.model.train()

        running_loss = 0.0
        total_batches = len(self.dataloader)

        if total_batches == 0:
            raise ValueError("Dataset is empty. Please check the dataset path and generated patches.")

        for batch_idx, batch in enumerate(self.dataloader):

            lr_tir = batch["lr_tir"].to(self.device)
            rgb_gt = batch["rgb"].to(self.device)

            self.optimizer.zero_grad()

            prediction = self.model(lr_tir)

            loss = self.criterion(prediction, rgb_gt)

            loss.backward()

            self.optimizer.step()

            running_loss += loss.item()

            print(
                f"Batch [{batch_idx + 1}/{total_batches}] "
                f"Loss: {loss.item():.6f}"
            )

        return running_loss / total_batches

    def fit(self):

        epochs = self.config["training"]["epochs"]

        for epoch in range(epochs):

            print("\n" + "=" * 60)
            print(f"Epoch {epoch + 1}/{epochs}")

            epoch_loss = self.train_one_epoch()

            print(f"Average Epoch Loss: {epoch_loss:.6f}")

        print("\nTraining Finished Successfully!")