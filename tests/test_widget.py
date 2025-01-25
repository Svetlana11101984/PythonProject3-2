import unittest
from bank_project.widget.mask_account_card import mask_account_card


class TestWidget(unittest.TestCase):

    def test_mask_account_card_invalid_length(self):
        account_number = "12345"
        expected_output = "Invalid card number"
        actual_output = mask_account_card(account_number)
        self.assertEqual(actual_output, expected_output)

    class TestWidget(unittest.TestCase):

        def test_mask_account_card_valid(self):
            account_number = "1234567890123456"
            expected_output = "123456789012**** 3456"
            actual_output = mask_account_card(account_number)
            self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()
