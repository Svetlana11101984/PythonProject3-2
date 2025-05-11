# tests/test_filter_by_state.py
import pytest

from src.processing.filtering import filter_by_state


@pytest.fixture
def sample_data():
    """Фикстура для предоставления тестового набора данных."""
    return [
        {"id": 1, "name": "item1", "state": "active"},
        {"id": 2, "name": "item2", "state": "inactive"},
        {"id": 3, "name": "item3", "state": "active"},
    ]


def test_filter_by_state_active(sample_data):
    """Тест фильтрации активных элементов."""
    expected_output = [
        {"id": 1, "name": "item1", "state": "active"},
        {"id": 3, "name": "item3", "state": "active"},
    ]
    actual_output = filter_by_state(sample_data, "active")
    assert actual_output == expected_output


def test_filter_by_state_inactive(sample_data):
    """Тест фильтрации неактивных элементов."""
    expected_output = [
        {"id": 2, "name": "item2", "state": "inactive"},
    ]
    actual_output = filter_by_state(sample_data, "inactive")
    assert actual_output == expected_output


def test_filter_by_state_no_match(sample_data):
    """Тест фильтрации по несуществующему статусу."""
    expected_output = []  # Должно вернуть пустой список
    actual_output = filter_by_state(sample_data, "pending")
    assert actual_output == expected_output
