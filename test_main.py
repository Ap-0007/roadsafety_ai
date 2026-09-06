import pytest
from main import _default_priority

# Note: The issue description contains an outdated version of _default_priority
# returning 'high'/'low', but the actual implementation in main.py returns
# priority strings 'p1'-'p4'. These tests correctly target the actual implementation.
@pytest.mark.parametrize(
    "etype, severity, expected",
    [
        ("accident", "critical", "p1"),
        ("accident", "high", "p1"),
        ("accident", "medium", "p2"),
        ("accident", "low", "p4"),
        ("fallen_tree", "critical", "p1"),
        ("fallen_tree", "high", "p1"),
        ("fallen_tree", "medium", "p3"),
        ("fallen_tree", "low", "p4"),
        ("roadblock", "critical", "p1"),
        ("roadblock", "high", "p1"),
        ("roadblock", "medium", "p3"),
        ("roadblock", "low", "p4"),
        ("pothole", "critical", "p1"),
        ("pothole", "high", "p2"),
        ("pothole", "medium", "p3"),
        ("pothole", "low", "p4"),
        ("waterlogging", "critical", "p1"),
        ("waterlogging", "high", "p2"),
        ("waterlogging", "medium", "p3"),
        ("waterlogging", "low", "p4"),
        ("road_crack", "critical", "p1"),
        ("road_crack", "high", "p2"),
        ("road_crack", "medium", "p3"),
        ("road_crack", "low", "p4"),
        ("other", "low", "p4"),
    ]
)
def test_default_priority(etype, severity, expected):
    assert _default_priority(etype, severity) == expected
