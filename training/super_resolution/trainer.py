import os
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
        self.best_loss = float("inf")

        self.checkpoint_dir = os.path.join(
            "..",
            "..",
            "artifacts",
            "checkpoints",
            "super_resolution",
        )

        os.makedirs(self.checkpoint_dir, exist_ok=True)

    def train_one_epoch(self):

        self.model.train()

        running_loss = 0.0

        total_batches = len(self.dataloader)

        for batch_idx, batch in enumerate(self.dataloader):

            lr_tir = batch["lr_tir"].to(self.device)
            hr_tir = batch["hr_tir"].to(self.device)

            self.optimizer.zero_grad()

            prediction = self.model(lr_tir)

            loss = self.criterion(prediction, hr_tir)

            loss.backward()

            self.optimizer.step()

            running_loss += loss.item()

            print(
                f"Batch [{batch_idx+1}/{total_batches}] "
                f"Loss: {loss.item():.6f}"
            )

        return running_loss / total_batches

    def fit(self):

        epochs = self.config["training"]["epochs"]

        print("\nStarting Super Resolution Training...\n")

        for epoch in range(epochs):

            print("=" * 60)
            print(f"Epoch {epoch + 1}/{epochs}")

            epoch_loss = self.train_one_epoch()

            print(f"Average Loss : {epoch_loss:.6f}\n")

            # Save latest checkpoint
            torch.save(
                self.model.state_dict(),
                os.path.join(self.checkpoint_dir, "last_sr_model.pth"),
            )

            # Save best checkpoint
            if epoch_loss < self.best_loss:

                self.best_loss = epoch_loss

                torch.save(
                    self.model.state_dict(),
                    os.path.join(self.checkpoint_dir, "best_sr_model.pth"),
                )

                print("✅ Best model saved.")

        print("\nTraining Completed Successfully.")