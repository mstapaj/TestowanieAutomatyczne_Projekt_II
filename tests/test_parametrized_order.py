import unittest
from assertpy import assert_that
from src.order import Order
from parameterized import *


@parameterized_class(('wrongPositiveInt', 'wrongPositiveInt'), [
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
        assert_that(Order).raises(ValueError).when_called_with(self.wrongPositiveInt, 2)

    def test_order_init_wrong_id_client(self):
        assert_that(Order).raises(ValueError).when_called_with(1, self.wrongPositiveInt)

    def test_order_init_wrong_id_id_client(self):
        assert_that(Order).raises(ValueError).when_called_with(self.wrongPositiveInt, self.wrongPositiveInt)
