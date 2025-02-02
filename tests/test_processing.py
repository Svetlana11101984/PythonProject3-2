import pytest
from src.processing import sort_by_date

def test_sort_by_date_ascending():
    unsorted_data = [
        {"date": "2023-01-05"},
        {"date": "2023-02-03"},
        {"date": "2023-01-15"}
    ]
    expected_output = [
        {"date": "2023-01-05"},
        {"date": "2023-01-15"},
        {"date": "2023-02-03"}
    ]
    actual_output = sort_by_date(unsorted_data)
    assert actual_output == expected_output

def test_sort_by_date_descending():
    unsorted_data = [
        {"date": "2023-04-20"},
        {"date": "2023-06-30"},
        {"date": "2023-08-25"}
    ]
    expected_output = [
        {"date": "2023-08-25"},
        {"date": "2023-06-30"},
        {"date": "2023-04-20"}
    ]
    actual_output = sort_by_date(unsorted_data, order=False)
    assert actual_output == expected_output