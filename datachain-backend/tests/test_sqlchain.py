import pytest
from unittest.mock import MagicMock
from datachain_backend.sqlchain import SQLChain

def test_connect(mocker):
    # Arrange
    mock_connect = mocker.patch('psycopg2.connect', return_value=MagicMock())
    sqlchain = SQLChain()

    # Act
    sqlchain.connect()

    # Assert
    mock_connect.assert_called_once_with(
        database=sqlchain.database, 
        user=sqlchain.user, 
        password=sqlchain.password, 
        host=sqlchain.host,
        port=sqlchain.port
    )

def test_disconnect(mocker):
    # Arrange
    mock_connection = MagicMock()
    mocker.patch('psycopg2.connect', return_value=mock_connection)
    sqlchain = SQLChain()
    sqlchain.connect()

    # Act
    sqlchain.disconnect()

    # Assert
    mock_connection.close.assert_called_once()

# Add more tests as needed