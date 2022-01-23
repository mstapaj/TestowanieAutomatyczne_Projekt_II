import unittest
from assertpy import assert_that
from unittest.mock import Mock
from src.item import Item


class TestItem(unittest.TestCase):

    def setUp(self):
        self.item = Item(1, 'Piłka', 12.5)

    def test_add_item_to_database(self):
        self.item.add_item_to_database = Mock(return_value='Dodano przedmiot do bazy danych')
        assert_that(self.item.add_item_to_database()).is_equal_to('Dodano przedmiot do bazy danych')

    def test_add_item_to_database_two_time(self):
        self.item.add_item_to_database = Mock(side_effect=[None, ValueError('Podany obiekt jest już w bazie')])
        self.item.add_item_to_database()
        assert_that(self.item.add_item_to_database).raises(ValueError)

    def test_edit_item_in_database(self):
        self.item.edit_item_in_database = Mock(return_value='Pomyślnie edytowano przedmiot')
        assert_that(self.item.edit_item_in_database(2, 3, 'Latarka', 20.99)).is_equal_to(
            'Pomyślnie edytowano przedmiot')

    def test_edit_item_in_database_two_time(self):
        self.item.edit_item_in_database = Mock(side_effect=[None, ValueError('Stary i nowy obiekt są identyczne')])
        self.item.edit_item_in_database(2, 2, 'Latarka', 20.99)
        assert_that(self.item.edit_item_in_database).raises(ValueError).when_called_with(2, 2, 'Latarka', 20.99)

    def test_delete_item_in_database(self):
        self.item.delete_item_in_database = Mock(return_value='Pomyślnie usunięto przedmiot')
        assert_that(self.item.delete_item_in_database(2)).is_equal_to(
            'Pomyślnie usunięto przedmiot')

    def test_delete_item_in_database_two_time(self):
        self.item.delete_item_in_database = Mock(side_effect=[None, ValueError('Nie istnieje przedmiot o takim id')])
        self.item.delete_item_in_database(2)
        assert_that(self.item.delete_item_in_database).raises(ValueError).when_called_with(2)

    def test_show_items_from_database(self):
        self.item.show_items_from_database = Mock(
            return_value=[{'id': 1, 'name': 'Piłka', 'value': 35.99}, {'id': 2, 'name': 'Rower', 'value': 399.99}])
        assert_that(self.item.show_items_from_database()).is_equal_to(
            [{'id': 1, 'name': 'Piłka', 'value': 35.99}, {'id': 2, 'name': 'Rower', 'value': 399.99}])

    def test_show_items_from_database_empty(self):
        self.item.show_items_from_database = Mock(return_value=[])
        assert_that(self.item.show_items_from_database()).is_equal_to([])
