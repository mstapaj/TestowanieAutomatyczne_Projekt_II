import json

from src.database import Database
from src.order import Order


class Client:
    def __init__(self, client_id, firstname, lastname, email, database=None):
        if not isinstance(client_id, int) or client_id < 0 or str(client_id) == 'True' or str(client_id) == 'False':
            raise ValueError('Id klienta musi być dodatnią liczbą całkowitą')
        if not isinstance(firstname, str):
            raise ValueError('Imię musi być typu string')
        if not isinstance(lastname, str):
            raise ValueError('Nazwisko musi być typu string')
        if not isinstance(email, str):
            raise ValueError('Email musi być typu string')
        if '@' not in list(email):
            raise ValueError('Email musi zawierać @')
        self.client_id = client_id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.orders = []
        if not isinstance(database, Database):
            self.database = Database()
        else:
            self.database = database

    def add_client_to_database(self):
        return self.database.add_client(self)

    def edit_client_in_database(self, client_id, new_id=None, firstname=None, lastname=None, email=None):
        if not isinstance(client_id, int) or client_id < 0 or str(client_id) == 'True' or str(client_id) == 'False':
            raise ValueError('Id klienta musi być dodatnią liczbą całkowitą')
        if isinstance(new_id, int) and str(new_id) != 'True' and str(new_id) != 'False' and new_id >= 0:
            self.client_id = new_id
        elif new_id is not None:
            raise ValueError('Nowe id klienta musi być dodatnią liczbą całkowitą')
        if isinstance(firstname, str):
            self.firstname = firstname
        elif firstname is not None:
            raise ValueError('Błedny typ danych w imieniu')
        if isinstance(lastname, str):
            self.lastname = lastname
        elif lastname is not None:
            raise ValueError('Błedny typ danych w nazwisku')
        if isinstance(email, str) and '@' in list(email):
            self.email = email
        elif email is not None:
            raise ValueError('Błedny typ danych w emailu, email musi zawierać @')
        return self.database.edit_client(client_id, self)

    def delete_client_in_database(self, client_id):
        if not isinstance(client_id, int) or client_id < 0 or str(client_id) == 'True' or str(client_id) == 'False':
            raise ValueError('Id klienta musi być dodatnią liczbą całkowitą')
        return self.database.delete_client(client_id)

    def show_clients(self):
        return self.database.show_clients()

    def show_client_by_id(self, client_id):
        if not isinstance(client_id, int) or client_id < 0 or str(client_id) == 'True' or str(client_id) == 'False':
            raise ValueError('Id klienta musi być dodatnią liczbą całkowitą')
        return self.database.show_client_by_id(client_id)

    def show_clients_by_firstname_and_lastname(self, word):
        if not isinstance(word, str):
            raise ValueError('Błedny typ danych w wyszukiwanym imieniu lub nazwisku')
        return self.database.show_clients_by_firstname_and_lastname(word)

    def add_order_to_client(self, order_id):
        if not isinstance(order_id, int) or order_id < 0 or str(order_id) == 'True' or str(order_id) == 'False':
            raise ValueError('Id zamówienia musi być dodatnią liczbą całkowitą')
        for i in self.orders:
            if i.order_id == order_id:
                raise ValueError('Zamowienie o takim id znajduje sie juz w bazie')
        self.orders.append(Order(order_id, self.client_id))
        return self.database.add_order_to_client(self.client_id, order_id)

    def delete_order_from_client(self, order_id):
        if not isinstance(order_id, int) or order_id < 0 or str(order_id) == 'True' or str(order_id) == 'False':
            raise ValueError('Id zamówienia musi być dodatnią liczbą całkowitą')
        neworders = []
        for i in self.orders:
            if i.order_id != order_id:
                neworders.append(i)
        return self.database.delete_order_from_client(self.client_id, order_id)

    def show_orders_by_client_id(self, client_id):
        if not isinstance(client_id, int) or client_id < 0 or str(client_id) == 'True' or str(client_id) == 'False':
            raise ValueError('Id klienta musi być dodatnią liczbą całkowitą')
        return self.database.show_orders_by_client_id(client_id)

    def save_clients_to_file(self):
        allclients = self.database.show_clients()
        with open('data/clients.json', 'w') as file:
            file.write(json.dumps(allclients))
