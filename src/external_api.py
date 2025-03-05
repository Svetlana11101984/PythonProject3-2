import os
import requests

EXCHANGE_API_KEY = os.getenv('EXCHANGE_API_KEY')


def convert_to_rub(transaction):
    """
    Функция для конвертации суммы транзакции в рубли.

    :param transaction: Словарь с данными о транзакции
    :return: Сумма транзакции в рублях (тип float)
    """
    amount = transaction['amount']
    currency = transaction.get('currency', 'RUB').upper()
    if currency == 'RUB':
        return float(amount)
    elif currency in ['USD', 'EUR']:
        url = f'https://api.exchangerate.host/latest?base={currency}&symbols=RUB&key={EXCHANGE_API_KEY}'
        response = requests.get(url)
        rates = response.json()['rates']['RUB']
        return round(float(amount) * rates, 2)
    else:
        raise ValueError(f"Не поддерживаемая валюта: {currency}")
