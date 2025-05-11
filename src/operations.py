# operations.py
from collections import Counter


def count_operations_by_category(transactions):
    categories = [txn['category'] for txn in transactions]
    return Counter(categories)


def search_in_description(transactions, keyword):
    return [txn for txn in transactions if keyword.lower() in txn['description'].lower()]
