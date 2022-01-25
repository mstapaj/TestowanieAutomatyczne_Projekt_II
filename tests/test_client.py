import unittest
from assertpy import assert_that
from unittest.mock import Mock
from src.client import Client
from src.database import Database


class TestClient(unittest.TestCase):

    def setUp(self):
        self.database = Database()
        self.client = Client(1, 'Jan', 'Kowalski', 'example@example.com', self.database)

    def test_add_client_to_database(self):
        self.database.add_client = Mock()
        self.client.add_client_to_database()
        self.database.add_client.assert_called_once()

    def test_add_client_to_database_two_times(self):
        self.database.add_client = Mock(side_effect=[None, ValueError])
        self.client.add_client_to_database()
        assert_that(self.client.add_client_to_database).raises(ValueError)

    def test_edit_client_in_database(self):
        self.database.edit_client = Mock()
        self.client.edit_client_in_database(2, 1, 'Ola', 'Kot', 'example@example.com')
        self.database.edit_client.assert_called_once()

    def test_edit_client_in_database_two_times(self):
        self.database.edit_client = Mock(side_effect=[None, ValueError])
        self.client.edit_client_in_database(1, 1, 'Ola', 'Kot', 'example@exaXXLmple.com')
        assert_that(self.client.edit_client_in_database).raises(ValueError).when_called_with(1, 1, 'Ola', 'Kot',
                                                                                             'example@exaXXLmple.com')

    def test_delete_client_in_database(self):
        self.database.delete_client = Mock()
        self.client.delete_client_in_database(2)
        self.database.delete_client.assert_called_once()

    def test_delete_client_in_database_two_times(self):
        self.database.delete_client = Mock(side_effect=[None, ValueError])
        self.client.delete_client_in_database(2)
        assert_that(self.client.delete_client_in_database).raises(ValueError).when_called_with(2)

    def test_show_clients(self):
        self.database.show_clients = Mock(
            return_value=[{'id': 1, "firstname": "Ola", "lastname": "Kot", "email": 'example@example.com'},
                          {'id': 2, "firstname": "Jan", "lastname": "Kowalski", "email": 'exa@example.com'}])
        assert_that(self.client.show_clients()).is_equal_to(
            [{'id': 1, "firstname": "Ola", "lastname": "Kot", "email": 'example@example.com'},
             {'id': 2, "firstname": "Jan", "lastname": "Kowalski", "email": 'exa@example.com'}])

    def test_show_clients_empty(self):
        self.database.show_clients = Mock(return_value=[])
        assert_that(self.client.show_clients()).is_equal_to([])

    def test_show_client_by_id(self):
        self.database.show_client_by_id = Mock(
            return_value={'id': 1, "firstname": "Ola", "lastname": "Kot", "email": 'example@example.com'})
        assert_that(self.client.show_client_by_id(1)).is_equal_to(
            {'id': 1, "firstname": "Ola", "lastname": "Kot", "email": 'example@example.com'})

    def test_show_client_by_id_no_client(self):
        self.database.show_client_by_id = Mock(side_effect=ValueError('Nie istnieje klient o takim id'))
        assert_that(self.client.show_client_by_id).raises(ValueError).when_called_with(5)

    def test_show_clients_by_firstname_and_lastname(self):
        self.database.show_clients_by_firstname_and_lastname = Mock(
            return_value=[{'id': 1, "firstname": "Michał", "lastname": "Kowal", "email": 'example@example.com'},
                          {'id': 2, "firstname": "Jan", "lastname": "Kowalski", "email": 'exa@example.com'}])
        assert_that(self.client.show_clients_by_firstname_and_lastname('Kowal')).is_equal_to(
            [{'id': 1, "firstname": "Michał", "lastname": "Kowal", "email": 'example@example.com'},
             {'id': 2, "firstname": "Jan", "lastname": "Kowalski", "email": 'exa@example.com'}])

    def test_show_clients_by_firstname_and_lastname_empty(self):
        self.database.show_clients_by_firstname_and_lastname = Mock(return_value=[])
        assert_that(self.client.show_clients_by_firstname_and_lastname('abascasd')).is_equal_to([])

    def test_add_order_to_client(self):
        self.database.add_order_to_client = Mock()
        self.client.add_order_to_client(1)
        self.database.add_order_to_client.assert_called_once_with(1, 1)

    def test_add_order_to_client_two_times(self):
        self.database.add_order_to_client = Mock(side_effect=[None, ValueError])
        self.client.add_order_to_client(1)
        assert_that(self.client.add_order_to_client).raises(ValueError).when_called_with(1)

    def test_delete_order_from_client(self):
        self.database.delete_order_from_client = Mock()
        self.client.delete_order_from_client(1)
        self.database.delete_order_from_client.assert_called_once_with(1, 1)

    def test_delete_order_from_client_two_times(self):
        self.database.delete_order_from_client = Mock(side_effect=[None, ValueError])
        self.client.delete_order_from_client(1)
        assert_that(self.client.delete_order_from_client).raises(ValueError).when_called_with(1)

    def test_show_orders_by_client_id(self):
        self.database.show_orders_by_client_id = Mock(
            return_value=[{'id': 1, 'items': [{'id': 1, 'name': 'Piłka Nike', 'value': 89.99}]}])
        assert_that(self.client.show_orders_by_client_id(1)).is_equal_to(
            [{'id': 1, 'items': [{'id': 1, 'name': 'Piłka Nike', 'value': 89.99}]}, {'id': 2, 'items': [
                {'id': 2, 'name': 'Piłka Adidas', 'value': 69.99}, {'id': 3, 'name': 'Buty Nike', 'value': 269.99}]}])

    def test_show_orders_by_client_id_many(self):
        self.database.show_orders_by_client_id = Mock(
            return_value=[{'id': 1, 'items': [{'id': 1, 'name': 'Piłka Nike', 'value': 89.99}]}, {'id': 2, 'items': [
                {'id': 2, 'name': 'Piłka Adidas', 'value': 69.99}, {'id': 3, 'name': 'Buty Nike', 'value': 269.99}]}])
        assert_that(self.client.show_orders_by_client_id(2)).is_equal_to(
            [{'id': 1, 'items': [{'id': 1, 'name': 'Piłka Nike', 'value': 89.99}]}, {'id': 2, 'items': [
                {'id': 2, 'name': 'Piłka Adidas', 'value': 69.99}, {'id': 3, 'name': 'Buty Nike', 'value': 269.99}]}])

    def test_show_orders_by_client_id_empty(self):
        self.database.show_orders_by_client_id = Mock(return_value=[])
        assert_that(self.client.show_orders_by_client_id(3)).is_equal_to([])

    def test_show_orders_by_client_id_wrong_id(self):
        self.database.show_orders_by_client_id = Mock(side_effect=ValueError)
        assert_that(self.client.show_orders_by_client_id).raises(ValueError).when_called_with(4)
