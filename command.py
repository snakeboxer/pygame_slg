from server.hall import Hall

"""
command type enums
"""
REGISTER = ord('1')
LOGIN = ord('2')
TAKE_SEAT = ord('3')

class Command:

    def __init__(self, command_type: int, *args, **kwargs):
        self.command_type = command_type
        self.params = kwargs

    def get_param(self, param_name: str):
        return self.params.get(param_name)




def dec_command(payload: str)-> Command:
    command_type = ord(payload[0:1])
    param_length = int(payload[1:3])
    parameters = payload[3:param_length+3]

    if command_type == REGISTER:
        params = parameters.split('||')
        return Command(REGISTER, user_name = params[0], password = params[1])
    elif command_type == LOGIN:
        params = parameters.split('||')
        return Command(LOGIN, user_name = params[0], password = params[1])

def encrypt_hall_info(hall: Hall) -> bytes:
    return bytes(repr(hall), 'utf-8')

def decrypt_hall_info(encrypted_bytes: bytes) -> Hall:
    return eval(bytes.decode(encrypted_bytes, 'utf-8'))

if __name__ == '__main__':
    user_name = "mimyu"
    password = "asdfasdf"
    string = chr(REGISTER) +str(len(user_name + "||" + password)) + user_name + "||" + password
    command = dec_command(string)
    print(command)
    print(REGISTER)