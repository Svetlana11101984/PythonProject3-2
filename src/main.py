import json
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Dict, List

from operations import read_json_file
from src.external_api import convert_to_rub


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


def filter_by_status(transactions: List[Dict], status: str) -> List[Dict]:
    """ Фильтрует транзакции по статусу. """
    normalized_status = status.upper()
    filtered_transactions = [
        txn for txn in transactions if txn.get('status', '').upper() == normalized_status
    ]
    return filtered_transactions


def count_categories(transactions: List[Dict]) -> Dict[str, int]:
    """ Группирует транзакции по категориям в описаниях. """
    categories = {
        'пополнение': ['пополнение', 'внесение', 'deposit'],
        'переводы': ['перевод', 'transfer', 'wiring'],
        'снятие наличных': ['снятие', 'withdrawal', 'cash out'],
        'интернет-платежи': ['интернет', 'онлайн', 'online']
    }

    counters = Counter()

    for txn in transactions:
        description = txn.get('description', '').lower()
        for category, keywords in categories.items():
            for kw in keywords:
                if kw in description:
                    counters[category] += 1
                    break

    return dict(counters)


def sort_by_date(transactions: List[Dict], ascending: bool = True) -> List[Dict]:
    """ Сортирует транзакции по дате. """
    return sorted(
        transactions,
        key=lambda txn: datetime.fromisoformat(txn.get('date')),
        reverse=not ascending
    )


def main():
    """ Основной поток выполнения программы. """
    if len(sys.argv) > 1:
        operations_file = sys.argv[1]
    else:
        operations_file = Path(__file__).parent / 'data' / 'operations.json'  # Путь по умолчанию

    transactions = load_json_data(operations_file)

    if not transactions:
        print("Нет доступных транзакций для обработки.")
        return

    converted_amounts = {}  # Инициализация словаря для хранения преобразованных сумм

    keyword = input("Введите ключевое слово для поиска транзакций (или оставьте пустым для пропуска): ")
    if keyword.strip():
        transactions = search_in_description(transactions, keyword)

    status = input("Введите статус для фильтрации (EXECUTED, CANCELED, PENDING): ")
    transactions = filter_by_status(transactions, status)

    ascending = input("Сортировать по возрастанию? (да/нет): ").strip().lower() == 'да'
    sorted_transactions = sort_by_date(transactions, ascending)

    counts = count_categories(sorted_transactions)
    print("Количество транзакций по категориям:")
    for cat, count in counts.items():
        print(f"- {cat}: {count}")

    # Преобразуем суммы и сохраняем их в словаре
    for tid, transaction in enumerate(sorted_transactions):
        amount = convert_to_rub(transaction)
        converted_amounts[tid] = amount  # Сохраняем преобразованную сумму по идентификатору транзакции
        print(f"TID {tid}: {transaction['description']} - {amount} RUB")

    # Выводим все преобразованные суммы
    print("\nПреобразованные суммы:")
    for tid, amount in converted_amounts.items():
        print(f"TID {tid}: {amount} RUB")


if __name__ == "__main__":
    main()
