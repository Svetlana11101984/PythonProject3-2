from src.masks import get_mask_account_number, get_mask_card_number


def mask_account_card(account_info: str) -> str:
    """Функция маскировки номера карты и счета"""
    if "Счет" in account_info:
        return f"Счет {get_mask_account_number(account_info.split()[-1])}"
    else:
        card_name = account_info.split()
        card_number = card_name.pop()
        return f"{' '.join(card_name)} {get_mask_card_number(card_number)}"


def get_date(date_str: str) -> str:
    """
Преобразует дату из одного формата в другой.

    :param date_str: Дата в формате "YYYY-MM-DDTHH:MM:SS.mmmmmm".
    :return: Дата в формате "DD.MM.YYYY".
    """
    from datetime import datetime
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
        return dt.strftime("%d.%m.%Y")
    except ValueError as e:
        print(f"Ошибка преобразования даты: {e}")
        return "Не удалось преобразовать дату."
