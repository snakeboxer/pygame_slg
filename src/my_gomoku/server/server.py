import socket
import threading
from hall import Hall
from user import User

class Server:

    def __init__(self, table_count = 4):
        self.hall = Hall(table_count)

    def start(self, ip_address='127.0.0.1', port=8123):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((ip_address, port))
        server_socket.listen()

        while(True):
            (client_socket, client_address) = server_socket.accept()
            payload = client_socket.recv(1024)

            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))


    def register(self, name, password):
        users = self.register_info.values()
        for user in users:
            if user.name == name:
                raise Exception('user name already exists')

        user_id = max(self.register_info.keys()) + 1
        self.register_info[user_id] = User(user_id, name, password)


    def init_register_info(self):
        self.register_info = {
            1: User(1, 'mimyu', '123456'),
            2: User(2, 'l', '123456')
        }
