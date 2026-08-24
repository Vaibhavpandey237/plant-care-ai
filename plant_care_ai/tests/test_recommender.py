"""
tests/test_recommender.py — Unit tests for care recommendation engine.
"""

from core.care_recommender import (
    KNOWLEDGE_BASE,
    get_recommendation,
    list_all_labels,
)


def test_mandatory_labels_present():
    mandatory_labels = [
        "Apple___Apple_scab",
        "Apple___Black_rot",
        "Apple___healthy",
        "Tomato___Late_blight",
        "Tomato___Early_blight",
        "Tomato___healthy",
        "Potato___Late_blight",
        "Potato___healthy",
    ]
    for label in mandatory_labels:
        assert label in KNOWLEDGE_BASE, f"Missing mandatory label: {label}"


def test_knowledge_base_structure():
    for label, entry in KNOWLEDGE_BASE.items():
        assert "display_name" in entry, f"Missing display_name for {label}"
        assert "description" in entry, f"Missing description for {label}"
        assert "causes" in entry, f"Missing causes for {label}"
        assert "symptoms" in entry, f"Missing symptoms for {label}"
        assert "treatment" in entry, f"Missing treatment for {label}"
        assert "watering" in entry, f"Missing watering for {label}"
        assert "sunlight" in entry, f"Missing sunlight for {label}"
        assert "fertilizer" in entry, f"Missing fertilizer for {label}"
        assert "prevention" in entry, f"Missing prevention for {label}"


def test_get_recommendation_output_schema():
    rec = get_recommendation("Tomato___Late_blight", 0.95, 10, "HIGH")

    assert rec["condition"] == "Tomato___Late_blight"
    assert rec["severity"] == "HIGH"
    assert rec["health_score"] == 10
    assert rec["confidence"] == 0.95
    assert isinstance(rec["recommendations"], list)
    assert len(rec["recommendations"]) > 0

    first_item = rec["recommendations"][0]
    assert "category" in first_item
    assert "text" in first_item


def test_unknown_label_fallback():
    rec = get_recommendation("Unknown___Alien_Fungi", 0.80, 20, "MEDIUM")
    assert rec["condition"] == "Unknown___Alien_Fungi"
    assert len(rec["recommendations"]) > 0
