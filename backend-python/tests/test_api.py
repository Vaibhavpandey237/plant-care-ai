"""
tests/test_api.py — Integration tests for Flask REST API endpoints.
"""

import io
import json
import pytest
from PIL import Image

from app import create_app
from database import repository


@pytest.fixture
def client():
    """Create Flask test client."""
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def create_dummy_png_bytes() -> bytes:
    """Generate in-memory tiny PNG bytes for testing."""
    img = Image.new("RGB", (50, 50), color=(34, 139, 34))
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()


def test_api_health_check(client):
    res = client.get("/api/health")
    assert res.status_code == 200
    data = res.get_json()
    assert data["success"] is True
    assert data["data"]["status"] == "ok"


def test_api_classes_endpoint(client):
    res = client.get("/api/classes")
    assert res.status_code == 200
    data = res.get_json()
    assert data["success"] is True
    assert "classes" in data["data"]
    assert len(data["data"]["classes"]) > 0


def test_api_recommendations_endpoint(client):
    res = client.get("/api/recommendations/Tomato___Late_blight")
    assert res.status_code == 200
    data = res.get_json()
    assert data["success"] is True
    assert data["data"]["condition"] == "Tomato___Late_blight"
    assert data["data"]["severity"] == "HIGH"


def test_api_recommendations_not_found(client):
    res = client.get("/api/recommendations/NonExistentClass123")
    assert res.status_code == 404
    data = res.get_json()
    assert data["success"] is False


def test_api_history_endpoint(client):
    res = client.get("/api/history?page=1&per_page=5")
    assert res.status_code == 200
    data = res.get_json()
    assert data["success"] is True
    assert "items" in data["data"]


def test_api_diagnose_bad_file_type(client):
    data = {"image": (io.BytesIO(b"hello world"), "test.txt")}
    res = client.post("/api/diagnose", data=data, content_type="multipart/form-data")
    assert res.status_code == 400
    json_data = res.get_json()
    assert json_data["success"] is False
    assert "Unsupported file type" in json_data["error"]


def test_api_diagnose_missing_file_field(client):
    res = client.post("/api/diagnose", data={})
    assert res.status_code == 400
    json_data = res.get_json()
    assert json_data["success"] is False


def test_web_routes_status_ok(client):
    """Test that all Jinja2 HTML pages render cleanly."""
    for path in ["/", "/dashboard", "/plants", "/result/1"]:
        res = client.get(path)
        assert res.status_code == 200

