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

    def edit_client_in_database(self):
        return self.database.edit_client(self)
