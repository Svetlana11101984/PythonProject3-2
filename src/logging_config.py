import logging
from logging.handlers import RotatingFileHandler


def setup_logger(logger_name, level=logging.DEBUG):
    """
    Функция для настройки логера.

    :param logger_name: Имя логера
    :param level: Уровень логирования (по умолчанию DEBUG)
    :return: Логер
    """
    # Создаем логер с указанным именем
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    # Настройка формата логов
    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    # Настройка записи в файл
    log_filename = f'logs/{logger_name}.log'
    file_handler = RotatingFileHandler(log_filename, mode='w', maxBytes=1024 * 1024 * 10, backupCount=5)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    # Добавляем обработчики логов
    logger.addHandler(file_handler)

    return logger
