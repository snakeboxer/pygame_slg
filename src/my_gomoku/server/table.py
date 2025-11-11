from src.my_gomoku.server.game_session import GameSession


class Table:

    seat_left = None
    seat_right = None

    game = None

    def __init__(self):
        pass

    def take_seat(self, user_id, position = 'left'):
        if user_id is None:
            raise Exception('user_id input missing')
        if position == 'left':
            self.seat_left = user_id
        elif position == 'right':
            self.seat_right = user_id
        else:
            raise Exception('wrong position input')

        if self.seat_left is not None and self.seat_right is not None:
            game = GameSession()
            game.start()

    def leave_seat(self, position = 'left'):
        if position == 'left':
            self.seat_left = None
        elif position == 'right':
            self.seat_right = None