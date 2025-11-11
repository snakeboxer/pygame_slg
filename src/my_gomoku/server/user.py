from socket import socket

class User:

    def __init__(self, uid: int, name: str, password: str):
        self.session = None
        self.uid = uid
        self.name = name
        self.password = password

    def bind_session(self, session: socket):
        self.session = session

    def unbind_session(self):
        self.session = None