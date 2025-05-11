# utils/file_utils.py
import csv
import json

import pandas as pd


def load_json_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def load_csv_data(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)


def load_xlsx_data(file_path):
    df = pd.read_excel(file_path)
    return df.to_dict(orient='records')
