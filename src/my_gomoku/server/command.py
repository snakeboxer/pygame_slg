class Command:
    """

    """
    def __init__(self, command_type: str, *args, **kwargs):
        self.command_type = command_type
        print(kwargs)


REGISTER_COMMAND = b'a'
LOGIN_COMMAND = 0b0010
TAKE_SEAT_COMMAND = 0b0011

def parse_command(payload: str)-> Command:
    command_type = payload[0:1].encode(encoding='ascii')
    param_length = int(payload[1:3])
    parameters = payload[3:param_length+3]

    if command_type == REGISTER_COMMAND:
        params = parameters.split('||')
        return Command(REGISTER_COMMAND, name = params[0], password = params[1])

payload = 'a07fa||sdf'
command = parse_command(payload)