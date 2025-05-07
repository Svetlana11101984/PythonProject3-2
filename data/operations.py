import re


def filter_transactions(transactions, search_term):
    """Фильтрация транзакций по строке поиска в описании."""
    filtered = [txn for txn in transactions if
                re.search(re.escape(search_term), txn.get('description', ''), re.IGNORECASE)]
    return filtered


def count_categories(transactions, categories):
    """Подсчет транзакций по категориям."""
    category_count = {category: 0 for category in categories}

    for txn in transactions:
        description = txn.get('description', '')
        for category in categories:
            if category.lower() in description.lower():
                category_count[category] += 1

    return category_count
