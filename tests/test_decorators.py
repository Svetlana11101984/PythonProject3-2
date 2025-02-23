import os
import pytest
from src.decorators import Log

log = Log("logs/mylog.txt")


@log
def subtract(a, b):
    return a - b


# Очистка/имитация лога перед тестами
@pytest.fixture(autouse=True)
def clean_logs():
    """ Fixture очищает лог файл перед каждым тестом """
    log_file = "logs/mylog.txt"
    if os.path.exists(log_file):
        os.remove(log_file)


def test_log_success():
    result = subtract(10, 5)
    assert result == 5
    with open("logs/mylog.txt") as f:
        contents = f.read()
        assert "Called subtract with args: (10, 5)," in contents


def test_log_error():
    with pytest.raises(TypeError):  # Ожидаем ошибку при неверных типах
        subtract(1, 'a')  # Это приведет к ошибке
    with open("logs/mylog.txt") as f:
        contents = f.read()
        assert "Called subtract with args: (1, 'a')," in contents
