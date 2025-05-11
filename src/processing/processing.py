# src/processing.py
from typing import Dict, List


def sort_by_date(data: List[Dict], order: bool = True) -> List[Dict]:
    """Сортирует список словарей по ключу 'date'.

    Аргументы:
        data (List[Dict]): Список словарей с данными.
        order (bool): Булевое значение, определяющее порядок сортировки
        (True - по возрастанию, False - по убыванию).

    Возвращает:
        List[Dict]: Отсортированный список словарей.
    """
    sorted_data = sorted(data, key=lambda x: x["date"], reverse=not order)
    return sorted_data
