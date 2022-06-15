import unittest
from assertpy import assert_that
from src.order import Order
from parameterized import parameterized_class


@parameterized_class(('wrongId', 'wrongIdClient'), [
    ({}, {}),
    ([], []),
    (True, True),
    (False, False),
    (None, None),
    ("abc", "abc"),
    ("", ""),
    (3.13, 3.13),
    (-2.56, -2.82),
    (-4, -4)
])
class TestParametrizedOrder(unittest.TestCase):

    def test_order_init_wrong_id(self):
        assert_that(Order).raises(ValueError).when_called_with(self.wrongId, 2)

    def test_order_init_wrong_id_client(self):
        assert_that(Order).raises(ValueError).when_called_with(1, self.wrongIdClient)

    def test_order_init_wrong_id_id_client(self):
        assert_that(Order).raises(ValueError).when_called_with(self.wrongId, self.wrongIdClient)


@parameterized_class(('wrongId', 'wrongNewId', 'wrongClientId'), [
    ({}, {}, {}),
    ([], [], []),
    (True, True, True),
    (False, False, False),
    (None, 'AA', 'AA'),
    ("abc", "abc", "abc"),
    ("", "", ""),
    (3.13, 3.13, 3.13),
    (-2.56, -2.82, -2.56),
    (-4, -4, -4)
])
class TestParametrizedEditOrder(unittest.TestCase):

    def setUp(self):
        self.temp = Order(1, 1)

    def test_edit_order_in_database_wrong_id(self):
        assert_that(self.temp.edit_order_in_database).raises(ValueError).when_called_with(self.wrongId, 2, 2)

    def test_edit_order_in_database_wrong_new_id(self):
        assert_that(self.temp.edit_order_in_database).raises(ValueError).when_called_with(1, self.wrongNewId, 2)

    def test_edit_order_in_database_wrong_client_id(self):
        assert_that(self.temp.edit_order_in_database).raises(ValueError).when_called_with(1, 2, self.wrongClientId)

    def test_edit_order_in_database_wrong_id_new_id(self):
        assert_that(self.temp.edit_order_in_database).raises(ValueError).when_called_with(self.wrongId, self.wrongNewId,
                                                                                          2)

    def test_edit_order_in_database_wrong_new_id_client_id(self):
        assert_that(self.temp.edit_order_in_database).raises(ValueError).when_called_with(1, self.wrongNewId,
                                                                                          self.wrongClientId)

    def test_edit_order_in_database_wrong_id_client_id(self):
        assert_that(self.temp.edit_order_in_database).raises(ValueError).when_called_with(self.wrongId, 2,
                                                                                          self.wrongClientId)

    def test_edit_order_in_database_wrong_id_new_id_client_id(self):
        assert_that(self.temp.edit_order_in_database).raises(ValueError).when_called_with(self.wrongId, self.wrongNewId,
                                                                                          self.wrongClientId)

    def test_delete_order_from_database(self):
        assert_that(self.temp.delete_order_from_database).raises(ValueError).when_called_with(self.wrongId)

    def test_add_item_to_order(self):
        assert_that(self.temp.add_item_to_order).raises(ValueError).when_called_with(self.wrongId)

    def test_delete_item_from_order(self):
        assert_that(self.temp.delete_item_from_order).raises(ValueError).when_called_with(self.wrongId)

    def test_show_items_by_order_id(self):
        assert_that(self.temp.show_items_by_order_id).raises(ValueError).when_called_with(self.wrongId)
