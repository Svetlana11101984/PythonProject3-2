import csv
from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent.parent / 'data'


def read_csv_transactions(csv_file_path=None, limit=None):
    """Читает транзакции из CSV файла и возвращает в формате списка словарей.

    Args:
        csv_file_path (str): Путь к файлу CSV.
        limit (int): Максимальное число возвращаемых записей.

    Returns:
        List[Dict]: Список транзакций.
    """
    csv_file_path = DATA_DIR / 'transactions.csv' if csv_file_path is None else csv_file_path
    try:
        with open(csv_file_path, 'r', newline='', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            records = list(reader)
            if limit is not None:
                records = records[:limit]
            return records
    except FileNotFoundError:
        print(f"Не найден файл {csv_file_path}")
        return []


def read_excel_transactions(excel_file_path=None, limit=None):
    excel_file_path = DATA_DIR / 'transactions_excel.xlsx' if excel_file_path is None else excel_file_path
    print(f"Чтение Excel файла из: {excel_file_path}")
    try:
        df = pd.read_excel(excel_file_path)
        if limit is not None:
            df = df.iloc[:limit]
        return df.to_dict('records')
    except FileNotFoundError:
        print(f"Не найден файл {excel_file_path}")
        return []
