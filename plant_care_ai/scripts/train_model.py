"""
scripts/train_model.py — Standalone runner script for model training.
"""

import argparse
import sys
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core.trainer import train
import config


def main():
    parser = argparse.ArgumentParser(description="Train Plant Care AI Model")
    parser.add_argument("--epochs", type=int, default=5, help="Phase 1 epochs")
    parser.add_argument("--epochs-phase2", type=int, default=10, help="Phase 2 epochs")
    parser.add_argument("--batch-size", type=int, default=32, help="Batch size")
    parser.add_argument("--subset", type=float, default=1.0, help="Subset fraction (e.g. 0.2)")
    parser.add_argument("--data-dir", help="Custom dataset path")
    args = parser.parse_args()

    data_path = Path(args.data_dir) if args.data_dir else config.DATASET_DIR

    train(
        dataset_dir=data_path,
        epochs_phase1=args.epochs,
        epochs_phase2=args.epochs_phase2,
        batch_size=args.batch_size,
        subset_fraction=args.subset,
    )


if __name__ == "__main__":
    main()
