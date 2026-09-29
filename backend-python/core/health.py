"""
core/health.py — Plant health scoring and severity classification.

Maps model predictions to a 0–100 health score and a severity level.
"""

from typing import Dict, List, Tuple

import config
from utils.logger import get_logger

logger = get_logger(__name__)

# ─── Severity Map ─────────────────────────────────────────────────────────────
# Maps class label suffix patterns to (LOW | MEDIUM | HIGH).
# Healthy classes always map to LOW severity.
SEVERITY_MAP: Dict[str, str] = {
    # Apple
    "Apple___Apple_scab": "HIGH",
    "Apple___Black_rot": "HIGH",
    "Apple___Cedar_apple_rust": "MEDIUM",
    "Apple___healthy": "LOW",
    # Tomato
    "Tomato___Late_blight": "HIGH",
    "Tomato___Early_blight": "MEDIUM",
    "Tomato___Leaf_Miner": "MEDIUM",
    "Tomato___Septoria_leaf_spot": "MEDIUM",
    "Tomato___Spider_mites Two-spotted_spider_mite": "MEDIUM",
    "Tomato___Target_Spot": "MEDIUM",
    "Tomato___Tomato_mosaic_virus": "HIGH",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": "HIGH",
    "Tomato___Bacterial_spot": "HIGH",
    "Tomato___healthy": "LOW",
    # Potato
    "Potato___Late_blight": "HIGH",
    "Potato___Early_blight": "MEDIUM",
    "Potato___healthy": "LOW",
    # Grape
    "Grape___Black_rot": "HIGH",
    "Grape___Esca_(Black_Measles)": "HIGH",
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": "MEDIUM",
    "Grape___healthy": "LOW",
    # Corn
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": "MEDIUM",
    "Corn_(maize)___Common_rust_": "MEDIUM",
    "Corn_(maize)___Northern_Leaf_Blight": "HIGH",
    "Corn_(maize)___healthy": "LOW",
    # Pepper
    "Pepper,_bell___Bacterial_spot": "HIGH",
    "Pepper,_bell___healthy": "LOW",
    # Strawberry
    "Strawberry___Leaf_scorch": "MEDIUM",
    "Strawberry___healthy": "LOW",
    # Cherry
    "Cherry_(including_sour)___Powdery_mildew": "MEDIUM",
    "Cherry_(including_sour)___healthy": "LOW",
    # Peach
    "Peach___Bacterial_spot": "HIGH",
    "Peach___healthy": "LOW",
    # Squash
    "Squash___Powdery_mildew": "MEDIUM",
    # Soybean
    "Soybean___healthy": "LOW",
    # Raspberry
    "Raspberry___healthy": "LOW",
    # Blueberry
    "Blueberry___healthy": "LOW",
    # Orange
    "Orange___Haunglongbing_(Citrus_greening)": "HIGH",
}


def get_severity(label: str) -> str:
    """
    Return the severity level for a given class label.

    Falls back to MEDIUM for unknown diseased classes,
    and LOW for anything containing 'healthy'.

    Args:
        label: Class label string.

    Returns:
        One of: "LOW", "MEDIUM", "HIGH".
    """
    if label in SEVERITY_MAP:
        return SEVERITY_MAP[label]
    if "healthy" in label.lower():
        return "LOW"
    # Unknown disease → conservative MEDIUM
    logger.warning("Unknown label '%s' — defaulting severity to MEDIUM.", label)
    return "MEDIUM"


def compute_health_score(label: str, confidence: float) -> int:
    """
    Compute a 0–100 health score from the top prediction.

    Logic:
        - Healthy classes: base score of 90 + up to 10 from confidence.
        - Diseased classes: score = round(100 * (1 - disease_confidence)).
          Clamped to [0, 79] so diseased plants never reach healthy range.

    Args:
        label: Top-predicted class label.
        confidence: Confidence of the top prediction [0.0, 1.0].

    Returns:
        Integer health score in [0, 100].
    """
    if "healthy" in label.lower():
        # 90–100 range for healthy plants
        score = int(90 + round(confidence * 10))
        return min(score, 100)
    else:
        # Inverse of disease confidence
        score = int(round(100 * (1.0 - confidence)))
        return max(0, min(score, 79))  # cap below healthy range


def assess_health(
    predictions: List[Dict],
    threshold: float = None,
) -> Dict:
    """
    Produce a full health assessment from top-k predictions.

    Args:
        predictions: List of {"label": str, "confidence": float} sorted desc.
        threshold: Minimum confidence to consider a prediction certain.

    Returns:
        Dict with keys: label, confidence, health_score, severity, uncertain.
    """
    thresh = threshold if threshold is not None else config.CONFIDENCE_THRESHOLD

    if not predictions:
        return {
            "label": "Unknown",
            "confidence": 0.0,
            "health_score": 0,
            "severity": "HIGH",
            "uncertain": True,
        }

    top = predictions[0]
    label = top["label"]
    confidence = top["confidence"]
    uncertain = confidence < thresh

    health_score = compute_health_score(label, confidence)
    severity = get_severity(label)

    return {
        "label": label,
        "confidence": confidence,
        "health_score": health_score,
        "severity": severity,
        "uncertain": uncertain,
    }
