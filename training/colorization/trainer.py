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

        # Precompute and cache SR model predictions to accelerate CPU training
        self.sr_cache = {}
        print("Precomputing Super-Resolution predictions to accelerate training...")
        with torch.no_grad():
            for i in range(len(self.dataloader.dataset)):
                batch_item = self.dataloader.dataset[i]
                lr_tir = batch_item["lr_tir"].unsqueeze(0).to(self.device)
                sr_tir = self.sr_model(lr_tir).squeeze(0).cpu() # Cache on CPU/RAM
                self.sr_cache[batch_item["idx"]] = sr_tir
        print("Precomputation finished successfully.")

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

            idxs = batch["idx"]
            ab_gt = batch["ab"].to(self.device)

            # Retrieve precomputed SR images from cache and load to device
            sr_tirs = [self.sr_cache[int(idx)].to(self.device) for idx in idxs]
            sr_tir = torch.stack(sr_tirs, dim=0)

            # ----------------------------
            # Colorization
            # ----------------------------
            prediction = self.color_model(sr_tir)

            loss = self.criterion(prediction, ab_gt)

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

                print("[SUCCESS] Best Colorization Model Saved")

        print("\nTraining Finished Successfully.")