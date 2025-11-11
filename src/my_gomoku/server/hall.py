import typing

from table import Table
from user import User

class Hall:

    def __init__(self, table_count = 4):
        self.register_info = {}
        self.tables = {}
        for index in range(table_count):
            self.tables[index] = Table()

        self.init_register_info()


