"""
app/routes/pages.py — Web routes for About Us and Contact Us pages.
"""

from flask import Blueprint, flash, redirect, render_template, request, url_for
from database import repository
from utils.logger import get_logger

logger = get_logger(__name__)
pages_bp = Blueprint("pages", __name__)


@pages_bp.route("/about", methods=["GET"])
def about():
    """Render the About Us page."""
    return render_template("about.html")


@pages_bp.route("/contact", methods=["GET"])
def contact():
    """Render the Contact Us page."""
    return render_template("contact.html")


@pages_bp.route("/contact", methods=["POST"])
def contact_post():
    """Handle Contact Us form submission."""
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    subject = request.form.get("subject", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not subject or not message:
        flash("Please fill out all required fields.", "error")
        return render_template("contact.html", name=name, email=email, subject=subject, message=message)

    try:
        repository.create_contact_message(name, email, subject, message)
        flash("Thank you for reaching out! Your message has been sent successfully. Our team will get back to you shortly.", "success")
        return redirect(url_for("pages.contact"))
    except Exception as exc:
        logger.error("Contact message error: %s", exc)
        flash("Failed to submit message. Please try again.", "error")
        return render_template("contact.html", name=name, email=email, subject=subject, message=message)
