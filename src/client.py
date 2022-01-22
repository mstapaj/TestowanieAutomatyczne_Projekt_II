class Client:
    def __init__(self, id, firstname, lastname, email):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.orders = []
