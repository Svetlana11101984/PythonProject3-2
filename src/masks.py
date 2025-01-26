def get_mask_card_number(card_number: str) -> str:
    """Возвращает маску номера банковской карты форматом 'XXXX XX** **** XXXX'

    :param card_number: Номер карты
    :return: Маскированный номер карты
    """
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account_number(account_number: str) -> str:
    """Возвращает маску номера банковского счета по формату '**XXXX'.

    :param account_number: Номер счета
    :return: Маска номера счета
    """
    return f"**{account_number[-4:]}"
