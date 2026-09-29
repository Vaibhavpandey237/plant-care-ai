"""
utils/validators.py — Input validation helpers for file uploads and API requests.
"""

import io
from pathlib import Path
from typing import Tuple, Optional
from PIL import Image
import config
from utils.logger import get_logger

logger = get_logger(__name__)


def validate_image_file(
    filename: str, file_bytes: bytes
) -> Tuple[bool, Optional[str]]:
    """
    Validate an uploaded image file by extension, size, and MIME content.

    Args:
        filename: Original filename from the upload.
        file_bytes: Raw bytes of the uploaded file.

    Returns:
        (is_valid, error_message) — error_message is None when valid.
    """
    # Check extension
    if not filename:
        return False, "No filename provided."

    ext = Path(filename).suffix.lstrip(".").lower()
    if ext not in config.ALLOWED_EXTENSIONS:
        allowed = ", ".join(sorted(config.ALLOWED_EXTENSIONS))
        return False, f"Unsupported file type '.{ext}'. Allowed: {allowed}."

    # Check file size
    size_bytes = len(file_bytes)
    if size_bytes == 0:
        return False, "File is empty."
    if size_bytes > config.MAX_UPLOAD_BYTES:
        mb = size_bytes / (1024 * 1024)
        return False, f"File too large ({mb:.1f} MB). Maximum is {config.MAX_UPLOAD_MB} MB."

    # Verify actual image content (catches renamed non-image files)
    try:
        img = Image.open(io.BytesIO(file_bytes))
        img.verify()  # raises if not a valid image
    except Exception as exc:
        logger.warning("Image verification failed for '%s': %s", filename, exc)
        return False, "File does not appear to be a valid image."

    return True, None


def validate_class_name(class_name: str) -> Tuple[bool, Optional[str]]:
    """
    Validate that a class name string is a non-empty, safe identifier.

    Args:
        class_name: The class name to validate.

    Returns:
        (is_valid, error_message)
    """
    if not class_name or not isinstance(class_name, str):
        return False, "Class name must be a non-empty string."
    if len(class_name) > 200:
        return False, "Class name is too long."
    return True, None


def validate_pagination(page: int, per_page: int) -> Tuple[bool, Optional[str]]:
    """
    Validate pagination parameters.

    Args:
        page: Page number (1-indexed).
        per_page: Items per page.

    Returns:
        (is_valid, error_message)
    """
    if page < 1:
        return False, "Page number must be >= 1."
    if not (1 <= per_page <= 200):
        return False, "per_page must be between 1 and 200."
    return True, None
