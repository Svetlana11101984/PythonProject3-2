from unittest.mock import patch

import pytest

from src.utils import read_json_file


@pytest.fixture
def mock_json_file(tmpdir):
    p = tmpdir.join("mock.json")
    p.write('[{"amount": 100, "currency": "USD"}]')
    return str(p)


@patch('json.load')
def test_read_json_file(mock_load, mock_json_file):
    mock_load.return_value = [{'amount': 100, 'currency': 'USD'}]
    result = read_json_file(mock_json_file)
    assert result == [{'amount': 100, 'currency': 'USD'}]
