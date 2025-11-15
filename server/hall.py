from server.table import Table

class Hall:

    def __init__(self, table_count):
        self.tables = {}
        for index in range(table_count):
            self.tables[index] = Table()

    def __repr__(self):
        pass
