import numpy as np
import pytest
from ai_bridge import _noise_road

def test_noise_road_default_shape_and_type():
    """Verify default image has the correct shape and data type."""
    img = _noise_road()
    assert isinstance(img, np.ndarray), "Output should be a numpy array"
    assert img.shape == (480, 640, 3), "Default shape should be (480, 640, 3)"
    assert img.dtype == np.uint8, "Data type should be uint8"

def test_noise_road_custom_shape():
    """Verify custom h and w parameters correctly adjust output dimensions."""
    custom_h = 240
    custom_w = 320
    img = _noise_road(h=custom_h, w=custom_w)
    assert isinstance(img, np.ndarray), "Output should be a numpy array"
    assert img.shape == (custom_h, custom_w, 3), f"Shape should be ({custom_h}, {custom_w}, 3)"
    assert img.dtype == np.uint8, "Data type should be uint8"

def test_noise_road_value_range():
    """Verify pixel values are within the valid 8-bit range [0, 255]."""
    img = _noise_road()
    assert np.min(img) >= 0, "Minimum pixel value should not be less than 0"
    assert np.max(img) <= 255, "Maximum pixel value should not exceed 255"

def test_noise_road_custom_base():
    """Verify setting a custom base value works without errors."""
    img = _noise_road(base=150)
    assert img.shape == (480, 640, 3)
    assert img.dtype == np.uint8
    assert np.min(img) >= 0
    assert np.max(img) <= 255
