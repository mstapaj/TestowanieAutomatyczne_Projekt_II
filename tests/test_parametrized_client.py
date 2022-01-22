import unittest
from assertpy import assert_that
from src.client import Client
from parameterized import *


@parameterized_class(('wrongId', 'wrongFirstname', 'wrongLastname', 'wrongEmail'), [
    ({}, {}, {}, {}),
    ([], [], [], []),
    (True, True, True, True),
    (False, False, False, False),
    (None, None, None, None),
    ("abc", 2, 2, 2),
    ("", -2, -2, -2, -2),
    (3.13, 3.13, 3.12, 3.12),
    (-2.56, -2.82, -3.25, -3.11),
    (-4, -4, -4, -4),
    ("AAAAAAAA", 2, 2, 'AAaaa'),
    ("xxxxxxxx", -10, -10, 'aaaaacos.com')
])
class TestParametrizedItem(unittest.TestCase):

    def test_client_init_wrong_id(self):
        assert_that(Client).raises(ValueError).when_called_with(self.wrongId, 'Jan', 'Kowalski',
                                                                'example@example.com')

    def test_client_init_wrong_firstname(self):
        assert_that(Client).raises(ValueError).when_called_with(1, self.wrongFirstname, 'Kowalski',
                                                                'example@example.com')

    def test_client_init_wrong_lastname(self):
        assert_that(Client).raises(ValueError).when_called_with(1, 'Jan', self.wrongLastname,
                                                                'example@example.com')

    def test_client_init_wrong_email(self):
        assert_that(Client).raises(ValueError).when_called_with(1, 'Jan', 'Kowalski',
                                                                self.wrongEmail)

    def test_client_init_wrong_id_firstname(self):
        assert_that(Client).raises(ValueError).when_called_with(self.wrongId, self.wrongFirstname, 'Kowalski',
                                                                'example@example.com')

    def test_client_init_wrong_firstname_lastname(self):
        assert_that(Client).raises(ValueError).when_called_with(1, self.wrongFirstname, self.wrongLastname,
                                                                'example@example.com')

    def test_client_init_wrong_lastname_email(self):
        assert_that(Client).raises(ValueError).when_called_with(1, 'Jan', self.wrongLastname,
                                                                self.wrongEmail)

    def test_client_init_wrong_id_email(self):
        assert_that(Client).raises(ValueError).when_called_with(self.wrongId, 'Jan', 'Kowalski',
                                                                self.wrongEmail)

    def test_client_init_wrong_id_lastname(self):
        assert_that(Client).raises(ValueError).when_called_with(self.wrongId, 'Jan', self.wrongLastname,
                                                                'example@example.com')

    def test_client_init_wrong_firstname_email(self):
        assert_that(Client).raises(ValueError).when_called_with(1, self.wrongFirstname, 'Kowalski',
                                                                self.wrongEmail)

    def test_client_init_wrong_id_firstname_lastname(self):
        assert_that(Client).raises(ValueError).when_called_with(self.wrongId, self.wrongFirstname, self.wrongLastname,
                                                                'example@example.com')

    def test_client_init_wrong_firstname_lastname_email(self):
        assert_that(Client).raises(ValueError).when_called_with(1,self.wrongFirstname, self.wrongLastname,
                                                                self.wrongEmail)

    def test_client_init_wrong_id_lastname_email(self):
        assert_that(Client).raises(ValueError).when_called_with(self.wrongId, 'Jan', self.wrongLastname,
                                                                self.wrongEmail)

    def test_client_init_wrong_id_firstname_email(self):
        assert_that(Client).raises(ValueError).when_called_with(self.wrongId, self.wrongFirstname, 'Kowalski',
                                                                self.wrongEmail)

    def test_client_init_wrong_id_firstname_lastname_email(self):
        assert_that(Client).raises(ValueError).when_called_with(self.wrongId, self.wrongFirstname, self.wrongLastname,
                                                                self.wrongEmail)


