from masks import get_mask_card_number as mask_card_number, get_mask_account_number as mask_account_number

def mask_account_card(account_info: str) -> str:
    """
    Функция для маскирования номеров карт и счетов.

    :param account_info: Строка с типом и номером карты или счета.
    :return: Строка с замаскированным номером.
    """
    if 'Счет' in account_info:
        return f"Счет {mask_account_number(account_info.split()[-1])}"
    else:
        return f"{account_info[:12]} {mask_card_number(account_info[12:])}"

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
