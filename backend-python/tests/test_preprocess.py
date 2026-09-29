"""
tests/test_preprocess.py — Unit tests for image preprocessing module.
"""

import io
import pytest
import numpy as np
from PIL import Image

from core.preprocess import load_image, preprocess_image, pil_to_array


def create_dummy_image_bytes(format="PNG", color=(0, 255, 0), size=(100, 100)) -> bytes:
    """Generate raw image bytes in memory for testing."""
    img = Image.new("RGB", size, color=color)
    buf = io.BytesIO()
    img.save(buf, format=format)
    return buf.getvalue()


def test_load_image_from_bytes():
    img_bytes = create_dummy_image_bytes()
    img = load_image(img_bytes)
    assert isinstance(img, Image.Image)
    assert img.mode == "RGB"


def test_load_image_invalid_bytes():
    with pytest.raises(ValueError, match="Cannot identify image file"):
        load_image(b"invalid image corrupt bytes")


def test_preprocess_image_shape_and_range():
    img_bytes = create_dummy_image_bytes(size=(300, 400))
    arr = preprocess_image(img_bytes, image_size=224)

    assert isinstance(arr, np.ndarray)
    assert arr.shape == (1, 224, 224, 3)
    assert arr.dtype == np.float32
    assert 0.0 <= arr.min() <= 1.0
    assert 0.0 <= arr.max() <= 1.0


def test_pil_to_array():
    pil_img = Image.new("RGB", (150, 150), color=(255, 0, 0))
    arr = pil_to_array(pil_img, image_size=224)

    assert arr.shape == (1, 224, 224, 3)
    # Red channel (index 0) should be ~1.0, green/blue ~0.0
    assert pytest.approx(arr[0, 0, 0, 0], 0.01) == 1.0
    assert pytest.approx(arr[0, 0, 0, 1], 0.01) == 0.0
