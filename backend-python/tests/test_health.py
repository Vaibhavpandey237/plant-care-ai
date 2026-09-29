"""
tests/test_health.py — Unit tests for plant health scoring logic.
"""

from core.health import (
    compute_health_score,
    get_severity,
    assess_health,
)


def test_healthy_class_scoring():
    # Healthy classes map to 90–100 range
    score_high = compute_health_score("Tomato___healthy", 0.95)
    score_low = compute_health_score("Apple___healthy", 0.50)

    assert 90 <= score_high <= 100
    assert 90 <= score_low <= 100
    assert score_high >= score_low


def test_diseased_class_scoring():
    # Diseased class score = round(100 * (1 - disease_confidence))
    # 0.90 confidence → 10 health score
    score1 = compute_health_score("Tomato___Late_blight", 0.90)
    assert score1 == 10

    # 0.60 confidence → 40 health score
    score2 = compute_health_score("Apple___Apple_scab", 0.60)
    assert score2 == 40


def test_severity_mapping():
    assert get_severity("Tomato___healthy") == "LOW"
    assert get_severity("Apple___healthy") == "LOW"
    assert get_severity("Tomato___Late_blight") == "HIGH"
    assert get_severity("Apple___Apple_scab") == "HIGH"
    assert get_severity("Tomato___Early_blight") == "MEDIUM"
    assert get_severity("Unknown___Disease") == "MEDIUM"  # fallback


def test_assess_health_uncertainty():
    preds = [{"label": "Apple___Apple_scab", "confidence": 0.40}]
    assessment = assess_health(preds, threshold=0.50)

    assert assessment["uncertain"] is True
    assert assessment["severity"] == "HIGH"

    preds_certain = [{"label": "Tomato___healthy", "confidence": 0.92}]
    assessment_certain = assess_health(preds_certain, threshold=0.50)
    assert assessment_certain["uncertain"] is False
