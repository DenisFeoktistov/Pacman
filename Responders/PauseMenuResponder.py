import pygame


class GamePauseResponder:
    def __init__(self, main_responder):
        self.main_responder = main_responder

    def set_interface(self, interface):
        self.interface = interface

    def continue_play(self):
        print(1)
        self.main_responder.game_window_responder.continue_play()
        self.interface.main_interface.close_pause_menu()

    def return_to_menu(self):
        self.main_responder.game_window_responder.return_to_menu()
        self.interface.main_interface.close_pause_menu()
