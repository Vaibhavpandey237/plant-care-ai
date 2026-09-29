"""
core/preprocess.py — Image loading, resizing, normalization, and augmentation helpers.
"""

import io
from pathlib import Path
from typing import Union

import numpy as np
from PIL import Image, UnidentifiedImageError

import config
from utils.logger import get_logger

logger = get_logger(__name__)


def load_image(source: Union[str, Path, bytes]) -> Image.Image:
    """
    Load an image from a file path or raw bytes.

    Args:
        source: File path (str/Path) or raw image bytes.

    Returns:
        PIL Image in RGB mode.

    Raises:
        ValueError: If the source cannot be interpreted as an image.
    """
    try:
        if isinstance(source, (str, Path)):
            img = Image.open(str(source))
        elif isinstance(source, (bytes, bytearray)):
            img = Image.open(io.BytesIO(source))
        else:
            raise ValueError(f"Unsupported source type: {type(source)}")
        return img.convert("RGB")
    except UnidentifiedImageError as exc:
        raise ValueError(f"Cannot identify image file: {exc}") from exc
    except Exception as exc:
        raise ValueError(f"Failed to load image: {exc}") from exc


def preprocess_image(
    source: Union[str, Path, bytes, Image.Image],
    image_size: int = None,
) -> np.ndarray:
    """
    Preprocess an image for model inference.

    Steps:
        1. Load and convert to RGB (if not already a PIL Image).
        2. Resize to (image_size, image_size).
        3. Normalize pixel values to [0, 1].
        4. Add batch dimension → shape (1, H, W, 3).

    Args:
        source: File path, bytes, or PIL Image.
        image_size: Target size (defaults to config.IMAGE_SIZE).

    Returns:
        Numpy array of shape (1, image_size, image_size, 3) dtype float32.
    """
    size = image_size or config.IMAGE_SIZE

    if isinstance(source, Image.Image):
        img = source.convert("RGB")
    else:
        img = load_image(source)

    img = img.resize((size, size), Image.BILINEAR)
    arr = np.array(img, dtype=np.float32) / 255.0  # normalize to [0, 1]
    arr = np.expand_dims(arr, axis=0)  # (1, H, W, 3)

    logger.debug("Preprocessed image → shape %s, range [%.3f, %.3f]",
                 arr.shape, arr.min(), arr.max())
    return arr


def pil_to_array(img: Image.Image, image_size: int = None) -> np.ndarray:
    """
    Convert a PIL Image directly to a preprocessed numpy array.

    Args:
        img: PIL Image (will be converted to RGB).
        image_size: Target size (defaults to config.IMAGE_SIZE).

    Returns:
        Numpy array of shape (1, image_size, image_size, 3) dtype float32.
    """
    return preprocess_image(img, image_size=image_size)
