from src.database import Database


class Order:
    def __init__(self, order_id, client_id, database=None):
        if not isinstance(order_id, int) or order_id < 0 or str(order_id) == 'True' or str(order_id) == 'False':
            raise ValueError('Id zamówienia musi być dodatnią liczbą całkowitą')
        if not isinstance(client_id, int) or client_id < 0 or str(client_id) == 'True' or str(client_id) == 'False':
            raise ValueError('Id klienta musi być dodatnią liczbą całkowitą')
        self.order_id = order_id
        self.client_id = client_id
        self.items = []
        if not isinstance(database, Database):
            self.database = Database()
        else:
            self.database = database

    def add_order_to_database(self):
        return self.database.add_order(self)

    def edit_order_in_database(self, order_id, new_id=None, client_id=None):
        if not isinstance(order_id, int) or order_id < 0 or str(order_id) == 'True' or str(order_id) == 'False':
            raise ValueError('Id zamówienia musi być dodatnią liczbą całkowitą')
        if isinstance(new_id, int) and str(new_id) != 'True' and str(new_id) != 'False' and new_id >= 0:
            self.order_id = new_id
        elif new_id is not None:
            raise ValueError('Nowe id zamówienia musi być dodatnią liczbą całkowitą')
        if isinstance(client_id, int) and str(client_id) != 'True' and str(client_id) != 'False' and client_id >= 0:
            self.client_id = client_id
        elif client_id is not None:
            raise ValueError('Nowe id klienta musi być dodatnią liczbą całkowitą')
        return self.database.edit_order(order_id, self)

    def delete_order_from_database(self, order_id):
        if not isinstance(order_id, int) or order_id < 0 or str(order_id) == 'True' or str(order_id) == 'False':
            raise ValueError('Id zamówienia musi być dodatnią liczbą całkowitą')
        return self.database.delete_order(order_id)

    def add_item_to_order(self, item_id):
        if not isinstance(item_id, int) or item_id < 0 or str(item_id) == 'True' or str(item_id) == 'False':
            raise ValueError('Id produktu musi być dodatnią liczbą całkowitą')
        if len(self.database.show_item_by_id(item_id)) > 0:
            self.items.append(self.database.show_item_by_id(item_id))
            return self.database.add_item_to_order(self.client_id, item_id)

    def delete_item_from_order(self, item_id):
        if not isinstance(item_id, int) or item_id < 0 or str(item_id) == 'True' or str(item_id) == 'False':
            raise ValueError('Id produktu musi być dodatnią liczbą całkowitą')
        newitems = []
        for i in self.items:
            if i.item_id != item_id:
                newitems.append(i)
        return self.database.delete_item_from_order(self.client_id, item_id)

    def show_items_by_order_id(self, order_id):
        if not isinstance(order_id, int) or order_id < 0 or str(order_id) == 'True' or str(order_id) == 'False':
            raise ValueError('Id zamówienia musi być dodatnią liczbą całkowitą')
        return self.database.show_items_by_order_id(order_id)
