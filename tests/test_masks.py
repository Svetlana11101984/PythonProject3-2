import pytest
from src.masks import get_mask_card_number


@pytest.mark.parametrize("card_number, expected", [
    ("4234567890123456", "4234 56** **** 3456"),
    ("5234123409876543", "5234 12** **** 6543"),
    ("6123456789012345", "6123 45** **** 2345"),
])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected