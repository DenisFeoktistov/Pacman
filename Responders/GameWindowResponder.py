class GameWindowResponder:
    def __init__(self, main_responder):
        self.main_responder = main_responder

    def set_interface(self, interface):
        self.interface = interface

    def get_score(self):
        return self.interface.game.points - self.interface.game.score

    def get_minutes(self):
        return self.interface.game.responder.get_minutes()

    def get_seconds(self):
        return self.interface.game.responder.get_seconds()
