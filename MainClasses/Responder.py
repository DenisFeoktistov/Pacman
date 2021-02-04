from Responders.MainMenuResponder import MainMenuResponder
from Responders.GameWindowResponder import GameWindowResponder
from Responders.PauseMenuResponder import GamePauseResponder


class MainResponder:
    def __init__(self):
        self.main_menu_responder = MainMenuResponder(self)
        self.game_window_responder = GameWindowResponder(self)
        self.pause_menu_responder = GamePauseResponder(self)

    def set_interface(self, interface):
        self.interface = interface
        self.game_window_responder.set_interface(interface.game_window)
        self.main_menu_responder.set_interface(interface.main_menu)
        self.pause_menu_responder.set_interface(interface.pause_menu)

    def from_menu_to_game(self):
        self.interface.from_menu_to_game()
