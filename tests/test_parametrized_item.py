import unittest
from assertpy import assert_that
from src.item import Item
from parameterized import parameterized_class


@parameterized_class(('wrongId', 'wrongName', 'wrongValue'), [
    ({}, {}, {}),
    ([], [], []),
    (True, True, True),
    (False, False, False),
    (None, None, None),
    ("abc", 2, "abc"),
    ("", -2, ""),
    (3.13, 3.13, 'def'),
    (-2.56, -2.82, -3.25),
    (-4, -4, -4)
])
class TestParametrizedItem(unittest.TestCase):

    def test_item_init_wrong_id(self):
        assert_that(Item).raises(ValueError).when_called_with(self.wrongId, 'Piłka', 40)

    def test_item_init_wrong_name(self):
        assert_that(Item).raises(ValueError).when_called_with(1, self.wrongName, 40)

    def test_item_init_wrong_value(self):
        assert_that(Item).raises(ValueError).when_called_with(1, 'Piłka', self.wrongValue)

    def test_item_init_wrong_id_name(self):
        assert_that(Item).raises(ValueError).when_called_with(self.wrongId, self.wrongName, 40)

    def test_item_init_wrong_name_value(self):
        assert_that(Item).raises(ValueError).when_called_with(1, self.wrongName, self.wrongValue)

    def test_item_init_wrong_id_value(self):
        assert_that(Item).raises(ValueError).when_called_with(self.wrongId, 'Piłka', self.wrongValue)

    def test_item_init_wrong_id_name_value(self):
        assert_that(Item).raises(ValueError).when_called_with(self.wrongId, self.wrongName, self.wrongValue)


@parameterized_class(('wrongId', 'wrongNewId', 'wrongName', 'wrongValue'), [
    ({}, {}, {}, {}),
    ([], [], [], []),
    (True, True, True, True),
    (False, False, False, False),
    ("abc", 'abc', 2, "abc"),
    ("", '', -2, ""),
    (3.13, 2.12, 3.13, 'def'),
    (-2.56, -2.12, -2.82, -3.25),
    (-4, -4, -4, -4),
    (None, 2.1, 2, 'aaa')
])
class TestParametrizedEditItemInDatabase(unittest.TestCase):

    def setUp(self):
        self.temp = Item(1, 'Piłka', 2.5)

    def test_edit_item_in_database_wrong_id(self):
        assert_that(self.temp.edit_item_in_database).raises(ValueError).when_called_with(self.wrongId, 4, 'Latarka',
                                                                                         18.5)

    def test_edit_item_in_database_wrong_new_id(self):
        assert_that(self.temp.edit_item_in_database).raises(ValueError).when_called_with(1, self.wrongNewId, 'Latarka',
                                                                                         18.5)

    def test_edit_item_in_database_wrong_name(self):
        assert_that(self.temp.edit_item_in_database).raises(ValueError).when_called_with(1, 4, self.wrongName,
                                                                                         18.5)

    def test_edit_item_in_database_wrong_value(self):
        assert_that(self.temp.edit_item_in_database).raises(ValueError).when_called_with(1, 4, 'Latarka',
                                                                                         self.wrongValue)

    def test_edit_item_in_database_wrong_id_new_id(self):
        assert_that(self.temp.edit_item_in_database).raises(ValueError).when_called_with(self.wrongId, self.wrongNewId,
                                                                                         'Latarka',
                                                                                         18.5)

    def test_edit_item_in_database_wrong_new_id_name(self):
        assert_that(self.temp.edit_item_in_database).raises(ValueError).when_called_with(1, self.wrongNewId,
                                                                                         self.wrongName,
                                                                                         18.5)

    def test_edit_item_in_database_wrong_name_value(self):
        assert_that(self.temp.edit_item_in_database).raises(ValueError).when_called_with(1, 4, self.wrongName,
                                                                                         self.wrongValue)

    def test_edit_item_in_database_wrong_id_value(self):
        assert_that(self.temp.edit_item_in_database).raises(ValueError).when_called_with(self.wrongId, 4, 'Latarka',
                                                                                         self.wrongValue)

    def test_edit_item_in_database_wrong_id_name(self):
        assert_that(self.temp.edit_item_in_database).raises(ValueError).when_called_with(self.wrongId, 4,
                                                                                         self.wrongName,
                                                                                         18.5)

    def test_edit_item_in_database_wrong_new_id_value(self):
        assert_that(self.temp.edit_item_in_database).raises(ValueError).when_called_with(1, self.wrongNewId, 'Latarka',
                                                                                         self.wrongValue)

    def test_edit_item_in_database_wrong_id_new_id_name(self):
        assert_that(self.temp.edit_item_in_database).raises(ValueError).when_called_with(self.wrongId, self.wrongNewId,
                                                                                         self.wrongName,
                                                                                         18.5)

    def test_edit_item_in_database_wrong_new_id_name_value(self):
        assert_that(self.temp.edit_item_in_database).raises(ValueError).when_called_with(1, self.wrongNewId,
                                                                                         self.wrongName,
                                                                                         self.wrongValue)

    def test_edit_item_in_database_wrong_id_name_value(self):
        assert_that(self.temp.edit_item_in_database).raises(ValueError).when_called_with(self.wrongId, 4,
                                                                                         self.wrongName,
                                                                                         self.wrongValue)

    def test_edit_item_in_database_wrong_id_new_id_value(self):
        assert_that(self.temp.edit_item_in_database).raises(ValueError).when_called_with(self.wrongId, self.wrongNewId,
                                                                                         'Latarka',
                                                                                         self.wrongValue)

    def test_edit_item_in_database_wrong_id_new_id_name_value(self):
        assert_that(self.temp.edit_item_in_database).raises(ValueError).when_called_with(self.wrongId, self.wrongNewId,
                                                                                         self.wrongName,
                                                                                         self.wrongValue)

    def test_delete_item_in_database(self):
        assert_that(self.temp.delete_item_in_database).raises(ValueError).when_called_with(self.wrongId)

    def test_show_item_by_id(self):
        assert_that(self.temp.show_item_by_id).raises(ValueError).when_called_with(self.wrongId)

    def test_show_items_by_name(self):
        assert_that(self.temp.show_items_by_name).raises(ValueError).when_called_with(self.wrongName)
