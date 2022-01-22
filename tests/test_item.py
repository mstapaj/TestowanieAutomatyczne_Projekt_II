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
