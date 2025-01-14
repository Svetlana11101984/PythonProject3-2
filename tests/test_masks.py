from src.masks import get_mask_card_number, get_mask_account_number


def test_get_mask_card_number():
    test_data = {
        "4234567890123456": "4234 56** **** 3456",
        "5234123409876543": "5234 12** **** 6543",
        "6123456789012345": "6123 45** **** 2345",
    }

    for card_number, expected_result in test_data.items():
        assert get_mask_card_number(card_number) == expected_result


def test_get_mask_account_number():
    test_data = {
        "9876543210": ("3210", "******3210"),
        "0987654321": ("6543", "******6543"),
        "1234567890": ("7890", "******7890"),
    }

    for account_number, (last_four_digits, expected_result)\
            in test_data.items():
        assert get_mask_account_number(
            account_number, last_four_digits
        ) == expected_result
