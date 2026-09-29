"""
run_server.py — Web server entry point for Plant Care AI.

Boots the Flask application on the configured host/port.
"""

import config
from app import create_app
from utils.logger import get_logger

logger = get_logger(__name__)

app = create_app()

if __name__ == "__main__":
    host = "127.0.0.1"
    port = config.SERVER_PORT
    logger.info("Starting Plant Care AI Web Server on http://%s:%d", host, port)
    app.run(
        host=host,
        port=port,
        debug=False,
        use_reloader=False,
    )
