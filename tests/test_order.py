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
        self.database.add_order=MagicMock()
        self.order.add_order_to_database()
        self.database.add_order.assert_called_once()

    def test_add_order_to_database_two_times(self):
        self.database.add_order=MagicMock(side_effect=[None, ValueError])
        self.order.add_order_to_database()
        assert_that(self.database.add_order).raises(ValueError)
