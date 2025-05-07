import unittest

from src.main import (
    count_operations_by_category,
    filter_by_status,
    load_json_data,
    search_in_description,
    sort_by_date
)


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

    def test_load_json_data(self):
        """ Тест функции загрузки данных из JSON-файла. """
        # Предполагается, что у вас есть корректный JSON-файл для тестирования
        # Здесь можно добавить код для создания временного файла или использовать mock
        result = load_json_data('path/to/your/json/file.json')
        self.assertIsInstance(result, list)

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

    def test_filter_by_status(self):
        """ Тест функции фильтрации по статусу. """
        result = filter_by_status(self.transactions, 'completed')
        expected_result = [
            {'id': 1, 'description': 'Перевод на счет', 'category': 'переводы',
             'status': 'completed', 'date': '2023-01-01'},
            {'id': 3, 'description': 'Кэшбэк', 'category': 'кэшбэк',
             'status': 'completed', 'date': '2023-01-03'},
            {'id': 4, 'description': 'Перевод в другой банк', 'category': 'переводы',
             'status': 'completed', 'date': '2023-01-04'},
        ]
        self.assertEqual(result, expected_result)

    def test_count_operations_by_category(self):
        """ Тест функции подсчета операций по категориям. """
        categories = ['переводы', 'платежи', 'кэшбэк']
        result = count_operations_by_category(self.transactions, categories)
        expected_result = {'переводы': 2, 'платежи': 2, 'кэшбэк': 1}
        self.assertEqual(result, expected_result)

    def test_sort_by_date(self):
        """ Тест функции сортировки по дате. """
        result = sort_by_date(self.transactions, ascending=True)
        expected_result = [
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
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
