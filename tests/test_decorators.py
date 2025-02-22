from unittest.mock import patch
import pytest
from src.decorators import log


@pytest.fixture
def capsys(capsys):
    with patch('decorators.logging'):
        yield capsys


def test_log_decorator_success(capsys):
    @log()
    def add_numbers(x, y):
        return x + y

    assert add_numbers(1, 2) == 3
    captured = capsys.readouterr()
    assert "add_numbers ok" in captured.out


def test_log_decorator_error(capsys):
    @log()
    def divide_numbers(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide_numbers(10, 0)

    captured = capsys.readouterr()
    expected_message = "divide_numbers error: ZeroDivisionError. Inputs: (10, 0), {}"
    assert expected_message in captured.err


def test_log_to_file(tmp_path):
    file_name = tmp_path / "test.log"

    @log(str(file_name))
    def multiply_numbers(x, y):
        return x * y

    multiply_numbers(2, 3)

    with open(file_name, 'r') as f:
        content = f.read()
        assert "multiply_numbers ok" in content
