def filter_by_currency(transactions, currency):
    """
    Возвращает итератор транзакций с указанной валютой.

    :param transactions: Список словарей, представляющих транзакции.
    :param currency: Валюта для фильтрации.
    :return: Итератор, выдающий подходящие транзакции.
    """
    return (txn for txn in transactions if txn["operationAmount"]["currency"]["code"] == currency)


def transaction_descriptions(transactions):
    """
    Генератор описаний транзакций.

    :param transactions: Список словарей, представляющий транзакции.
    :return: Описания транзакций по порядку.
    """
    for txn in transactions:
        yield txn["description"]


def card_number_generator(start=1, stop=10000):
    """
    Генератор номеров банковских карт в формате 'XXXX XXXX XXXX XXXX'.

    :param start: Начальная граница диапазона номеров.
    :param stop: Конечная граница диапазона номеров.
    :return: Следующий номер банковской карты.
    """
    for i in range(start, stop + 1):
        yield f"{i:016}".replace(" ", "").replace("(.{4})", r"\1 ")