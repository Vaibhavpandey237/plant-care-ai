"""
app/routes/history.py — Web routes for diagnosis history and dashboard.
"""

from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from database import repository
from utils.logger import get_logger

logger = get_logger(__name__)
history_bp = Blueprint("history", __name__)


@history_bp.route("/dashboard", methods=["GET"])
def dashboard():
    """Render the main dashboard with history and statistics."""
    try:
        page = int(request.args.get("page", 1))
    except ValueError:
        page = 1

    user_id = session.get("user_id")
    data = repository.list_diagnoses(page=page, per_page=15, user_id=user_id)
    stats = repository.get_stats(user_id=user_id)
    return render_template(
        "dashboard.html",
        data=data,
        diagnoses=data["diagnoses"],
        stats=stats,
        page=page,
    )


@history_bp.route("/history/delete/<int:diagnosis_id>", methods=["POST"])
def delete_diagnosis(diagnosis_id: int):
    """Delete a diagnosis and redirect to dashboard."""
    deleted = repository.delete_diagnosis(diagnosis_id)
    if deleted:
        flash(f"Diagnosis #{diagnosis_id} deleted.", "success")
    else:
        flash(f"Diagnosis #{diagnosis_id} not found.", "error")
    return redirect(url_for("history.dashboard"))
