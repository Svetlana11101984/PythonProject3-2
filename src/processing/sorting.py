# processing/sorting.py
from datetime import datetime


def sort_by_date(transactions):
    return sorted(transactions, key=lambda txn: datetime.fromisoformat(txn['date']), reverse=True)
