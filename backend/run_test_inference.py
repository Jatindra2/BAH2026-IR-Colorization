import os
import sys
from pathlib import Path

# Add backend directory to sys.path
sys.path.append(os.path.dirname(__file__))

from inference import predict_image

# Test files relative to backend directory
test_samples = [
    ("LC08/sample_013", "../baseline/output/patches/LC08/sample_013/tir_200m.npy"),
    ("LC08/sample_000", "../baseline/output/patches/LC08/sample_000/tir_200m.npy"),
    ("LC08/sample_000_100m", "../baseline/output/patches/LC08/sample_000/tir_100m_512.npy"),
    ("LC09/sample_002", "../baseline/output/patches/LC09/sample_002/tir_200m.npy"),
]

output_dir = Path(__file__).resolve().parent / "test_outputs"
output_dir.mkdir(exist_ok=True)

print("Running test inferences...")
for name, path in test_samples:
    input_path = (Path(__file__).resolve().parent / path).resolve()
    if not input_path.exists():
        print(f"Skipping {name}: file does not exist at {input_path}")
        continue
    out_path = output_dir / f"{name.replace('/', '_')}_colorized.png"
    print(f"Predicting for {name} ({input_path.name}) -> {out_path}")
    predict_image(input_path, out_path)

print("Inference completed successfully!")
