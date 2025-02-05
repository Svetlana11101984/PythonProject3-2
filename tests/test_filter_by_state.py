# test_processing.py
import pytest
from src.processing import filter_by_state


@pytest.fixture
def sample_data():
    return [
        {"id": 1, "name": "item1", "state": "active"},
        {"id": 2, "name": "item2", "state": "inactive"},
        {"id": 3, "name": "item3", "state": "active"},
    ]

def test_filter_by_state_active(sample_data):
    expected_output = [
        {"id": 1, "name": "item1", "state": "active"},
        {"id": 3, "name": "item3", "state": "active"},
    ]
    actual_output = filter_by_state(sample_data, "active")
    assert actual_output == expected_output

def test_filter_by_state_inactive(sample_data):
    expected_output = [
        {"id": 2, "name": "item2", "state": "inactive"},
    ]
    actual_output = filter_by_state(sample_data, "inactive")
    assert actual_output == expected_output

def test_filter_by_state_empty(sample_data):
    expected_output = []
    actual_output = filter_by_state(sample_data, "pending")
    assert actual_output == expected_output