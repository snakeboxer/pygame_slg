import socket
from server.manager import Manager



class Server:
    """
    only task is to accept new client connection
    """
    def __init__(self, table_count = 4):
        """
        init a game manager
        :param table_count:
        """
        self.manager = Manager(4)

    def start(self, ip_address='127.0.0.1', port=8123):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((ip_address, port))
        server_socket.listen()

        while True:
            (client_socket, client_address) = server_socket.accept()
            self.manager.submit(client_socket)
