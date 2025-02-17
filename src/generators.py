def filter_by_currency(transactions, currency_code):
    """
    Функция фильтрует транзакции по заданному коду валюты.

    :param transactions: список словарей, представляющих транзакции
    :type transactions: list[dict]
    :param currency_code: код валюты для фильтрации
    :type currency_code: str
    :return: итератор, выдающий подходящие транзакции
    :rtype: Iterator[dict]
    """
    return (
        transaction
        for transaction in transactions
        if transaction["operationAmount"]["currency"]["code"] == currency_code
    )


def transaction_descriptions(transactions):
    """
    Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.

    :param transactions: список словарей, представляющих транзакции
    :type transactions: list[dict]
    :yield: описание каждой транзакции
    :rtype: str
    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start, end):
    """
    Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX.

    :param start: начальный номер карты
    :type start: int
    :param end: конечный номер карты
    :type end: int
    :yield: номер банковской карты в формате XXXX XXXX XXXX XXXX
    :rtype: str
    """
    for i in range(start, end + 1):
        # Преобразуем число в строку формата '0000 0000 0000 0000'
        formatted_card_number = f"{i:016d}"
        # Разделяем каждую группу из четырех цифр пробелом
        grouped_card_number = " ".join(formatted_card_number[i : i + 4] for i in range(0, 16, 4))
        yield grouped_card_number
