from src.database import Database


class Client:
    def __init__(self, id, firstname, lastname, email):
        if not isinstance(id, int) or id < 0 or str(id) == 'True' or str(id) == 'False':
            raise ValueError('Id musi być dodatnią liczbą całkowitą')
        if not isinstance(firstname, str):
            raise ValueError('Imię musi być typu string')
        if not isinstance(lastname, str):
            raise ValueError('Nazwisko musi być typu string')
        if not isinstance(email, str):
            raise ValueError('Email musi być typu string')
        if '@' not in list(email):
            raise ValueError('Email musi zawierać @')
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.orders = []
        self.database = Database()

    def add_client_to_database(self):
        return self.database.add_client(self)

    def edit_client_in_database(self, id, new_id=None, firstname=None, lastname=None, email=None):
        if not isinstance(id, int) or id < 0 or str(id) == 'True' or str(id) == 'False':
            raise ValueError('Id musi być dodatnią liczbą całkowitą')
        if isinstance(new_id, int) and str(new_id) != 'True' and str(new_id) != 'False' and new_id >= 0:
            self.id = new_id
        elif new_id is not None:
            raise ValueError('Nowe id musi być dodatnią liczbą całkowitą')
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
        return self.database.edit_client(self)

    def delete_client_in_database(self, id):
        return self.database.delete_client(id)
