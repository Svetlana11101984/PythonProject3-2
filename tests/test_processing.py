import pytest
from datetime import datetime
from src.processing import filter_by_state, sort_by_date

# Генерация тестового набора данных
@pytest.fixture

def test_data():
    return [
        {'id': 1, 'state': 'PENDING', 'date': datetime(2023, 10, 15)},
        {'id': 2, 'state': 'EXECUTED', 'date': datetime(2023, 9, 20)},
        {'id': 3, 'state': 'CANCELED', 'date': datetime(2023, 8, 25)},
        {'id': 4, 'state': 'EXECUTED', 'date': datetime(2023, 7, 30)}
    ]

@pytest.mark.parametrize("state, expected_result", [
    ('EXECUTED', [{'id': 2, 'state': 'EXECUTED', 'date': datetime(2023, 9, 20)}, {'id': 4, 'state': 'EXECUTED', 'date': datetime(2023, 7, 30)}]),
    ('PENDING', [{'id': 1, 'state': 'PENDING', 'date': datetime(2023, 10, 15)}])
])

def test_filter_by_state(test_data, state, expected_result):
    result = filter_by_state(test_data, state)
    assert result == expected_result

@pytest.mark.parametrize("order, expected_result", [
        (True, [{'id': 4, 'state': 'EXECUTED', 'date': datetime(2023, 7, 30)}, {'id': 3, 'state': 'CANCELED', 'date': datetime(2023, 8, 25)}, {'id': 2, 'state': 'EXECUTED', 'date': datetime(2023, 9, 20)}, {'id': 1, 'state': 'PENDING', 'date': datetime(2023, 10, 15)}]),
        (False, [({'id': 1, 'state': 'PENDING', 'date': datetime(2023, 10, 15)}, {'id': 2, 'state': 'EXECUTED', 'date': datetime(2023, 9, 20)}, {'id': 3, 'state': 'CANCELED', 'date': datetime(2023, 8, 25)}, {'id': 4, 'state': 'EXECUTED', 'date': datetime(2023, 7, 30)})
                 ])])

def sort_by_date(data, order):
    if order:
        sorted_data = sorted(data, key=lambda x: x['date'], reverse=True)
    else:
        sorted_data = sorted(data, key=lambda x: x['date'])
    return sorted_data
