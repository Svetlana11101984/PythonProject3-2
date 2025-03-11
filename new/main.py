# import sys  # Импорт временно отключён, но оставлен для будущего использования
from src.utils import read_json_file
from src.external_api import convert_to_rub


def main():
    transactions = read_json_file('data/operations.json')

    for transaction in transactions:
        converted_amount = convert_to_rub(transaction)
        print(f"Транзакция: {transaction}, сумма в рублях: {converted_amount:.2f}")


if __name__ == "__main__":
    main()
