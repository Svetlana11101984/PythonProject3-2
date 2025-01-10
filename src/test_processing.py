import unittest
from processing import filter_by_state

class TestProcessing(unittest.TestCase):
    def test_filter_by_state_executed(self):
        # Подготавливаем тестовые данные
        transactions = [
            {'id': 1, 'amount': 1000, 'state': 'PENDING'},
            {'id': 2, 'amount': 2000, 'state': 'EXECUTED'},
            {'id': 3, 'amount': 3000, 'state': 'CANCELED'}
        ]

        # Выполняем фильтрацию
        filtered_transactions = filter_by_state(transactions)

        # Проверка результата
        self.assertEqual(len(filtered_transactions), 1)
        self.assertDictEqual(filtered_transactions[0], {'id': 2, 'amount': 2000, 'state': 'EXECUTED'})

    def test_filter_by_state_pending(self):
        transactions = [
            {'id': 1, 'amount': 1000, 'state': 'PENDING'},
            {'id': 2, 'amount': 2000, 'state': 'EXECUTED'},
            {'id': 3, 'amount': 3000, 'state': 'CANCELED'}
        ]

        filtered_transactions = filter_by_state(transactions, state='PENDING')

        self.assertEqual(len(filtered_transactions), 1)
        self.assertDictEqual(filtered_transactions[0], {'id': 1, 'amount': 1000, 'state': 'PENDING'})

    def test_filter_by_state_no_matches(self):
        transactions = [
            {'id': 1, 'amount': 1000, 'state': 'PENDING'},
            {'id': 2, 'amount': 2000, 'state': 'EXECUTED'},
            {'id': 3, 'amount': 3000, 'state': 'CANCELED'}
        ]

        filtered_transactions = filter_by_state(transactions, state='COMPLETED')

        self.assertEqual(len(filtered_transactions), 0)

    def test_filter_empty_transactions(self):
        transactions = []

        filtered_transactions = filter_by_state(transactions)

        self.assertEqual(len(filtered_transactions), 0)

if __name__ == '__main__':
    unittest.main()