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

    def test_edit_client_in_database(self):
        self.client.edit_client_in_database = Mock()
        self.client.edit_client_in_database(2, 1, 'Ola', 'Kot', 'example@example.com')
        self.client.edit_client_in_database.assert_called_once()

    def test_edit_client_in_database_two_times(self):
        self.client.edit_client_in_database = Mock(side_effect=[None, ValueError])
        self.client.edit_client_in_database(1, 1, 'Ola', 'Kot', 'example@exaXXLmple.com')
        assert_that(self.client.edit_client_in_database).raises(ValueError).when_called_with(1, 1, 'Ola', 'Kot',
                                                                                             'example@exaXXLmple.com')

    def test_delete_client_in_database(self):
        self.client.delete_client_in_database = Mock()
        self.client.delete_client_in_database(2)
        self.client.delete_client_in_database.assert_called_once()

    def test_delete_client_in_database_two_times(self):
        self.client.delete_client_in_database = Mock(side_effect=[None, ValueError])
        self.client.delete_client_in_database(2)
        assert_that(self.client.delete_client_in_database).raises(ValueError).when_called_with(2)
