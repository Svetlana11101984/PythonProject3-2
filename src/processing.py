from typing import Dict, List


def filter_by_state(data: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Фильтрует список словарей по состоянию (ключу 'state').

    Аргументы:
        data (List[Dict]): Список словарей с данными.
        state (str): Значение, которое нужно найти (по умолчанию 'EXECUTED').

    Возвращает:
        List[Dict]: Новый список словарей, содержащих указанное состояние.
    """
    return [item for item in data if item.get("state") == state]


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
