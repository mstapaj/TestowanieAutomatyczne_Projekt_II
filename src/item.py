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
        Database.add_item(self)
