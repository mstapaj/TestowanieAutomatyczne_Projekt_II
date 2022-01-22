import unittest
from assertpy import assert_that
from unittest.mock import Mock
from src.item import Item
from src.database import Database


class TestItem(unittest.TestCase):

    def setUp(self):
        self.database = Database()
        self.item = Item(1, 'Piłka', 12.5)

    def test_add_item(self):
        self.database.add_item = Mock(return_value='Dodano przedmiot do bazy danych')
        assert_that(self.database.add_item(self.item)).is_equal_to('Dodano przedmiot do bazy danych')

    def test_add_item_wrong_type(self):
        self.database.add_item = Mock(side_effect=ValueError('Podany obiekt nie jest przedmiotem'))
        assert_that(self.database.add_item).raises(ValueError).when_called_with(None)

    def test_add_item_two_time(self):
        self.database.add_item = Mock(side_effect=[None, ValueError('Podany obiekt jest już w bazie')])
        self.database.add_item(self.item)
        assert_that(self.database.add_item).raises(ValueError).when_called_with(self.item)

    def test_edit_item(self):
        self.database.edit_item=Mock(return_value='Pomyślnie edytowano przedmiot')
        assert_that(self.database.edit_item(self.item)).is_equal_to('Pomyślnie edytowano przedmiot')

    def test_edit_item_wrong_type(self):
        self.database.edit_item=Mock(side_effect=ValueError('Podany obiekt nie jest przedmiotem'))
        assert_that(self.database.edit_item).raises(ValueError).when_called_with(None)

    def test_edit_item_two_time(self):
        self.database.edit_item = Mock(side_effect=[None, ValueError('Stary i nowy obiekt są takie same')])
        self.database.edit_item(self.item)
        assert_that(self.database.edit_item).raises(ValueError).when_called_with(self.item)
