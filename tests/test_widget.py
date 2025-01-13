import pytest
from src.widget import mask_account_card, get_date


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
    ("Счет 73654108430135874305", "Счет ****************4305")
])
def test_mask_account_card(input_string, expected_output):
    result = mask_account_card(input_string)

    # Проверить, что начало строки совпадает
    assert result.startswith(input_string.split(' ')[0])  # Первая часть строки должна остаться неизменной

    # Проверить, что конец строки совпадает
    if ' ' in input_string:
        assert result.endswith(input_string[-4:])
    else:
        assert result.endswith(input_string[-4:])

    # Проверить, что маска содержит правильные символы
    assert '*' in result
    assert result.count('*') >= 6  # Минимум 6 звездочек

    # Проверить, что возвращаемое значение — строка
    assert isinstance(result, str)


# Тесты для функции get_date
@pytest.mark.parametrize("input_date, expected_output", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2030-01-15T10:30:00.000000", "15.01.2030")
])
def test_get_date(input_date, expected_output):
    result = get_date(input_date)

    # Проверить, что формат даты правильный
    assert result == expected_output

    # Проверить, что возвращаемое значение — строка
    assert isinstance(result, str)
