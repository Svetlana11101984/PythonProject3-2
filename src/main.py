import re
from collections import Counter
from typing import Dict, List


def search_in_description(transactions: List[Dict], keyword: str) -> List[Dict]:
    """ Производит поиск транзакций по наличию ключевого слова в описании. """
    pattern = re.compile(re.escape(keyword), re.IGNORECASE)
    matching_transactions = [
        txn for txn in transactions if pattern.search(txn.get('description', ''))
    ]
    return matching_transactions


def filter_operations(operations: List[Dict], search_string: str) -> List[Dict]:
    """ Фильтрует список операций по строке поиска. """
    filtered_operations = [
        operation for operation in operations
        if re.search(search_string, operation.get('description', ''), re.IGNORECASE)
    ]
    return filtered_operations


def count_operations_by_category(operations: List[Dict], categories: List[str]) -> Dict[str, int]:
    """ Подсчитывает количество операций по категориям. """
    category_count = Counter()
    for operation in operations:
        # Изменено, чтобы использовать get для избежания KeyError
        category = operation.get('category')
        if category in categories:
            category_count[category] += 1
    return dict(category_count)


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
