def filter_by_currency(transactions, currency_code):
    """Фильтрует транзакции по заданной валюте и возвращает итератор."""
    for transaction in transactions:
        if transaction.get('operationAmount', {}).get('currency', {}).get('code') == currency_code:
            yield transaction

def transaction_descriptions(transactions):
    """Генератор, который возвращает описание каждой операции."""
    for transaction in transactions:
        yield transaction.get('description')

def card_number_generator(start, stop):
    """Генератор, который выдает номера банковских карт в заданном диапазоне."""
    for number in range(start, stop + 1):
        yield f"{number:016d}"  # Форматирование номера карты