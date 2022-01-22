import unittest
from assertpy import assert_that
from src.item import Item
from parameterized import *


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