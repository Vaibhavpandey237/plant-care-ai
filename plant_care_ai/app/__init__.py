"""
app/__init__.py — Flask application factory.
"""

from pathlib import Path
from flask import Flask

import config
from database.db import init_db
from utils.logger import get_logger

logger = get_logger(__name__)


def create_app() -> Flask:
    """
    Create and configure the Flask application.

    Returns:
        Configured Flask app instance.
    """
    app = Flask(
        __name__,
        template_folder=str(Path(__file__).parent / "templates"),
        static_folder=str(Path(__file__).parent / "static"),
    )

    app.config["SECRET_KEY"] = config.SECRET_KEY
    app.config["MAX_CONTENT_LENGTH"] = config.MAX_UPLOAD_BYTES
    app.config["UPLOAD_FOLDER"] = str(config.UPLOAD_FOLDER)

    # Ensure upload directory exists
    config.UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)

    # Initialize database (idempotent)
    init_db()

    # Register blueprints
    from app.routes.diagnose import diagnose_bp
    from app.routes.plants import plants_bp
    from app.routes.history import history_bp
    from app.routes.auth import auth_bp
    from app.routes.pages import pages_bp
    from app.api import api_bp

    app.register_blueprint(api_bp, url_prefix="/api")
    app.register_blueprint(diagnose_bp)
    app.register_blueprint(plants_bp)
    app.register_blueprint(history_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(pages_bp)

    # Inject current_user in all templates
    @app.context_processor
    def inject_user():
        from flask import session
        from database.repository import get_user_by_id
        user_id = session.get("user_id")
        user = get_user_by_id(user_id) if user_id else None
        return dict(current_user=user)

    # Register error handlers
    _register_error_handlers(app)

    logger.info("Flask app created and configured.")
    return app


def _register_error_handlers(app: Flask) -> None:
    """Register JSON-aware error handlers."""
    from flask import jsonify, render_template

    @app.errorhandler(400)
    def bad_request(e):
        return jsonify({"success": False, "data": None, "error": str(e)}), 400

    @app.errorhandler(404)
    def not_found(e):
        return jsonify({"success": False, "data": None, "error": "Resource not found."}), 404

    @app.errorhandler(413)
    def too_large(e):
        return jsonify({
            "success": False,
            "data": None,
            "error": f"File too large. Maximum size is {config.MAX_UPLOAD_MB} MB.",
        }), 413

    @app.errorhandler(500)
    def server_error(e):
        logger.error("Internal server error: %s", e)
        return jsonify({"success": False, "data": None, "error": "Internal server error."}), 500
