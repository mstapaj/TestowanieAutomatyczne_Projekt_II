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
        if not isinstance(id, int) or id < 0 or str(id) == 'True' or str(id) == 'False':
            raise ValueError('Id musi być dodatnią liczbą całkowitą')
        if isinstance(new_id, int) and str(new_id) != 'True' and str(new_id) != 'False' and new_id >= 0:
            self.id = new_id
        elif new_id is not None:
            raise ValueError('Nowe id musi być dodatnią liczbą całkowitą')
        if isinstance(client_id, int) and str(client_id) != 'True' and str(client_id) != 'False' and client_id >= 0:
            self.id_client = client_id
        elif client_id is not None:
            raise ValueError('Nowe id musi być dodatnią liczbą całkowitą')
        return self.database.edit_order(id, self)

    def delete_order_from_database(self, id):
        if not isinstance(id, int) or id < 0 or str(id) == 'True' or str(id) == 'False':
            raise ValueError('Id musi być dodatnią liczbą całkowitą')
        return self.database.delete_order(id)

    def add_item_to_order(self, item_id):
        if not isinstance(item_id, int) or item_id < 0 or str(item_id) == 'True' or str(item_id) == 'False':
            raise ValueError('Id musi być dodatnią liczbą całkowitą')
        if len(self.database.show_item_by_id(item_id)) > 0:
            return self.database.add_item_to_order(self.id_client, item_id)
