import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

# Пример данных для тестов
transactions = [
    {'description': 'Перевод организации', 'operationAmount': {'amount': '1000.00', 'currency': {'code': 'USD'}}},
    {'description': 'Оплата карты', 'operationAmount': {'amount': '500.00', 'currency': {'code': 'USD'}}},
    {'description': 'Книга', 'operationAmount': {'amount': '300.00', 'currency': {'code': 'EUR'}}},
    {'description': 'Перевод другому человеку', 'operationAmount': {'amount': '700.00', 'currency': {'code': 'USD'}}},
]

def test_filter_by_currency():
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 3  # Проверьте количество транзакций в USD

def test_transaction_descriptions():
    descriptions = transaction_descriptions(transactions)
    assert next(descriptions) == "Перевод организации"  # Проверяем, что первое значение - это "Перевод организации"

def test_card_number_generator():
    generated_numbers = list(card_number_generator(1, 5))
    assert generated_numbers == ['0000000000000001', '0000000000000002', '0000000000000003', '0000000000000004', '0000000000000005']
