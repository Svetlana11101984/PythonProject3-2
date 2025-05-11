from unittest.mock import MagicMock, patch

from src.external_api import convert_to_rub


@patch('os.getenv')
@patch('requests.get')
def test_convert_usd_to_rub(mock_get, mock_env):
    mock_env.return_value = 'test_api_key'
    mock_response = MagicMock()
    mock_response.json.return_value = {'rates': {'RUB': 70}}
    mock_get.return_value = mock_response
    transaction = {'amount': 10, 'currency': 'USD'}
    result = convert_to_rub(transaction)
    assert result == 700.0
