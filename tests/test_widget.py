import pytest
from src.widget import mask_account_card


def test_mask_account_card_valid_master_card():
    account_number = "Master Card 1234123456785678"
    expected_output = "Master Card 1234 12** **** 5678"
    actual_output = mask_account_card(account_number)
    assert actual_output == expected_output

def test_mask_account_card_valid_account():
    account_number = "Счет 1234567890123456"
    expected_output = "Счет **3456"
    actual_output = mask_account_card(account_number)
    assert actual_output == expected_output