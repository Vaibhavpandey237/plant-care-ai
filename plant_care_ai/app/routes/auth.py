"""
app/routes/auth.py — Authentication blueprint (Sign Up, Sign In, Logout).
"""

from functools import wraps
from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from werkzeug.security import generate_password_hash, check_password_hash

from database import repository
from utils.logger import get_logger

logger = get_logger(__name__)
auth_bp = Blueprint("auth", __name__)


def login_required(f):
    """Decorator to enforce login for protected routes."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            flash("Please sign in to access this page.", "warning")
            return redirect(url_for("auth.login", next=request.url))
        return f(*args, **kwargs)
    return decorated_function


@auth_bp.route("/signup", methods=["GET"])
def signup():
    """Render sign up form page."""
    if "user_id" in session:
        return redirect(url_for("diagnose.index"))
    return render_template("signup.html")


@auth_bp.route("/signup", methods=["POST"])
def signup_post():
    """Handle sign up form submission."""
    username = request.form.get("username", "").strip()
    email = request.form.get("email", "").strip().lower()
    password = request.form.get("password", "")
    confirm_password = request.form.get("confirm_password", "")

    if not username or not email or not password:
        flash("All fields are required.", "error")
        return render_template("signup.html", username=username, email=email)

    if len(username) < 3:
        flash("Username must be at least 3 characters long.", "error")
        return render_template("signup.html", username=username, email=email)

    if password != confirm_password:
        flash("Passwords do not match.", "error")
        return render_template("signup.html", username=username, email=email)

    if len(password) < 6:
        flash("Password must be at least 6 characters long.", "error")
        return render_template("signup.html", username=username, email=email)

    # Check existing user
    if repository.get_user_by_email(email):
        flash("An account with this email already exists.", "error")
        return render_template("signup.html", username=username, email=email)

    if repository.get_user_by_username(username):
        flash("Username is already taken.", "error")
        return render_template("signup.html", username=username, email=email)

    # Hash password and create user
    password_hash = generate_password_hash(password)
    try:
        user = repository.create_user(username, email, password_hash)
        session["user_id"] = user["id"]
        session["username"] = user["username"]
        flash(f"Welcome to PlantCareAI, {username}! Account created successfully.", "success")
        return redirect(url_for("diagnose.index"))
    except Exception as exc:
        logger.error("Sign up error: %s", exc)
        flash("Failed to create account. Please try again.", "error")
        return render_template("signup.html", username=username, email=email)


@auth_bp.route("/login", methods=["GET"])
def login():
    """Render login form page."""
    if "user_id" in session:
        return redirect(url_for("diagnose.index"))
    return render_template("login.html")


@auth_bp.route("/login", methods=["POST"])
def login_post():
    """Handle login form submission."""
    email_or_user = request.form.get("email_or_username", "").strip()
    password = request.form.get("password", "")

    if not email_or_user or not password:
        flash("Please enter your email/username and password.", "error")
        return render_template("login.html")

    # Find user by email or username
    user = repository.get_user_by_email(email_or_user) or repository.get_user_by_username(email_or_user)

    if not user or not check_password_hash(user["password_hash"], password):
        flash("Invalid email/username or password.", "error")
        return render_template("login.html")

    # Login successful
    session["user_id"] = user["id"]
    session["username"] = user["username"]
    flash(f"Welcome back, {user['username']}!", "success")

    next_page = request.args.get("next")
    return redirect(next_page or url_for("diagnose.index"))


@auth_bp.route("/logout", methods=["GET", "POST"])
def logout():
    """Clear session and log out."""
    session.clear()
    flash("You have been signed out.", "success")
    return redirect(url_for("diagnose.index"))
