import pytest
from simulator import Bus, ROUTE_MAP

def test_bus_to_dict_serialization():
    # Instantiate the actual Bus object with the real attributes in simulator.py
    bus = Bus(
        bus_id="BUS-1",
        route_id=1,
        lat=28.1234567,
        lng=77.1234567,
        speed=45.67,
        heading=180.12,
        network="good",
        wp_idx=0,
        wp_frac=0.5,
        offline_q=["EVT-001", "EVT-002"]
    )

    # Call to_dict()
    bus_dict = bus.to_dict()

    # Assert properties mapping and rounding for the actual implementation
    assert bus_dict["id"] == "BUS-1"
    assert bus_dict["route"] == 1
    assert bus_dict["lat"] == 28.123457
    assert bus_dict["lng"] == 77.123457
    assert bus_dict["speed"] == 45.7
    assert bus_dict["heading"] == 180.1
    assert bus_dict["network"] == "good"
    assert bus_dict["queued"] == 2
    assert bus_dict["color"] == ROUTE_MAP[1]["color"]
