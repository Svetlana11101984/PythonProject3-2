# Виджет банковских операций клиента

Этот проект представляет собой инструмент для обработки и анализа данных о банковских операциях клиентов. Он включает функции фильтрации и сортировки данных по различным критериям.

## Установка

Для установки проекта необходимо клонировать репозиторий и установить зависимости:

## Тестирование
Покрытие кода
Мы стремимся поддерживать высокий уровень покрытия кода тестами. Для оценки покрытия используется инструмент coverage.py. Текущий уровень покрытия составляет XX%.

Запуск тестов
Для запуска тестов выполните следующую команду:


pip install -r requirements.txt
pytest
Отчёт о покрытии
Чтобы получить отчёт о покрытии кода, выполните:


coverage run -m pytest
coverage report
Для создания HTML-отчёта:


coverage html
Откройте файл htmlcov/index.html в браузере, чтобы посмотреть детальный отчёт.

```bash
git clone https://https://github.com/Svetlana11101984/bank_project
cd bank_project

## Модуль `generators`
Этот модуль содержит функции для работы с данными транзакций. Он включает в себя три основных функции:

### `filter_by_currency`
Функция-фильтр, которая позволяет выбрать транзакции по определенной валюте.

Пример использования:
```python
transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
    # другие транзакции...
]

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))

### transaction_descriptions
Генератор, который возвращает описания транзакций по очереди.

Пример использования:


descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))

### card_number_generator
Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX.

Пример использования:


for card_number in card_number_generator(1, 10):
    print(card_number)