from MainMenu import MainMenu
from GameWindow import GameWindow


class MainInterface:
    def __init__(self):
        self.main_menu = MainMenu(self)
        self.game_window = GameWindow(self)
