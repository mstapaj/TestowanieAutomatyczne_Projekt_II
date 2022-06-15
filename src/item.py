from src.database import Database
import json


class Item:
    def __init__(self, item_id, name, value, database=None):
        if not isinstance(item_id, int) or item_id < 0 or str(item_id) == 'True' or str(item_id) == 'False':
            raise ValueError('Id produktu musi być dodatnią liczbą całkowitą')
        if not isinstance(name, str):
            raise ValueError('Nazwa musi być typu string')
        if not isinstance(value, float) or value < 0 or str(value) == 'True' or str(value) == 'False':
            raise ValueError('Wartość musi być dodatnią liczbą zmiennoprzecinkową')
        self.item_id = item_id
        self.name = name
        self.value = value
        if not isinstance(database, Database):
            self.database = Database()
        else:
            self.database = database

    def add_item_to_database(self):
        return self.database.add_item(self)

    def edit_item_in_database(self, item_id, new_id=None, name=None, value=None):
        if not isinstance(item_id, int) or item_id < 0 or str(item_id) == 'True' or str(item_id) == 'False':
            raise ValueError('Id musi być dodatnią liczbą całkowitą')
        if isinstance(new_id, int) and str(new_id) != 'True' and str(new_id) != 'False' and new_id >= 0:
            self.item_id = new_id
        elif new_id is not None:
            raise ValueError('Nowe id produktu musi być dodatnią liczbą całkowitą')
        if isinstance(name, str):
            self.name = name
        elif name is not None:
            raise ValueError('Błedny typ danych w nazwie')
        if isinstance(value, float) and str(value) != 'True' and str(value) != 'False' and value >= 0:
            self.value = value
        elif value is not None:
            raise ValueError('Wartość musi być dodatnią liczbą zmiennoprzecinkową')
        return self.database.edit_item(item_id, self)

    def delete_item_in_database(self, item_id):
        if not isinstance(item_id, int) or item_id < 0 or str(item_id) == 'True' or str(item_id) == 'False':
            raise ValueError('Id produktu musi być dodatnią liczbą całkowitą')
        return self.database.delete_item(item_id)

    def show_items_from_database(self):
        return self.database.show_items()

    def show_item_by_id(self, item_id):
        if not isinstance(item_id, int) or item_id < 0 or str(item_id) == 'True' or str(item_id) == 'False':
            raise ValueError('Id produktu musi być dodatnią liczbą całkowitą')
        return self.database.show_item_by_id(item_id)

    def show_items_by_name(self, name):
        if not isinstance(name, str):
            raise ValueError('Nazwa musi być typu string')
        return self.database.show_items_by_name(name)

    def save_items_to_file(self):
        allitems = self.database.show_items()
        with open('data/items.json', 'w') as file:
            file.write(json.dumps(allitems))
