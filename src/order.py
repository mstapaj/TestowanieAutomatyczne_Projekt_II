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
