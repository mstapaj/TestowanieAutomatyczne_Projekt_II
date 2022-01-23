from src.database import Database


class Item:
    def __init__(self, id, name, value):
        if not isinstance(id, int) or id < 0 or str(id) == 'True' or str(id) == 'False':
            raise ValueError('Id musi być dodatnią liczbą całkowitą')
        if not isinstance(name, str):
            raise ValueError('Nazwa musi być typu string')
        if not isinstance(value, float) or value < 0 or str(value) == 'True' or str(value) == 'False':
            raise ValueError('Wartość musi być dodatnią liczbą zmiennoprzecinkową')
        self.id = id
        self.name = name
        self.value = value

    def add_item_to_database(self):
        return Database.add_item(self)

    def edit_item_in_database(self, id, new_id=None, name=None, value=None):
        if not isinstance(id, int) or id < 0 or str(id) == 'True' or str(id) == 'False':
            raise ValueError('Id musi być dodatnią liczbą całkowitą')
        if isinstance(new_id, int) and str(new_id) != 'True' and str(new_id) != 'False' and new_id >= 0:
            self.id = new_id
        elif new_id is not None:
            raise ValueError('Nowe id musi być dodatnią liczbą całkowitą')
        if isinstance(name, str):
            self.name = name
        elif name is not None:
            raise ValueError('Błedny typ danych w nazwie')
        if isinstance(value, int) and str(value) != 'True' and str(value) != 'False' and value >= 0:
            self.value = value
        elif value is not None:
            raise ValueError('Wartość musi być dodatnią liczbą zmiennoprzecinkową')
        return Database.edit_item(id, self)

    def delete_item_in_database(self, id):
        if not isinstance(id, int) or id < 0 or str(id) == 'True' or str(id) == 'False':
            raise ValueError('Id musi być dodatnią liczbą całkowitą')
        return Database.delete_item(id)
