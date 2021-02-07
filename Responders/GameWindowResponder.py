import datetime as dt


class GameWindowResponder:
    def __init__(self, main_responder):
        self.main_responder = main_responder

    def set_interface(self, interface):
        self.interface = interface

    def get_score(self):
        return self.interface.game.points - self.interface.game.score

    def get_minutes(self):
        if not self.interface.game.lose:
            return ((dt.datetime.now() - self.interface.game.start_time).seconds // 60) % 60
        return ((self.interface.game.end_time - self.interface.game.start_time).seconds // 60) % 60

    def get_seconds(self):
        if not self.interface.game.lose:
            return (dt.datetime.now() - self.interface.game.start_time).seconds % 60
        return (self.interface.game.end_time - self.interface.game.start_time).seconds % 60
