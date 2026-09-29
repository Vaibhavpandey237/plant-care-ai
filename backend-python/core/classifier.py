"""
core/classifier.py — High-level classify/diagnose API combining preprocessing,
model inference, health assessment, and care recommendations.
"""

from pathlib import Path
from typing import Any, Dict, List, Optional, Union

import config
from core import model as model_module
from core.preprocess import preprocess_image
from core.health import assess_health
from core.care_recommender import get_recommendation
from core.species import extract_species_from_label, get_species_info
from utils.logger import get_logger

logger = get_logger(__name__)


def diagnose_image(
    source: Union[str, Path, bytes],
    top_k: int = None,
    confidence_threshold: float = None,
) -> Dict[str, Any]:
    """
    Full diagnosis pipeline: preprocess → infer → health → recommendations.

    Args:
        source: Image file path (str/Path) or raw bytes.
        top_k: Number of top predictions to return.
        confidence_threshold: Minimum confidence to mark result as certain.

    Returns:
        Complete diagnosis dict with keys:
            top_prediction, top_confidence, predictions, health_score,
            severity, uncertain, recommendations, species_info.

    Raises:
        RuntimeError: If model is not loaded.
        ValueError: If image cannot be processed.
    """
    k = top_k or config.TOP_K_PREDICTIONS
    thresh = confidence_threshold if confidence_threshold is not None else config.CONFIDENCE_THRESHOLD

    logger.info("Starting diagnosis — top_k=%d, threshold=%.2f", k, thresh)

    # Step 1: Preprocess
    try:
        image_array = preprocess_image(source)
    except ValueError as exc:
        raise ValueError(f"Image preprocessing failed: {exc}") from exc

    # Step 2: Infer
    predictions = model_module.predict(image_array, top_k=k)
    logger.info("Top prediction: %s (%.2f%%)", predictions[0]["label"],
                predictions[0]["confidence"] * 100)

    # Step 3: Health assessment
    health = assess_health(predictions, threshold=thresh)

    # Step 4: Care recommendations
    recs = get_recommendation(
        label=health["label"],
        confidence=health["confidence"],
        health_score=health["health_score"],
        severity=health["severity"],
    )

    # Step 5: Species info (if available)
    species_name = extract_species_from_label(health["label"])
    species_info = get_species_info(species_name) if species_name else None

    result: Dict[str, Any] = {
        "top_prediction": health["label"],
        "top_confidence": round(health["confidence"], 4),
        "top_confidence_pct": round(health["confidence"] * 100, 2),
        "predictions": predictions,
        "health_score": health["health_score"],
        "severity": health["severity"],
        "uncertain": health["uncertain"],
        "recommendations": recs,
        "species_info": species_info,
    }

    if health["uncertain"]:
        logger.warning(
            "Low confidence (%.2f < %.2f) — result marked as uncertain.",
            health["confidence"],
            thresh,
        )

    return result


def classify_image_quick(source: Union[str, Path, bytes]) -> Optional[str]:
    """
    Quick classification — returns only the top label or None on error.

    Useful for CLI or batch processing where full detail is not needed.

    Args:
        source: Image file path or bytes.

    Returns:
        Top label string or None if inference fails.
    """
    try:
        arr = preprocess_image(source)
        preds = model_module.predict(arr, top_k=1)
        return preds[0]["label"] if preds else None
    except Exception as exc:
        logger.error("Quick classification failed: %s", exc)
        return None


def list_supported_classes() -> List[Dict[str, Any]]:
    """
    Return all supported class labels with display metadata.

    Returns:
        List of dicts with label, is_healthy, species, severity keys.
    """
    from core.health import get_severity
    from core.care_recommender import KNOWLEDGE_BASE

    labels = model_module.get_labels()
    if not labels:
        # Fallback to knowledge base labels if model not loaded
        from core.care_recommender import list_all_labels
        labels = list_all_labels()

    results = []
    for label in labels:
        is_healthy = "healthy" in label.lower()
        species = extract_species_from_label(label)
        kb_entry = KNOWLEDGE_BASE.get(label)
        results.append({
            "label": label,
            "display_name": kb_entry["display_name"] if kb_entry else label,
            "is_healthy": is_healthy,
            "species": species,
            "severity": get_severity(label),
            "in_knowledge_base": kb_entry is not None,
        })
    return results
