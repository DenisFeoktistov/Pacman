from MainMenuResponder import MainMenuResponder
from GameWindowResponder import  GameWindowResponder


class MainResponder:
    def __init__(self):
        self.main_menu_responder = MainMenuResponder(self)
        self.game_window_responder = GameWindowResponder(self)
