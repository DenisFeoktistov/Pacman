class GameWindowResponder:
    def __init__(self, game_window):
        self.game_window = game_window

    def get_score(self):
        return self.game_window.game.points - self.game_window.game.score

    def get_minutes(self):
        return self.game_window.game.responder.get_minutes()

    def get_seconds(self):
        return self.game_window.game.responder.get_seconds()
