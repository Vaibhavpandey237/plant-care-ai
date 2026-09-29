"""
database/db.py — SQLite connection management and schema initialization.
"""

import sqlite3
import json
from datetime import datetime, timezone
from typing import Any
from utils.logger import get_logger
import config

logger = get_logger(__name__)

# ─── Schema ───────────────────────────────────────────────────────────────────
CREATE_USERS_TABLE = """
CREATE TABLE IF NOT EXISTS users (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    username      TEXT    NOT NULL UNIQUE,
    email         TEXT    NOT NULL UNIQUE,
    password_hash TEXT    NOT NULL,
    created_at    TEXT    NOT NULL
);
"""

CREATE_CONTACT_MESSAGES_TABLE = """
CREATE TABLE IF NOT EXISTS contact_messages (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    name       TEXT    NOT NULL,
    email      TEXT    NOT NULL,
    subject    TEXT    NOT NULL,
    message    TEXT    NOT NULL,
    created_at TEXT    NOT NULL
);
"""

CREATE_DIAGNOSES_TABLE = """
CREATE TABLE IF NOT EXISTS diagnoses (
    id               INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id          INTEGER,           -- Foreign key to users.id (nullable for guest uploads)
    image_name       TEXT    NOT NULL,
    image_path       TEXT    NOT NULL,
    top_prediction   TEXT    NOT NULL,
    top_confidence   REAL    NOT NULL,
    all_predictions  TEXT    NOT NULL,  -- JSON array
    health_score     INTEGER NOT NULL,
    severity         TEXT    NOT NULL,
    recommendations  TEXT    NOT NULL,  -- JSON object
    created_at       TEXT    NOT NULL,  -- ISO 8601
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
"""

SEED_DIAGNOSES = [
    {
        "image_name": "demo_apple_scab.jpg",
        "image_path": "demo/demo_apple_scab.jpg",
        "top_prediction": "Apple___Apple_scab",
        "top_confidence": 0.87,
        "all_predictions": json.dumps([
            {"label": "Apple___Apple_scab", "confidence": 0.87},
            {"label": "Apple___Black_rot", "confidence": 0.08},
            {"label": "Apple___healthy", "confidence": 0.03},
            {"label": "Apple___Cedar_apple_rust", "confidence": 0.01},
            {"label": "Tomato___healthy", "confidence": 0.01},
        ]),
        "health_score": 13,
        "severity": "HIGH",
        "recommendations": json.dumps({
            "condition": "Apple___Apple_scab",
            "severity": "HIGH",
            "health_score": 13,
            "confidence": 0.87,
            "recommendations": [
                {"category": "Treatment", "text": "Apply fungicide containing captan or myclobutanil."},
                {"category": "Cultural Control", "text": "Remove and destroy fallen leaves to reduce inoculum."},
            ],
        }),
        "created_at": "2026-01-15T10:30:00+00:00",
    },
    {
        "image_name": "demo_tomato_healthy.jpg",
        "image_path": "demo/demo_tomato_healthy.jpg",
        "top_prediction": "Tomato___healthy",
        "top_confidence": 0.94,
        "all_predictions": json.dumps([
            {"label": "Tomato___healthy", "confidence": 0.94},
            {"label": "Tomato___Early_blight", "confidence": 0.04},
            {"label": "Tomato___Late_blight", "confidence": 0.01},
            {"label": "Potato___healthy", "confidence": 0.006},
            {"label": "Apple___healthy", "confidence": 0.004},
        ]),
        "health_score": 94,
        "severity": "LOW",
        "recommendations": json.dumps({
            "condition": "Tomato___healthy",
            "severity": "LOW",
            "health_score": 94,
            "confidence": 0.94,
            "recommendations": [
                {"category": "Watering", "text": "Water deeply 2–3 times per week at the base."},
                {"category": "Sunlight", "text": "Ensure 6–8 hours of full sun daily."},
            ],
        }),
        "created_at": "2026-01-16T14:20:00+00:00",
    },
]


def get_connection() -> sqlite3.Connection:
    """
    Return a SQLite connection with row_factory set for dict-like access.

    Returns:
        sqlite3.Connection with Row factory.
    """
    conn = sqlite3.connect(config.DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL;")
    return conn


def init_db() -> None:
    """
    Create database tables if they don't exist and seed demo data.

    This function is idempotent — safe to call multiple times.
    """
    logger.info("Initializing database at: %s", config.DB_PATH)
    conn = get_connection()
    try:
        with conn:
            conn.execute(CREATE_USERS_TABLE)
            conn.execute(CREATE_CONTACT_MESSAGES_TABLE)
            conn.execute(CREATE_DIAGNOSES_TABLE)

            # Check if user_id column exists in diagnoses table (migration check)
            cursor = conn.execute("PRAGMA table_info(diagnoses);")
            columns = [column[1] for column in cursor.fetchall()]
            if "user_id" not in columns:
                logger.info("Migrating diagnoses table: adding user_id column")
                conn.execute("ALTER TABLE diagnoses ADD COLUMN user_id INTEGER;")

            logger.info("Database tables ensured.")

            # Seed only if table is empty
            count = conn.execute("SELECT COUNT(*) FROM diagnoses").fetchone()[0]
            if count == 0:
                logger.info("Seeding %d demo diagnoses.", len(SEED_DIAGNOSES))
                for row in SEED_DIAGNOSES:
                    conn.execute(
                        """
                        INSERT INTO diagnoses
                            (image_name, image_path, top_prediction, top_confidence,
                             all_predictions, health_score, severity, recommendations, created_at)
                        VALUES
                            (:image_name, :image_path, :top_prediction, :top_confidence,
                             :all_predictions, :health_score, :severity, :recommendations, :created_at)
                        """,
                        row,
                    )
                logger.info("Seed complete.")
    finally:
        conn.close()
    logger.info("Database initialization complete.")
