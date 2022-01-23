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

    def test_show_clients(self):
        self.client.show_clients = Mock(
            return_value=[{'id': 1, "firstname": "Ola", "lastname": "Kot", "email": 'example@example.com'},
                          {'id': 2, "firstname": "Jan", "lastname": "Kowalski", "email": 'exa@example.com'}])
        assert_that(self.client.show_clients()).is_equal_to(
            [{'id': 1, "firstname": "Ola", "lastname": "Kot", "email": 'example@example.com'},
             {'id': 2, "firstname": "Jan", "lastname": "Kowalski", "email": 'exa@example.com'}])

    def test_show_clients_empty(self):
        self.client.show_clients = Mock(return_value=[])
        assert_that(self.client.show_clients()).is_equal_to([])

    def test_show_client_by_id(self):
        self.client.show_client_by_id = Mock(
            return_value={'id': 1, "firstname": "Ola", "lastname": "Kot", "email": 'example@example.com'})
        assert_that(self.client.show_client_by_id(1)).is_equal_to(
            {'id': 1, "firstname": "Ola", "lastname": "Kot", "email": 'example@example.com'})

    def test_show_client_by_id_no_client(self):
        self.client.show_client_by_id = Mock(side_effect=ValueError('Nie istnieje klient o takim id'))
        assert_that(self.client.show_client_by_id).raises(ValueError).when_called_with(5)
