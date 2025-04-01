import json
from typing import List, Dict

# Импортируем логгер из logging_config.py
from .logging_config import setup_logger

# Создаем логгер для модуля utils
logger = setup_logger(__name__)


def read_json_file(file_path: str) -> List[Dict]:
    """
    Функция для чтения JSON-файла и возврата списка словарей с данными о финансовых транзакциях.

    :param file_path: Путь к файлу JSON
    :return: Список словарей с данными о транзакциях или пустой список
    """
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            if isinstance(data, list):
                logger.info(f"JSON файл успешно прочитан: {len(data)} элементов")
                return data
            else:
                logger.warning("JSON файл не содержит список")
                return []
    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_path}")
        return []
    except json.JSONDecodeError:
        logger.error(f"Ошибка декодирования JSON: {file_path}")
        return []
    except Exception as e:
        logger.exception(f"Произошла неожиданная ошибка: {e}")
        return []
