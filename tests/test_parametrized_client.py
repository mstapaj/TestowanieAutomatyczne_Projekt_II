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
        assert_that(Client).raises(ValueError).when_called_with(1, self.wrongFirstname, self.wrongLastname,
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


@parameterized_class(('wrongId', 'wrongNewId', 'wrongFirstname', 'wrongLastname', 'wrongEmail'), [
    ({}, {}, {}, {}, {}),
    ([], [], [], [], []),
    (True, True, True, True, True),
    (False, False, False, False, False),
    (None, "abc", 87, 87, 123),
    ("abc", "abc", 2, 2, 2),
    ("", "", -2, -2, -2, -2),
    (3.13, 3.13, 3.13, 3.12, 3.12),
    (-2.56, -2.41, -2.82, -3.25, -3.11),
    (-4, -4, -4, -4, -4),
    ("AAAAAAAA", "AAAAAAAA", 2, 2, 'AAaaa'),
    ("xxxxxxxx", "xxxxxxxx", -10, -10, 'aaaaacos.com')
])
class TestParametrizedEditClientInDatabase(unittest.TestCase):
    def setUp(self):
        self.temp = Client(1, 'Jan', 'Kowalski', 'example@example.com')

    def test_edit_client_in_database_wrong_id(self):
        assert_that(self.temp.edit_client_in_database).raises(ValueError).when_called_with(self.wrongId, 3, 'Ola',
                                                                                           'Kot', 'exa@example.com')

    def test_edit_client_in_database_wrong_new_id(self):
        assert_that(self.temp.edit_client_in_database).raises(ValueError).when_called_with(1, self.wrongNewId, 'Ola',
                                                                                           'Kot', 'exa@example.com')

    def test_edit_client_in_database_wrong_firstname(self):
        assert_that(self.temp.edit_client_in_database).raises(ValueError).when_called_with(1, 3, self.wrongFirstname,
                                                                                           'Kot', 'exa@example.com')

    def test_edit_client_in_database_wrong_lastname(self):
        assert_that(self.temp.edit_client_in_database).raises(ValueError).when_called_with(1, 3, 'Ola',
                                                                                           self.wrongLastname,
                                                                                           'exa@example.com')

    def test_edit_client_in_database_wrong_email(self):
        assert_that(self.temp.edit_client_in_database).raises(ValueError).when_called_with(1, 3, 'Ola', 'Kot',
                                                                                           self.wrongEmail)

    def test_edit_client_in_database_wrong_id_new_id(self):
        assert_that(self.temp.edit_client_in_database).raises(ValueError).when_called_with(self.wrongId,
                                                                                           self.wrongNewId, 'Ola',
                                                                                           'Kot',
                                                                                           'exa@example.com')

    def test_edit_client_in_database_wrong_new_id_firstname(self):
        assert_that(self.temp.edit_client_in_database).raises(ValueError).when_called_with(1, self.wrongNewId,
                                                                                           self.wrongFirstname, 'Kot',
                                                                                           'exa@example.com')

    def test_edit_client_in_database_wrong_firstname_lastname(self):
        assert_that(self.temp.edit_client_in_database).raises(ValueError).when_called_with(1, 3, self.wrongFirstname,
                                                                                           self.wrongLastname,
                                                                                           'exa@example.com')

    def test_edit_client_in_database_wrong_lastname_email(self):
        assert_that(self.temp.edit_client_in_database).raises(ValueError).when_called_with(1, 3, 'Jan',
                                                                                           self.wrongLastname,
                                                                                           self.wrongEmail)

    def test_edit_client_in_database_wrong_id_lastname(self):
        assert_that(self.temp.edit_client_in_database).raises(ValueError).when_called_with(self.wrongId,
                                                                                           3, 'Ola',
                                                                                           self.wrongLastname,
                                                                                           'exa@example.com')

    def test_edit_client_in_database_wrong_new_id_lastname(self):
        assert_that(self.temp.edit_client_in_database).raises(ValueError).when_called_with(1, self.wrongNewId,
                                                                                           'Jan', self.wrongLastname,
                                                                                           'exa@example.com')

    def test_edit_client_in_database_wrong_firstname_email(self):
        assert_that(self.temp.edit_client_in_database).raises(ValueError).when_called_with(1, 3, self.wrongFirstname,
                                                                                           'Kot',
                                                                                           self.wrongEmail)

    def test_edit_client_in_database_wrong_new_id_email(self):
        assert_that(self.temp.edit_client_in_database).raises(ValueError).when_called_with(1, self.wrongNewId, 'Jan',
                                                                                           'Kot',
                                                                                           self.wrongEmail)

    def test_edit_client_in_database_wrong_id_email(self):
        assert_that(self.temp.edit_client_in_database).raises(ValueError).when_called_with(self.wrongId, 3, 'Jan',
                                                                                           'Kot',
                                                                                           self.wrongEmail)

    def test_edit_client_in_database_wrong_id_firstname(self):
        assert_that(self.temp.edit_client_in_database).raises(ValueError).when_called_with(self.wrongId, 3,
                                                                                           self.wrongFirstname,
                                                                                           'Kot',
                                                                                           'exa@example.com')

    def test_edit_client_in_database_wrong_id_new_id_firstname(self):
        assert_that(self.temp.edit_client_in_database).raises(ValueError).when_called_with(self.wrongId,
                                                                                           self.wrongNewId,
                                                                                           self.wrongFirstname,
                                                                                           'Kot',
                                                                                           'exa@example.com')

    def test_edit_client_in_database_wrong_new_id_firstname_lastname(self):
        assert_that(self.temp.edit_client_in_database).raises(ValueError).when_called_with(1, self.wrongNewId,
                                                                                           self.wrongFirstname,
                                                                                           self.wrongLastname,
                                                                                           'exa@example.com')

    def test_edit_client_in_database_wrong_firstname_lastname_email(self):
        assert_that(self.temp.edit_client_in_database).raises(ValueError).when_called_with(1, 3, self.wrongFirstname,
                                                                                           self.wrongLastname,
                                                                                           self.wrongEmail)

    def test_edit_client_in_database_wrong_id_lastname_email(self):
        assert_that(self.temp.edit_client_in_database).raises(ValueError).when_called_with(self.wrongId, 3, 'Jan',
                                                                                           self.wrongLastname,
                                                                                           self.wrongEmail)

    def test_edit_client_in_database_wrong_id_new_id_lastname(self):
        assert_that(self.temp.edit_client_in_database).raises(ValueError).when_called_with(self.wrongId,
                                                                                           self.wrongNewId, 'Ola',
                                                                                           self.wrongLastname,
                                                                                           'exa@example.com')

    def test_edit_client_in_database_wrong_new_id_lastname_email(self):
        assert_that(self.temp.edit_client_in_database).raises(ValueError).when_called_with(1, self.wrongNewId,
                                                                                           'Jan', self.wrongLastname,
                                                                                           self.wrongEmail)

    def test_edit_client_in_database_wrong_new_id_firstname_email(self):
        assert_that(self.temp.edit_client_in_database).raises(ValueError).when_called_with(1, self.wrongNewId,
                                                                                           self.wrongFirstname,
                                                                                           'Kot',
                                                                                           self.wrongEmail)

    def test_edit_client_in_database_wrong_id_new_id_email(self):
        assert_that(self.temp.edit_client_in_database).raises(ValueError).when_called_with(self.wrongId,
                                                                                           self.wrongNewId, 'Jan',
                                                                                           'Kot',
                                                                                           self.wrongEmail)

    def test_edit_client_in_database_wrong_id_firstname_email(self):
        assert_that(self.temp.edit_client_in_database).raises(ValueError).when_called_with(self.wrongId, 3,
                                                                                           self.wrongFirstname,
                                                                                           'Kot',
                                                                                           self.wrongEmail)

    def test_edit_client_in_database_wrong_id_firstname_lastname(self):
        assert_that(self.temp.edit_client_in_database).raises(ValueError).when_called_with(self.wrongId, 3,
                                                                                           self.wrongFirstname,
                                                                                           self.wrongLastname,
                                                                                           'exa@example.com')

    def test_edit_client_in_database_wrong_id_new_id_firstname_lastname(self):
        assert_that(self.temp.edit_client_in_database).raises(ValueError).when_called_with(self.wrongId,
                                                                                           self.wrongNewId,
                                                                                           self.wrongFirstname,
                                                                                           self.wrongLastname,
                                                                                           'exa@example.com')

    def test_edit_client_in_database_wrong_new_id_firstname_lastname_email(self):
        assert_that(self.temp.edit_client_in_database).raises(ValueError).when_called_with(1, self.wrongNewId,
                                                                                           self.wrongFirstname,
                                                                                           self.wrongLastname,
                                                                                           self.wrongEmail)

    def test_edit_client_in_database_wrong_id_firstname_lastname_email(self):
        assert_that(self.temp.edit_client_in_database).raises(ValueError).when_called_with(self.wrongId, 3,
                                                                                           self.wrongFirstname,
                                                                                           self.wrongLastname,
                                                                                           self.wrongEmail)

    def test_edit_client_in_database_wrong_id_new_id_lastname_email(self):
        assert_that(self.temp.edit_client_in_database).raises(ValueError).when_called_with(self.wrongId,
                                                                                           self.wrongNewId, 'Jan',
                                                                                           self.wrongLastname,
                                                                                           self.wrongEmail)

    def test_edit_client_in_database_wrong_id_new_id_firstname_email(self):
        assert_that(self.temp.edit_client_in_database).raises(ValueError).when_called_with(self.wrongId,
                                                                                           self.wrongNewId, 'Ola',
                                                                                           self.wrongLastname,
                                                                                           self.wrongEmail)

    def test_edit_client_in_database_wrong_id_new_id_firstname_lastname_email(self):
        assert_that(self.temp.edit_client_in_database).raises(ValueError).when_called_with(self.wrongId,
                                                                                           self.wrongNewId,
                                                                                           self.wrongLastname,
                                                                                           self.wrongLastname,
                                                                                           self.wrongEmail)

    def test_delete_client_in_database(self):
        assert_that(self.temp.delete_client_in_database).raises(ValueError).when_called_with(self.wrongId)

    def test_show_client_by_id(self):
        assert_that(self.temp.show_client_by_id).raises(ValueError).when_called_with(self.wrongId)

    def test_show_clients_by_firstname_and_lastname(self):
        assert_that(self.temp.show_clients_by_firstname_and_lastname).raises(ValueError).when_called_with(
            self.wrongFirstname)

    def test_add_order_to_client(self):
        assert_that(self.temp.add_order_to_client).raises(ValueError).when_called_with(self.wrongId)

    def test_delete_order_from_client(self):
        assert_that(self.temp.delete_order_from_client).raises(ValueError).when_called_with(self.wrongId)

    def test_show_orders_by_client_id(self):
        assert_that(self.temp.show_orders_by_client_id).raises(ValueError).when_called_with(self.wrongId)
