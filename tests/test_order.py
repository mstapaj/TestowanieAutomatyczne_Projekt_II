import unittest
from assertpy import assert_that, add_extension
from unittest.mock import MagicMock, create_autospec, Mock
from src.order import Order
from src.database import Database


def is_each_result_has_keys_id_name_value(self):
    for i in self.val:
        if 'id' not in i or 'name' not in i or 'value' not in i:
            return self.error('Przedmioty w zamówieniu nie mają wszystkich wartości')
    return self


add_extension(is_each_result_has_keys_id_name_value)


class TestOrder(unittest.TestCase):

    def setUp(self):
        self.database = Database()
        self.order = Order(1, 1, self.database)

    def test_order_not_none(self):
        assert_that(self.order).is_not_none()

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

    def test_edit_order_in_database_too_many_args(self):
        mock_function = create_autospec(self.database.edit_order)
        assert_that(mock_function).raises(TypeError).when_called_with(1, 1, 1, 3)

    def test_edit_order_in_database_too_few_args(self):
        mock_function = create_autospec(self.database.edit_order)
        assert_that(mock_function).raises(TypeError).when_called_with(1)

    def test_delete_order_from_database(self):
        self.database.delete_order = MagicMock()
        self.order.delete_order_from_database(1)
        self.database.delete_order.assert_called_once()

    def test_delete_order_from_database_two_times(self):
        self.database.delete_order = MagicMock(side_effect=[None, ValueError])
        self.order.delete_order_from_database(1)
        assert_that(self.order.delete_order_from_database).raises(ValueError).when_called_with(1)

    def test_delete_order_from_database_too_many_args(self):
        mock_function = create_autospec(self.database.delete_order)
        assert_that(mock_function).raises(TypeError).when_called_with(1, 1, 1, 3)

    def test_delete_order_from_database_too_few_args(self):
        mock_function = create_autospec(self.database.delete_order)
        assert_that(mock_function).raises(TypeError).when_called_with()

    def test_add_item_to_order(self):
        self.database.add_item_to_order = MagicMock()
        self.database.show_item_by_id = MagicMock(return_value={'id': 1, 'name': 'Piłka', 'value': 35.99})
        self.order.add_item_to_order(1)
        self.database.add_item_to_order.assert_called_once_with(1, 1)

    def test_delete_item_from_order(self):
        self.database.delete_item_from_order = MagicMock()
        self.database.show_item_by_id = MagicMock(return_value={'id': 1, 'name': 'Piłka', 'value': 35.99})
        self.order.delete_item_from_order(1)
        self.database.delete_item_from_order.assert_called_once_with(1, 1)

    def test_delete_item_from_order_two_times(self):
        self.database.delete_item_from_order = MagicMock(side_effect=[None, ValueError])
        self.order.delete_item_from_order(1)
        assert_that(self.order.delete_item_from_order).raises(ValueError).when_called_with(1)

    def test_show_items_by_order_id(self):
        self.database.show_items_by_order_id = Mock(
            return_value=[{'id': 1, 'name': 'Piłka Nike', 'value': 89.99}])
        assert_that(self.order.show_items_by_order_id(1)).is_equal_to(
            [{'id': 1, 'name': 'Piłka Nike', 'value': 89.99}])

    def test_show_items_by_order_id_many(self):
        self.database.show_items_by_order_id = Mock(
            return_value=[{'id': 1, 'name': 'Piłka Nike', 'value': 89.99},
                          {'id': 2, 'name': 'Piłka Adidas', 'value': 69.99},
                          {'id': 3, 'name': 'Buty Nike', 'value': 269.99}])
        assert_that(self.order.show_items_by_order_id(1)).is_equal_to(
            [{'id': 1, 'name': 'Piłka Nike', 'value': 89.99},
             {'id': 2, 'name': 'Piłka Adidas', 'value': 69.99},
             {'id': 3, 'name': 'Buty Nike', 'value': 269.99}])

    def test_show_items_by_order_id_many_custom_matcher(self):
        self.database.show_items_by_order_id = Mock(
            return_value=[{'id': 1, 'name': 'Piłka Nike', 'value': 89.99},
                          {'id': 2, 'name': 'Piłka Adidas', 'value': 69.99},
                          {'id': 3, 'name': 'Buty Nike', 'value': 269.99}])
        assert_that(self.order.show_items_by_order_id(1)).is_each_result_has_keys_id_name_value()

    # Test nie przechodzi, ponieważ w przedmiotach nie ma wszystkich wymaganych wartości
    # def test_show_items_by_order_id_many_custom_matcher_error(self):
    #     self.database.show_items_by_order_id = Mock(
    #         return_value=[{'id': 1, 'name': 'Piłka Nike', 'value': 89.99},
    #                       {'id': 2, 'name': 'Piłka Adidas'},
    #                       {'name': 'Buty Nike', 'value': 269.99}])
    #     assert_that(self.order.show_items_by_order_id(1)).is_each_result_has_keys_id_name_value()

    def test_show_items_by_order_id_many_length(self):
        self.database.show_items_by_order_id = Mock(
            return_value=[{'id': 1, 'name': 'Piłka Nike', 'value': 89.99},
                          {'id': 2, 'name': 'Piłka Adidas', 'value': 69.99},
                          {'id': 3, 'name': 'Buty Nike', 'value': 269.99}])
        assert_that(self.order.show_items_by_order_id(1)).is_length(3)

    def test_show_items_by_order_id_empty(self):
        self.database.show_items_by_order_id = Mock(return_value=[])
        assert_that(self.order.show_items_by_order_id(3)).is_empty()

    def test_show_items_by_order_id_wrong_id(self):
        self.database.show_items_by_order_id = Mock(side_effect=ValueError)
        assert_that(self.order.show_items_by_order_id).raises(ValueError).when_called_with(4)
