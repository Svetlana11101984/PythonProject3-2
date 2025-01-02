def git commit -m "Initial commit with previous homework"get_mask_card_number(card_number: int) -> str:
    """Возвращает маску номера банковской карты форматом 'XXXX XX** **** XXXX'

    :param card_number: Номер карты
    :return: Маска номера карты
    """
    card_str = f"{card_number:016d}"  # Преобразуем число в строку 16 символов
    return f"{card_str[:4]} {card_str[4:7]}** {card_str[11:15]} {card_str[-4:]}"


def get_mask_account(account_number: int) -> str:
    """Возвращает маску номера банковского счета по формату '**XXXX'.

    :param account_number: Номер счета
    :return: Маска номера счета
    """
    account_str = f"{account_number:d}"  # Преобразуем число в строку
    return f"**{account_str[-4:]}"
