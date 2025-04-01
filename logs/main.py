from src.logging_config import setup_logger
from src.utils import read_json_file
from src.masks import get_mask_card_number, get_mask_account_number


# Создаем логгер для основного модуля
logger = setup_logger(__name__)


if __name__ == "__main__":
    # Чтение данных из JSON файла
    transactions_data = read_json_file("transactions.json")
    logger.info(f"Прочитано {len(transactions_data)} транзакций.")

    # Демонстрация работы масок
    card_number = "1234567890123456"
    account_number = "98765432109876543210"

    masked_card_number = get_mask_card_number(card_number)
    masked_account_number = get_mask_account_number(account_number)

    logger.info(f"Маскированный номер карты: {masked_card_number}")
    logger.info(f"Маскированный номер счета: {masked_account_number}")
