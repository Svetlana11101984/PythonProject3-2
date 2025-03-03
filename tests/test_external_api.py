from unittest.mock import MagicMock, patch

from src.external_api import convert_to_rub


@patch('os.getenv')
@patch('requests.get')
def test_convert_usd_to_rub(mock_get, mock_env):
    mock_env.return_value = 'test_api_key'

    # Создаем магический объект, который ведет себя как Response
    mock_response = MagicMock()
    mock_response.json.return_value = {'rates': {'USD': 70}}  # Возвращаем нужный результат
    mock_get.return_value = mock_response  # Теперь это объект с методом .json()

    transaction = {'amount': 10, 'currency': 'USD'}
    result = convert_to_rub(transaction)
    assert result == 700.0
