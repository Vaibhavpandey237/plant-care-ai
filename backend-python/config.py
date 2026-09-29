"""
config.py — Centralized configuration for Plant Care AI.

All values can be overridden via environment variables or a .env file.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env if present
load_dotenv()

# ─── Paths ────────────────────────────────────────────────────────────────────
BASE_DIR: Path = Path(__file__).resolve().parent
DATA_DIR: Path = BASE_DIR / "data"
MODELS_DIR: Path = DATA_DIR / "models"
UPLOAD_FOLDER: Path = BASE_DIR / Path(os.getenv("UPLOAD_FOLDER", "data/uploads"))

# ─── Model ────────────────────────────────────────────────────────────────────
MODEL_PATH: Path = BASE_DIR / Path(os.getenv("MODEL_PATH", "data/models/plant_model.h5"))
LABELS_PATH: Path = BASE_DIR / Path(os.getenv("LABELS_PATH", "data/models/labels.json"))
IMAGE_SIZE: int = int(os.getenv("IMAGE_SIZE", "224"))
CONFIDENCE_THRESHOLD: float = float(os.getenv("CONFIDENCE_THRESHOLD", "0.5"))
TOP_K_PREDICTIONS: int = int(os.getenv("TOP_K_PREDICTIONS", "5"))

# ─── Upload Validation ─────────────────────────────────────────────────────────
MAX_UPLOAD_MB: int = int(os.getenv("MAX_UPLOAD_MB", "10"))
MAX_UPLOAD_BYTES: int = MAX_UPLOAD_MB * 1024 * 1024
ALLOWED_EXTENSIONS: set = {"png", "jpg", "jpeg", "webp", "bmp"}

# ─── Database ─────────────────────────────────────────────────────────────────
DB_PATH: str = os.getenv("DB_PATH", str(BASE_DIR / "plant_care.db"))

# ─── Server ───────────────────────────────────────────────────────────────────
SERVER_HOST: str = os.getenv("SERVER_HOST", "0.0.0.0")
SERVER_PORT: int = int(os.getenv("SERVER_PORT", "5000"))
DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
SECRET_KEY: str = os.getenv("SECRET_KEY", "plant-care-ai-secret-key-change-in-prod")

# ─── Logging ──────────────────────────────────────────────────────────────────
LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE: str = os.getenv("LOG_FILE", str(BASE_DIR / "logs" / "plant_care.log"))

# ─── Training ─────────────────────────────────────────────────────────────────
DATASET_DIR: Path = DATA_DIR / "raw"
TRAIN_EPOCHS_PHASE1: int = 5
TRAIN_EPOCHS_PHASE2: int = 10
BATCH_SIZE: int = 32
LEARNING_RATE: float = 0.001
FINE_TUNE_LR: float = 1e-5

# ─── Ensure critical directories exist ────────────────────────────────────────
for _dir in [DATA_DIR, MODELS_DIR, UPLOAD_FOLDER, BASE_DIR / "logs"]:
    _dir.mkdir(parents=True, exist_ok=True)
