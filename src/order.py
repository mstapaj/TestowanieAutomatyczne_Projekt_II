from src.database import Database


class Order:
    def __init__(self, id, id_client, database=None):
        if not isinstance(id, int) or id < 0 or str(id) == 'True' or str(id) == 'False':
            raise ValueError('Id musi być dodatnią liczbą całkowitą')
        if not isinstance(id_client, int) or id_client < 0 or str(id_client) == 'True' or str(id_client) == 'False':
            raise ValueError('Id klienta musi być dodatnią liczbą całkowitą')
        self.id = id
        self.id_client = id_client
        self.items = []
        if not isinstance(database, Database):
            self.database = Database()
        else:
            self.database = database

    def add_order_to_database(self):
        return self.database.add_order(self)

    def edit_order_in_database(self, id, new_id=None, client_id=None):
        self.id = new_id
        self.id_client = client_id
        return self.database.edit_order(id, self)

    def add_item_to_order(self, item_id):
        return self.database.add_item_to_order(self.id, item_id)
