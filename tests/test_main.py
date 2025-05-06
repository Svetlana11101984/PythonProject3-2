import unittest

from src.main import count_categories, filter_by_status, load_json_data, search_in_description, sort_by_date
from src.utils import read_json_file


class TestMainFunctions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.transactions = read_json_file('data/operations.json')

    def test_load_json_data(self):
        # Проверка успешной загрузки данных из JSON-файла
        data = load_json_data('data/operations.json')
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

    def test_filter_by_status(self):
        transactions = [
            {"status": "EXECUTED", "amount": 100},
            {"status": "CANCELED", "amount": 200},
            {"status": "PENDING", "amount": 300}
        ]

        # Проверим, что транзакции фильтруются корректно
        executed_txns = filter_by_status(transactions, 'EXECUTED')
        self.assertEqual(len(executed_txns), 1)
        self.assertEqual(executed_txns[0]['amount'], 100)

        canceled_txns = filter_by_status(transactions, 'CANCELED')
        self.assertEqual(len(canceled_txns), 1)
        self.assertEqual(canceled_txns[0]['amount'], 200)

        pending_txns = filter_by_status(transactions, 'PENDING')
        self.assertEqual(len(pending_txns), 1)
        self.assertEqual(pending_txns[0]['amount'], 300)

    def test_search_in_description(self):
        transactions = [
            {"description": "Пополнение счёта", "amount": 100},
            {"description": "Перевод на другой счёт", "amount": 200},
            {"description": "Снятие наличных", "amount": 300},
            {"description": "Интернет-платеж", "amount": 400}
        ]

        # Проверим поиск по каждому ключевому слову
        popolnenie_txns = search_in_description(transactions, 'пополнение')
        self.assertEqual(len(popolnenie_txns), 1)
        self.assertEqual(popolnenie_txns[0]['amount'], 100)

        perevod_txns = search_in_description(transactions, 'перевод')
        self.assertEqual(len(perevod_txns), 1)
        self.assertEqual(perevod_txns[0]['amount'], 200)

        snatie_txns = search_in_description(transactions, 'снятие')
        self.assertEqual(len(snatie_txns), 1)
        self.assertEqual(snatie_txns[0]['amount'], 300)

        internet_txns = search_in_description(transactions, 'интернет')
        self.assertEqual(len(internet_txns), 1)
        self.assertEqual(internet_txns[0]['amount'], 400)

    def test_count_categories(self):
        transactions = [
            {"description": "Пополнение счёта", "amount": 100},
            {"description": "Перевод средств", "amount": 200},
            {"description": "Снятие наличных", "amount": 300},
            {"description": "Интернет-платеж", "amount": 400}
        ]

        categories = count_categories(transactions)
        self.assertIn('пополнение', categories)
        self.assertIn('переводы', categories)
        self.assertIn('снятие наличных', categories)
        self.assertIn('интернет-платежи', categories)
        self.assertGreater(sum(categories.values()), 0)

    def test_sort_by_date(self):
        transactions = [
            {"date": "2023-10-01", "amount": 100},
            {"date": "2023-09-30", "amount": 200},
            {"date": "2023-09-29", "amount": 300},
            {"date": "2023-09-28", "amount": 400}
        ]

        # Проверим сортировку по возрастанию
        asc_sorted_txns = sort_by_date(transactions, ascending=True)
        self.assertEqual([txn['date'] for txn in asc_sorted_txns],
                         ['2023-09-28', '2023-09-29', '2023-09-30', '2023-10-01'])

        # Проверим сортировку по убыванию
        desc_sorted_txns = sort_by_date(transactions, ascending=False)
        self.assertEqual([txn['date'] for txn in desc_sorted_txns],
                         ['2023-10-01', '2023-09-30', '2023-09-29', '2023-09-28'])


if __name__ == '__main__':
    unittest.main()
