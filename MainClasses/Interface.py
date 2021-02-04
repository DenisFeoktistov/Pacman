from Windows.MainMenu import MainMenu
from Windows.GameWindow import GameWindow
from Windows.PauseMenu import PauseMenu


class MainInterface:
    def __init__(self):
        self.main_menu = MainMenu(self)
        self.game_window = GameWindow(self)
        self.pause_menu = PauseMenu(self)

    def set_responder(self, responder):
        self.responder = responder
        self.main_menu.set_responder(responder.main_menu_responder)
        self.game_window.set_responder(responder.game_window_responder)
        self.pause_menu.set_responder(responder.pause_menu_responder)

    def show_main_menu(self):
        self.main_menu.show()

    def close_main_menu(self):
        self.main_menu.close()

    def show_game_window(self):
        self.game_window.show()

    def close_game_window(self):
        self.game_window.close()

    def show_pause_menu(self):
        self.pause_menu.show()

    def close_pause_menu(self):
        print(9)
        self.pause_menu.close()

    def show(self):
        self.main_menu.show()
