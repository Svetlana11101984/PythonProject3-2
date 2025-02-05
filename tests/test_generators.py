import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        }
    ]

@pytest.mark.parametrize(
    "currency, expected_count",
    [
        ("USD", 2),
        ("RUB", 1),
        ("EUR", 0)
    ]
)
def test_filter_by_currency(currency, expected_count, transactions):
    filtered_transactions = list(filter_by_currency(transactions, currency))
    assert len(filtered_transactions) == expected_count

def test_transaction_descriptions(transactions):
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions == ["Перевод организации", "Перевод со счета на счет", "Перевод со счета на счет"]

@pytest.mark.parametrize(
    "start, stop, expected_card_numbers",
    [
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (10, 15, ["0000 0000 0000 0010", "0000 0000 0000 0011", "0000 0000 0000 0012", "0000 0000 0000 0013", "0000 0000 0000 0014", "0000 0000 0000 0015"])
    ]
)
def test_card_number_generator(start, stop, expected_card_numbers):
    generated_cards = list(card_number_generator(start, stop))
    assert generated_cards == expected_card_numbers