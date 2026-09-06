import pytest
import math
from simulator import _hav

def test_hav_identity():
    """Distance between the exact same point should be 0."""
    p1 = (48.8566, 2.3522)
    assert _hav(p1, p1) == 0.0

def test_hav_symmetry():
    """Distance from A to B should equal distance from B to A."""
    p1 = (48.8566, 2.3522)
    p2 = (51.5074, -0.1278)
    assert math.isclose(_hav(p1, p2), _hav(p2, p1))

def test_hav_positivity():
    """Distance between different points must be strictly positive."""
    p1 = (48.8566, 2.3522)
    p2 = (51.5074, -0.1278)
    assert _hav(p1, p2) > 0.0

def test_hav_monotonicity():
    """Distance should increase as coordinates move further apart."""
    origin = (0.0, 0.0)
    p1 = (1.0, 1.0)
    p2 = (2.0, 2.0)

    dist1 = _hav(origin, p1)
    dist2 = _hav(origin, p2)

    assert dist2 > dist1

def test_hav_return_type():
    """Function must return a float."""
    assert isinstance(_hav((0, 0), (1, 1)), float)
