import json
from typing import List, Dict


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
                return data
            else:
                print("JSON файл не содержит список")
                return []
    except FileNotFoundError:
        print("Файл не найден")
        return []
    except json.JSONDecodeError:
        print("Ошибка декодирования JSON")
        return []
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return []
