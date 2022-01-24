import unittest
from assertpy import assert_that
from unittest.mock import MagicMock
from src.order import Order
from src.database import Database


class TestOrder(unittest.TestCase):

    def setUp(self):
        self.database = Database()
        self.order = Order(1, 1, self.database)

    def test_add_order_to_database(self):
        self.database.add_order = MagicMock()
        self.order.add_order_to_database()
        self.database.add_order.assert_called_once()

    def test_add_order_to_database_two_times(self):
        self.database.add_order = MagicMock(side_effect=[None, ValueError])
        self.order.add_order_to_database()
        assert_that(self.order.add_order_to_database).raises(ValueError)

    def test_edit_order_in_database(self):
        self.database.edit_order = MagicMock()
        self.order.edit_order_in_database(2, 1, 3)
        self.database.edit_order.assert_called_once()

    def test_edit_order_in_database_two_times(self):
        self.database.edit_order = MagicMock(side_effect=[None, ValueError])
        self.order.edit_order_in_database(1, 1, 3)
        assert_that(self.order.edit_order_in_database).raises(ValueError).when_called_with(1, 1, 3)

    def test_delete_order_from_database(self):
        self.database.delete_order = MagicMock()
        self.order.delete_order_from_database(1)
        self.database.delete_order.assert_called_once()

    def test_delete_order_from_database_two_times(self):
        self.database.delete_order = MagicMock(side_effect=[None, ValueError])
        self.order.delete_order_from_database(1)
        assert_that(self.order.delete_order_from_database).raises(ValueError).when_called_with(1)

    def test_add_item_to_order(self):
        self.database.add_item_to_order = MagicMock()
        self.database.show_item_by_id = MagicMock(return_value={'id': 1, 'name': 'Piłka', 'value': 35.99})
        self.order.add_item_to_order(1)
        self.database.add_item_to_order.assert_called_once_with(1, 1)
