import json
import re
from collections import Counter
from datetime import datetime
from typing import Dict, List


def load_json_data(filepath: str) -> List[Dict]:
    """ Загружает данные из JSON-файла. """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Ошибка: Файл по пути '{filepath}' не найден.")
        return []
    except json.JSONDecodeError:
        print("Ошибка: Не удалось декодировать файл JSON.")
        return []


def search_in_description(transactions: List[Dict], keyword: str) -> List[Dict]:
    """ Производит поиск транзакций по наличию ключевого слова в описании. """
    # Создаем регулярное выражение для нечувствительного к регистру поиска
    pattern = re.compile(re.escape(keyword), re.IGNORECASE)
    matching_transactions = [
        txn for txn in transactions if pattern.search(txn.get('description', ''))
    ]
    return matching_transactions


def filter_operations(operations, search_string):
    """
    Фильтрует список операций по строке поиска.

    :param operations: Список словарей с операциями
    :param search_string: Строка для поиска в описании операций
    :return: Отфильтрованный список операций
    """
    filtered_operations = [
        operation for operation in operations
        if re.search(search_string, operation['description'], re.IGNORECASE)
    ]
    return filtered_operations


def filter_by_status(transactions: List[Dict], status: str) -> List[Dict]:
    """ Фильтрует транзакции по статусу. """
    normalized_status = status.upper()
    filtered_transactions = [
        txn for txn in transactions if txn.get('status', '').upper() == normalized_status
    ]
    return filtered_transactions


def count_operations_by_category(operations, categories):
    """
    Подсчитывает количество операций по категориям.

    :param operations: Список операций
    :param categories: Список категорий
    :return: Словарь с количеством операций по категориям
    """
    category_count = Counter()

    for operation in operations:
        category = operation.get('category')
        if category in categories:
            category_count[category] += 1

    return dict(category_count)


def sort_by_date(transactions: List[Dict], ascending: bool = True) -> List[Dict]:
    """ Сортирует транзакции по дате. """
    return sorted(
        transactions,
        key=lambda txn: datetime.fromisoformat(txn.get('date')),
        reverse=not ascending
    )


def main():
    operations = [
        {'id': 1, 'description': 'Перевод на счет', 'category': 'переводы'},
        {'id': 2, 'description': 'Оплата за услуги', 'category': 'платежи'},
        {'id': 3, 'description': 'Кэшбэк', 'category': 'кэшбэк'},
        # Добавьте другие операции по необходимости
    ]

    print("Добро пожаловать в систему управления операциями!")

    search_string = input("Введите строку для поиска в описании операций: ")
    filtered = filter_operations(operations, search_string)
    print("Отфильтрованные операции:")
    for op in filtered:
        print(op)

    categories = ['переводы', 'платежи', 'кэшбэк']
    category_count = count_operations_by_category(operations, categories)
    print("\nКоличество операций по категориям:")
    for category, count in category_count.items():
        print(f"{category}: {count}")


if __name__ == "__main__":
    main()
