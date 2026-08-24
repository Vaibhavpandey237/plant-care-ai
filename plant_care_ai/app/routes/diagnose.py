"""
app/routes/diagnose.py — Web routes for the diagnosis upload and result pages.
"""

import uuid
from pathlib import Path

from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

import config
from core import model as model_module
from core.classifier import diagnose_image
from database import repository
from utils.logger import get_logger
from utils.validators import validate_image_file

logger = get_logger(__name__)
diagnose_bp = Blueprint("diagnose", __name__)


@diagnose_bp.route("/", methods=["GET"])
def index():
    """Render the homepage with the upload form."""
    model_ready = model_module.is_model_loaded()
    if not model_ready:
        model_module.load_model()
        model_ready = model_module.is_model_loaded()
    return render_template("index.html", model_ready=model_ready)


@diagnose_bp.route("/upload", methods=["POST"])
def upload():
    """Handle image upload, run diagnosis, and redirect to result page."""
    if "image" not in request.files:
        flash("No image file selected.", "error")
        return redirect(url_for("diagnose.index"))

    file = request.files["image"]
    if not file or file.filename == "":
        flash("Please select a valid image file.", "error")
        return redirect(url_for("diagnose.index"))

    file_bytes = file.read()
    is_valid, err_msg = validate_image_file(file.filename, file_bytes)
    if not is_valid:
        flash(err_msg, "error")
        return redirect(url_for("diagnose.index"))

    # Check model
    if not model_module.is_model_loaded():
        flash(
            "Model not ready. Please run: python main.py train first.",
            "warning",
        )
        return redirect(url_for("diagnose.index"))

    # Save upload
    ext = Path(file.filename).suffix.lower()
    unique_name = f"{uuid.uuid4().hex}{ext}"
    save_path = config.UPLOAD_FOLDER / unique_name
    try:
        save_path.write_bytes(file_bytes)
    except OSError as exc:
        logger.error("Failed to save upload: %s", exc)
        flash("Failed to save image. Please try again.", "error")
        return redirect(url_for("diagnose.index"))

    # Run diagnosis
    try:
        result = diagnose_image(file_bytes)
    except Exception as exc:
        logger.exception("Diagnosis error in web upload")
        flash(f"Diagnosis error: {exc}", "error")
        return redirect(url_for("diagnose.index"))

    # Persist
    try:
        user_id = session.get("user_id")
        record = repository.create_diagnosis(
            image_name=file.filename,
            image_path=str(save_path),
            top_prediction=result["top_prediction"],
            top_confidence=result["top_confidence"],
            all_predictions=result["predictions"],
            health_score=result["health_score"],
            severity=result["severity"],
            recommendations=result["recommendations"],
            user_id=user_id,
        )
        return redirect(url_for("diagnose.result", diagnosis_id=record["id"]))
    except Exception as exc:
        logger.error("DB persistence error: %s", exc)
        # Still show result even if DB fails
        return render_template("result.html", result=result["recommendations"], diagnosis_id=None)


@diagnose_bp.route("/result/<int:diagnosis_id>", methods=["GET"])
def result(diagnosis_id: int):
    """Render the result page for a specific diagnosis."""
    record = repository.get_diagnosis_by_id(diagnosis_id)
    if record is None:
        flash(f"Diagnosis {diagnosis_id} not found.", "error")
        return redirect(url_for("diagnose.index"))
    return render_template("result.html", result=record["recommendations"],
                           diagnosis_id=diagnosis_id,
                           record=record)
