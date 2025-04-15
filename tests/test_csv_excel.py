import unittest
from unittest.mock import mock_open, patch

import pandas as pd

from src.financial_tools.csv_excel import read_csv_transactions, read_excel_transactions


class TestCsvExcel(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open,
           read_data="id,state,date,amount,currency_name,currency_code,from,to,description\n650703,EXECUTED,2023-09-05T11:30:32Z,16210,Sol,PEN,Счет 58803664561298323391,Счет 39745660563456619397,Перевод организации\n" * 100)
    def test_read_csv_transactions(self, mock_file):
        """Тест для проверки функции чтения CSV с лимитом."""
        result = read_csv_transactions(limit=100)
        self.assertEqual(len(result), 100)  # Должно возвращаться ровно 100 записей

    @patch.object(pd, "read_excel", return_value=pd.DataFrame({
        "id": ["650703"],
        "state": ["EXECUTED"],
        "date": ["2023-09-05T11:30:32Z"],
        "amount": ["16210"],
        "currency_name": ["Sol"],
        "currency_code": ["PEN"],
        "from": ["Счет 58803664561298323391"],
        "to": ["Счет 39745660563456619397"],
        "description": ["Перевод организации"]
    }))
    def test_read_excel_transactions(self, mock_read_excel):
        """Тест для проверки функции чтения Excel с лимитом."""
        result = read_excel_transactions(limit=1)  # Вызываем с лимитом 1
        self.assertEqual(len(result), 1)  # Ожидаем ровно 1 запись


if __name__ == "__main__":
    unittest.main()
