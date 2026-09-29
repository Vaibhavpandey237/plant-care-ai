"""
scripts/download_dataset.py — Dataset downloader and helper instructions for PlantVillage.
"""

import sys
from pathlib import Path
from utils.logger import get_logger
import config

logger = get_logger(__name__)

PLANTVILLAGE_KAGGLE_URL = "https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset"


def download_plant_village(auto_download: bool = False) -> bool:
    """
    Check for dataset or attempt download.

    Args:
        auto_download: If True, tries downloading via kagglehub / opendatasets.

    Returns:
        True if dataset is present, False otherwise.
    """
    raw_dir = config.DATASET_DIR
    raw_dir.mkdir(parents=True, exist_ok=True)

    # Check if already downloaded
    subdirs = [d for d in raw_dir.iterdir() if d.is_dir()]
    if subdirs:
        logger.info("Found dataset at '%s' with %d folders.", raw_dir, len(subdirs))
        return True

    print("\n" + "=" * 70)
    print("📦 PLANTVILLAGE DATASET INSTRUCTIONS")
    print("=" * 70)
    print(f"Dataset target path: {raw_dir.resolve()}")
    print("\nOption 1: Manual Download (Recommended)")
    print(f"  1. Go to: {PLANTVILLAGE_KAGGLE_URL}")
    print("  2. Download PlantVillage-dataset.zip")
    print(f"  3. Extract contents so class folders (e.g., Apple___Apple_scab)")
    print(f"     are located in: {raw_dir.resolve()}")

    print("\nOption 2: Kaggle CLI")
    print("  kaggle datasets download -d abdallahalidev/plantvillage-dataset")
    print(f"  unzip plantvillage-dataset.zip -d {raw_dir.resolve()}")

    if auto_download:
        print("\nAttempting auto-download via kagglehub...")
        try:
            import kagglehub
            path = kagglehub.dataset_download("abdallahalidev/plantvillage-dataset")
            print(f"Downloaded to: {path}")
            print(f"Please move/copy dataset folders to: {raw_dir.resolve()}")
            return True
        except Exception as exc:
            print(f"Auto-download failed: {exc}")
            print("Please follow manual download instructions above.")

    print("=" * 70 + "\n")
    return False


if __name__ == "__main__":
    auto = "--auto-download" in sys.argv
    download_plant_village(auto_download=auto)
