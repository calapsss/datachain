import unittest
from unittest.mock import patch, MagicMock
from datachain_backend.sqlchain import SQLChain

class TestSQLChain(unittest.TestCase):
    @patch('psycopg2.connect')
    def test_connect(self, mock_connect):
        # Arrange
        mock_connect.return_value = MagicMock()
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

    @patch('psycopg2.connect')
    def test_disconnect(self, mock_connect):
        # Arrange
        mock_connection = MagicMock()
        mock_connect.return_value = mock_connection
        sqlchain = SQLChain()
        sqlchain.connect()

        # Act
        sqlchain.disconnect()

        # Assert
        mock_connection.close.assert_called_once()

    # Add more tests as needed

if __name__ == '__main__':
    unittest.main()