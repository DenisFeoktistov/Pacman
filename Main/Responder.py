from MainMenuResponder import MainMenuResponder
from GameWindowResponder import GameWindowResponder


class MainResponder:
    def __init__(self):
        self.main_menu_responder = MainMenuResponder(self)
        self.game_window_responder = GameWindowResponder(self)

    def set_interface(self, interface):
        self.interface = interface
        self.game_window_responder.set_interface(interface.game_window)
        self.main_menu_responder.set_interface(interface.main_menu)
