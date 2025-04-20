import csv
from pathlib import Path

import pandas as pd

# Глобальная константа для путей к файлам
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / 'data'

CSV_FILE_PATH = DATA_DIR / 'transactions.csv'
EXCEL_FILE_PATH = DATA_DIR / 'transactions.xlsx'


def read_csv_transactions(csv_file_path=CSV_FILE_PATH, limit=None):
    """
    Функция для считывания финансовых операций из CSV файла.

    Параметры:
    ----------
    csv_file_path : str or Path-like object
        Путь к файлу CSV. По умолчанию берется путь к файлу в директории 'data'.
    limit : int, optional
        Лимит на количество возвращаемых записей.

    Возвращает:
    ---------
    list of dict
        Список словарей с финансовыми операциями.
    """
    try:
        with open(csv_file_path, 'r', newline='', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            records = list(reader)

            # Применяем ограничение, если оно передано
            if limit is not None:
                records = records[:limit]

            return records
    except FileNotFoundError:
        print(f"Файл '{csv_file_path}' не найден.")
        return []


def read_excel_transactions(excel_file_path=EXCEL_FILE_PATH, limit=None):
    """
    Функция для считывания финансовых операций из Excel файла.

    Параметры:
    ----------
    excel_file_path : str or Path-like object
        Путь к файлу Excel. По умолчанию берется путь к файлу в директории 'data'.
    limit : int, optional
        Лимит на количество возвращаемых записей.

    Возвращает:
    ---------
    list of dict
        Список словарей с финансовыми операциями.
    """
    try:
        df = pd.read_excel(excel_file_path)

        # Преобразование dataframe в список словарей
        records = df.to_dict('records')

        # Применяем ограничение, если оно передано
        if limit is not None:
            records = records[:limit]

        return records
    except FileNotFoundError:
        print(f"Файл '{excel_file_path}' не найден.")
        return []
