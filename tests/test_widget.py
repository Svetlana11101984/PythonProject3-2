import pytest
from src.widget import mask_account_card, get_date
from datetime import datetime


# Тесты для функции mask_account_card
@pytest.mark.parametrize("input_string, expected_output", [
    ("Visa Platinum 7000792289606361", "Visa Platinum ************6361"),
    ("Maestro 1596837868705199", "Maestro ************5199"),
    ("Счет 64686473678894779589", "Счет ****************9589"),
    ("MasterCard 7158300734726758", "MasterCard ************6758"),
    ("Счет 35383033474447895560", "Счет ****************5560"),
    ("Visa Classic 6831982476737658", "Visa Classic ************7658"),
    ("Visa Platinum 8990922113665229", "Visa Platinum ************5229"),
    ("Visa Gold 5999414228426353", "Visa Gold ************6353"),
    ("Счет 73654108430135874305", "Счет ****************4305"),
    ("1234567890123456", "************3456"),  # Добавили новый случай
])
def mask_account_card(account_info):
    if ' ' in account_info:
        parts = account_info.split(maxsplit=1)
        return f"{parts[0]} {'*' * (len(parts[1]) - 4)}{parts[1][-4:]}"
    else:
        return f"{'*' * (len(account_info) - 4)}{account_info[-4:]}"

    # Проверяем, что конец строки совпадает
    assert result.endswith(expected_output[-4:])

    # Проверяем, что маска содержит правильные символы
    assert '*' in result
    assert result.count('*') >= 6  # Минимум 6 звездочек

    # Проверяем, что возвращаемое значение — строка
    assert isinstance(result, str)


# Тесты для функции get_date
@pytest.mark.parametrize("input_date, expected_output", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2030-01-15T10:30:00.000000", "15.01.2030"),
    ("2023-10-15T10:30:00.000000", "15.10.2023")  # Исправлен формат даты
])
def test_get_date(input_date, expected_output):
    result = get_date(input_date)
    assert result == expected_output
    assert isinstance(result, str)  # Результат функции - строка
