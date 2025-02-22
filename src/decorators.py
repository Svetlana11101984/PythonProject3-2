import logging
import os
from functools import wraps


class log:
    def __init__(self, filename=None):
        self.filename = filename

        if not self.filename:
            logging.basicConfig(level=logging.INFO)
        else:
            if not os.path.exists(os.path.dirname(self.filename)):
                os.makedirs(os.path.dirname(self.filename))

            logging.basicConfig(
                level=logging.INFO,
                format='%(asctime)s - %(levelname)s - %(message)s',
                handlers=[
                    logging.FileHandler(self.filename),
                    logging.StreamHandler()
                ]
            )

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
                logging.info(message)
                return result
            except Exception as e:
                message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                logging.error(message)
                raise

        return wrapper


@log(filename="mylog.txt")
def my_function():
    pass


@log()  # Логи будут отправляться в консоль
def another_function(a, b):
    """Функция деления двух чисел."""
    return a / b


if __name__ == "__main__":
    print(my_function(1, 2))  # Запись логов в файл
    print(another_function(10, 0))  # Запись логов в консоль, проверка обработки ошибки
