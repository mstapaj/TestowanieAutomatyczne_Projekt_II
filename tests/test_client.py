import unittest
from assertpy import assert_that
from unittest.mock import Mock
from src.client import Client


class TestClient(unittest.TestCase):

    def setUp(self):
        self.client = Client(1, 'Jan', 'Kowalski', 'example@example.com')

    def test_add_client_to_database(self):
        self.client.add_client_to_database = Mock()
        self.client.add_client_to_database()
        self.client.add_client_to_database.assert_called_once()

    def test_add_client_to_database_two_times(self):
        self.client.add_client_to_database = Mock(side_effect=[None, ValueError])
        self.client.add_client_to_database()
        assert_that(self.client.add_client_to_database).raises(ValueError)
