import os
from functools import wraps


class Log:
    def __init__(self, filename):
        self.filename = filename
        # Создаем директорию, если её нет
        os.makedirs(os.path.dirname(os.path.abspath(self.filename)), exist_ok=True)

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Логика записи в файл
            with open(self.filename, 'a') as f:
                f.write(f"Called {func.__name__} with args: {args}, {kwargs}\n")
            return func(*args, **kwargs)
        return wrapper


# Присваиваем экземпляр класса Log, указывая файл лога
log = Log("logs/mylog.txt")


@log
def subtract(a, b):
    return a - b
