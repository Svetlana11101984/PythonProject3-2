import unittest

from src.main import count_operations_by_category, search_in_description


class TestMainFunctions(unittest.TestCase):

    def setUp(self):
        """ Метод, который будет выполняться перед каждым тестом. """
        self.transactions = [
            {'id': 1, 'description': 'Перевод на счет', 'category': 'переводы',
             'status': 'completed', 'date': '2023-01-01'},
            {'id': 2, 'description': 'Оплата за услуги', 'category': 'платежи',
             'status': 'pending', 'date': '2023-01-02'},
            {'id': 3, 'description': 'Кэшбэк', 'category': 'кэшбэк',
             'status': 'completed', 'date': '2023-01-03'},
            {'id': 4, 'description': 'Перевод в другой банк', 'category': 'переводы',
             'status': 'completed', 'date': '2023-01-04'},
            {'id': 5, 'description': 'Оплата интернета', 'category': 'платежи',
             'status': 'failed', 'date': '2023-01-05'},
        ]

    def test_search_in_description(self):
        """ Тест функции поиска по описанию. """
        result = search_in_description(self.transactions, 'оплата')
        expected_result = [
            {'id': 2, 'description': 'Оплата за услуги', 'category': 'платежи',
             'status': 'pending', 'date': '2023-01-02'},
            {'id': 5, 'description': 'Оплата интернета', 'category': 'платежи',
             'status': 'failed', 'date': '2023-01-05'},
        ]
        self.assertEqual(result, expected_result)

    def test_count_operations_by_category(self):
        """ Тест функции подсчета операций по категориям. """
        categories = ['переводы', 'платежи', 'кэшбэк']
        result = count_operations_by_category(self.transactions, categories)
        expected_result = {'переводы': 2, 'платежи': 2, 'кэшбэк': 1}
        self.assertEqual(result, expected_result)

    # Здесь можно добавить тесты для сортировки по дате и другим функциям


if __name__ == '__main__':
    unittest.main()
