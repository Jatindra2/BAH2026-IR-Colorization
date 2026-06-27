import os
import torch


class Trainer:

    def __init__(
        self,
        sr_model,
        color_model,
        dataloader,
        criterion,
        optimizer,
        device,
        config,
    ):

        self.sr_model = sr_model.to(device)
        self.color_model = color_model.to(device)

        self.dataloader = dataloader
        self.criterion = criterion
        self.optimizer = optimizer
        self.device = device
        self.config = config

        # Freeze SR model
        self.sr_model.eval()

        for param in self.sr_model.parameters():
            param.requires_grad = False

        self.best_loss = float("inf")

        self.checkpoint_dir = os.path.join(
            "..",
            "..",
            "artifacts",
            "checkpoints",
            "colorization",
        )

        os.makedirs(self.checkpoint_dir, exist_ok=True)

    def train_one_epoch(self):

        self.color_model.train()

        running_loss = 0.0

        total_batches = len(self.dataloader)

        for batch_idx, batch in enumerate(self.dataloader):

            lr_tir = batch["lr_tir"].to(self.device)
            rgb_gt = batch["rgb"].to(self.device)

            # ----------------------------
            # Generate SR image
            # ----------------------------
            with torch.no_grad():
                sr_tir = self.sr_model(lr_tir)

            # ----------------------------
            # Colorization
            # ----------------------------
            prediction = self.color_model(sr_tir)

            loss = self.criterion(prediction, rgb_gt)

            self.optimizer.zero_grad()

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

        print("\nStarting Colorization Training...\n")

        for epoch in range(epochs):

            print("=" * 60)
            print(f"Epoch {epoch+1}/{epochs}")

            epoch_loss = self.train_one_epoch()

            print(f"Average Loss : {epoch_loss:.6f}\n")

            torch.save(
                self.color_model.state_dict(),
                os.path.join(
                    self.checkpoint_dir,
                    "last_color_model.pth",
                ),
            )

            if epoch_loss < self.best_loss:

                self.best_loss = epoch_loss

                torch.save(
                    self.color_model.state_dict(),
                    os.path.join(
                        self.checkpoint_dir,
                        "best_color_model.pth",
                    ),
                )

                print("✅ Best Colorization Model Saved")

        print("\nTraining Finished Successfully.")