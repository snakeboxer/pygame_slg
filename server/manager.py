from server.hall import Hall
from server.user import User
from socket import socket
from command import (
    dec_command,
    encrypt_hall_info,
    REGISTER,
    LOGIN
)
from threading import Thread

class Manager:

    def __init__(self, table_count:int=4):
        self.hall = Hall(table_count)
        self.clients = []
        self.online_users = []
        self.init_register_info()


    def init_register_info(self):
        self.register_info = {
            1: User(1, 'mimyu', '123456'),
            2: User(2, 'l', '123456')
        }

    def register(self, user_name:str, password:str, socket_client:socket) -> bool:
        """
        for processing REGISTER command
        :param user_name:  username
        :param password:   password
        """

        # 0. user name deduplicate
        users = self.register_info.values()
        for user in users:
            if user.name == user_name:
                raise Exception('user name already exists')

        # 1. get new user id: max + 1
        user_id = max(self.register_info.keys()) + 1
        new_user = User(user_id, user_name, password)
        new_user.bind_session(socket)

        # 2. add to register info
        # todo: move register info to database
        self.register_info[user_id] = new_user

        # 3. add to client list
        self.clients.append(socket_client)

        # 4. send congratulation info
        socket_client.send(bytes('register success, your id is {}'.format(user_id), 'utf-8'))

        # 5. add to online user list
        self.online_users.append(new_user)

        # 6. send hall info
        socket_client.send(encrypt_hall_info(self.hall))

        return True

    def login(self, user_name:str, password:str, socket_client:socket) -> bool:
        users = self.register_info.values()
        for user in users:
            if user.name == user_name and user.password == password:
                user.bind_session(socket)
                self.clients.append(socket_client)
                self.online_users.append(user)

                socket_client.send(b'login success')
                socket_client.send(encrypt_hall_info(self.hall))
                return True


        socket_client.send(b'login failed')
        return False

    def submit(self, socket_client: socket ):
        # async processing to avoid blocked by any client
        Thread(target=process_submit, args = (socket_client, self)).start()


def process_submit(socket_client: socket, manager: Manager):
    command = dec_command(socket_client.recv(1024).decode('utf-8'))
    if command.command_type == REGISTER:
        manager.register(user_name=command.get_param("user_name"), password=command.get_param("password"), socket_client=socket_client)
    elif command.command_type == LOGIN:
        if manager.login(user_name=command.get_param("user_name"), password=command.get_param("password"), socket_client=socket_client) is False:
            # login failed then close the connection
            socket_client.close()
    else:
        socket_client.send(b'Unrecognized command')
        socket_client.close()

