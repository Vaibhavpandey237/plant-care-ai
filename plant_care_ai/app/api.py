"""
app/api.py — REST API blueprint with all /api/* endpoints.
"""

import os
import uuid
from pathlib import Path

from flask import Blueprint, jsonify, request

import config
from core import model as model_module
from core.classifier import diagnose_image, list_supported_classes
from core.care_recommender import get_recommendation, KNOWLEDGE_BASE
from core.health import get_severity
from database import repository
from utils.logger import get_logger
from utils.validators import validate_image_file, validate_class_name, validate_pagination

logger = get_logger(__name__)

api_bp = Blueprint("api", __name__)


def _ok(data, status: int = 200):
    """Return a success JSON envelope."""
    return jsonify({"success": True, "data": data, "error": None}), status


def _err(message: str, status: int = 400):
    """Return an error JSON envelope."""
    return jsonify({"success": False, "data": None, "error": message}), status


# ─── Health Check ─────────────────────────────────────────────────────────────

@api_bp.get("/health")
def api_health():
    """Service health check endpoint."""
    return _ok({
        "status": "ok",
        "model_loaded": model_module.is_model_loaded(),
        "model_path": str(config.MODEL_PATH),
        "db_path": config.DB_PATH,
        "version": "1.0.0",
    })


# ─── Diagnose ─────────────────────────────────────────────────────────────────

@api_bp.post("/diagnose")
def api_diagnose():
    """
    Upload a plant leaf image and receive a full diagnosis.

    Multipart form-data:
        image: The image file (JPEG, PNG, etc.)

    Returns:
        Diagnosis JSON with predictions, health score, and care recommendations.
    """
    if "image" not in request.files:
        return _err("No image file provided. Use field name 'image'.", 400)

    file = request.files["image"]
    if file.filename == "":
        return _err("Empty filename — please select a file.", 400)

    file_bytes = file.read()
    is_valid, err_msg = validate_image_file(file.filename, file_bytes)
    if not is_valid:
        return _err(err_msg, 400)

    if not model_module.is_model_loaded():
        model_module.load_model()
        if not model_module.is_model_loaded():
            return _err(
                "Model not found. Run: python main.py train",
                status=503,
            )

    # Save uploaded file
    ext = Path(file.filename).suffix.lower()
    unique_name = f"{uuid.uuid4().hex}{ext}"
    save_path = config.UPLOAD_FOLDER / unique_name
    try:
        save_path.write_bytes(file_bytes)
    except OSError as exc:
        logger.error("Failed to save upload: %s", exc)
        return _err("Failed to save uploaded file.", 500)

    # Run diagnosis
    try:
        result = diagnose_image(file_bytes)
    except RuntimeError as exc:
        return _err(str(exc), 503)
    except ValueError as exc:
        return _err(str(exc), 400)
    except Exception as exc:
        logger.exception("Unexpected diagnosis error")
        return _err(f"Diagnosis failed: {exc}", 500)

    # Persist to database
    try:
        record = repository.create_diagnosis(
            image_name=file.filename,
            image_path=str(save_path),
            top_prediction=result["top_prediction"],
            top_confidence=result["top_confidence"],
            all_predictions=result["predictions"],
            health_score=result["health_score"],
            severity=result["severity"],
            recommendations=result["recommendations"],
        )
        result["diagnosis_id"] = record["id"]
    except Exception as exc:
        logger.error("Failed to save diagnosis to DB: %s", exc)
        # Non-fatal — still return result
        result["diagnosis_id"] = None

    logger.info(
        "Diagnosis complete: %s (%.1f%%) — Health: %d/100",
        result["top_prediction"],
        result["top_confidence"] * 100,
        result["health_score"],
    )
    return _ok(result, 200)


# ─── History ──────────────────────────────────────────────────────────────────

@api_bp.get("/history")
def api_history():
    """List past diagnoses with pagination."""
    try:
        page = int(request.args.get("page", 1))
        per_page = int(request.args.get("per_page", 20))
    except ValueError:
        return _err("page and per_page must be integers.", 400)

    valid, err_msg = validate_pagination(page, per_page)
    if not valid:
        return _err(err_msg, 400)

    data = repository.list_diagnoses(page=page, per_page=per_page)
    return _ok(data)


@api_bp.get("/history/<int:diagnosis_id>")
def api_history_detail(diagnosis_id: int):
    """Fetch a single diagnosis by ID."""
    record = repository.get_diagnosis_by_id(diagnosis_id)
    if record is None:
        return _err(f"Diagnosis {diagnosis_id} not found.", 404)
    return _ok(record)


@api_bp.delete("/history/<int:diagnosis_id>")
def api_history_delete(diagnosis_id: int):
    """Delete a diagnosis record."""
    deleted = repository.delete_diagnosis(diagnosis_id)
    if not deleted:
        return _err(f"Diagnosis {diagnosis_id} not found.", 404)
    return _ok({"deleted_id": diagnosis_id, "message": "Diagnosis deleted."})


# ─── Classes ──────────────────────────────────────────────────────────────────

@api_bp.get("/classes")
def api_classes():
    """List all supported plant/disease classes."""
    classes = list_supported_classes()
    return _ok({"classes": classes, "total": len(classes)})


@api_bp.get("/recommendations/<string:class_name>")
def api_recommendations(class_name: str):
    """Get care/treatment information for a specific class."""
    valid, err_msg = validate_class_name(class_name)
    if not valid:
        return _err(err_msg, 400)

    if class_name not in KNOWLEDGE_BASE:
        # Try case-insensitive match
        match = next(
            (k for k in KNOWLEDGE_BASE if k.lower() == class_name.lower()), None
        )
        if match:
            class_name = match
        else:
            return _err(f"Class '{class_name}' not found in knowledge base.", 404)

    severity = get_severity(class_name)
    is_healthy = "healthy" in class_name.lower()
    health_score = 95 if is_healthy else 30
    recs = get_recommendation(class_name, 0.9, health_score, severity)
    return _ok(recs)
