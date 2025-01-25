# from src.masks import get_mask_card_number as mask_card_number,
# get_mask_account_number as mask_account_number

def mask_account_card(account_info):
    # Если строка содержит пробел, она включает информацию о банке или типе карты
    if ' ' in account_info:
        parts = account_info.split()
        masked_number = f"{parts[0]} {'*' * (len(parts[1]) - 4)}{parts[1][-4:]}"
        return masked_number
    else:
        # Если пробела нет, значит, дана лишь карта, маскамируем ее нужным образом
        return f"{'*' * (len(account_info) - 4)}{account_info[-4:]}"


def _mask_card_number(card_number: str) -> str:
    return card_number[:6] + '*' * (len(card_number) - 10) + card_number[-4:]


def _mask_account_number(account_number: str) -> str:
    return '*' * (len(account_number) - 4) + account_number[-4:]


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
