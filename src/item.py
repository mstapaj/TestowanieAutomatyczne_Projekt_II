class Item:
    def __init__(self, id, name, value, database):
        if not isinstance(id, int) or id < 0 or str(id) == 'True' or str(id) == 'False':
            raise ValueError('Id musi być dodatnią liczbą całkowitą')
        if not isinstance(name, str):
            raise ValueError('Nazwa musi być typu string')
        if not isinstance(value, float) or value < 0 or str(value) == 'True' or str(value) == 'False':
            raise ValueError('Wartość musi być dodatnią liczbą zmiennoprzecinkową')
        self.id = id
        self.name = name
        self.value = value
        self.database = database

    def add_item_to_database(self):
        return self.database.add_item(self)

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
        if isinstance(value, float) and str(value) != 'True' and str(value) != 'False' and value >= 0:
            self.value = value
        elif value is not None:
            raise ValueError('Wartość musi być dodatnią liczbą zmiennoprzecinkową')
        return self.database.edit_item(id, self)

    def delete_item_in_database(self, id):
        if not isinstance(id, int) or id < 0 or str(id) == 'True' or str(id) == 'False':
            raise ValueError('Id musi być dodatnią liczbą całkowitą')
        return self.database.delete_item(id)

    def show_items_from_database(self):
        return self.database.show_items()

    def show_item_by_id(self, id):
        if not isinstance(id, int) or id < 0 or str(id) == 'True' or str(id) == 'False':
            raise ValueError('Id musi być dodatnią liczbą całkowitą')
        return self.database.show_item_by_id(id)

    def show_items_by_name(self, name):
        if not isinstance(name, str):
            raise ValueError('Nazwa musi być typu string')
        return self.database.show_items_by_name(name)
