def filter_by_currency(transactions, currency_code):
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction

def transaction_descriptions(transactions):
    for transaction in transactions:
        yield transaction["description"]

def card_number_generator(start, stop):
    for i in range(start, stop + 1):
        yield f'{i:016}'.replace(' ', '0').replace('0', 'X')[::-1].replace('X', ' ').strip()[::-1]