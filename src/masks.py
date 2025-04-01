# Импорт конфигурации логирования
from .logging_config import setup_logger

# Создаем логгер для модуля masks
logger = setup_logger(__name__)


def get_mask_card_number(card_number: str) -> str:
    """Возвращает маску номера банковской карты форматом 'XXXX XX** **** XXXX'

    :param card_number: Номер карты
    :return: Маскированный номер карты
    """
    try:
        masked_card_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        logger.info(f"Маскировка карты выполнена: {masked_card_number}")
        return masked_card_number
    except Exception as e:
        logger.error(f"Ошибка маскировки карты: {e}")
        return ""


def get_mask_account_number(account_number: str) -> str:
    """Возвращает маску номера банковского счета по формату '**XXXX'.

    :param account_number: Номер счета
    :return: Маска номера счета
    """
    try:
        masked_account_number = f"**{account_number[-4:]}"
        logger.info(f"Маскировка счета выполнена: {masked_account_number}")
        return masked_account_number
    except Exception as e:
        logger.error(f"Ошибка маскировки счета: {e}")
        return ""
