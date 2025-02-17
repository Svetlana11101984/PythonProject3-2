import pytest
from src.masks import get_mask_card_number



@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("4234567890123456", "4234 56** **** 3456"),
        ("5234123409876543", "5234 12** **** 6543"),
        ("6123456789012345", "6123 45** **** 2345"),
    ],
)
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2023-01-01T00:00:00.000001", "01.01.2023"),
        ("2023-12-31T23:59:59.999999", "31.12.2023"),
        ("invalid-date", "Не удалось преобразовать дату."),
    ],
)
def test_get_date(date_str, expected):
    assert get_date(date_str) == expected
