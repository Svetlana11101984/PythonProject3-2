def filter_by_state(transactions, state):
    # Реализация функции
    return [txn for txn in transactions if txn['state'] == state]
