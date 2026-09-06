import pytest
import numpy as np
import cv2
import importlib.util
import sys

def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod

main_root = load_module("main_root", "main.py")

def test_decode_img_invalid_bytes():
    # Pass random invalid bytes
    invalid_data = b'this is not an image'

    with pytest.raises(ValueError) as exc_info:
        main_root._decode_img(invalid_data)

    assert str(exc_info.value) == "Failed to decode image data."

def test_decode_img_valid_bytes():
    # Create a dummy image
    dummy_img = np.zeros((100, 100, 3), dtype=np.uint8)
    _, encoded = cv2.imencode('.jpg', dummy_img)
    valid_data = encoded.tobytes()

    img = main_root._decode_img(valid_data)
    assert img is not None
    assert img.shape == (100, 100, 3)
