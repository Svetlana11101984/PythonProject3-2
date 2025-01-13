from src.masks import get_mask_card_number as mask_card_number, get_mask_account_number as mask_account_number

def mask_account_card(account_number):
    parts = account_number.split()
    if len(parts) > 1:
        # Если номер карты состоит из нескольких частей (например, Visa Gold 5999 4142 2842 6353)
        masked_parts = []
        for part in parts[1:]:
            if len(part) <= 4:
                masked_part = part
            else:
                masked_part = part[:1] + "*" * (len(part) - 4) + part[-4:]
            masked_parts.append(masked_part)
        return f"{parts[0]} {' '.join(masked_parts)}"
    else:
        # Если номер карты представлен одной строкой (например, MasterCard 1234567890123456)
        return f"{parts[0]} {'*' * (len(parts[0]) - 4)}{parts[0][-4:]}"

def mask_card_number(card_number: str) -> str:
    return card_number[:6] + '*' * (len(card_number) - 10) + card_number[-4:]

def mask_account_number(account_number: str) -> str:
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
