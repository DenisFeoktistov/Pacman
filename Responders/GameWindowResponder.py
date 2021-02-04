import pygame


class GameWindowResponder:
    def __init__(self, main_responder):
        self.main_responder = main_responder

    def set_interface(self, interface):
        self.interface = interface

    def pause(self):
        print(3)
        self.interface.running = False
        self.interface.main_interface.show_pause_menu()

    def continue_play(self):
        print(4)
        self.interface.start_main_cycle()

    def return_to_menu(self):
        self.interface.main_interface.close_game_window()
        self.interface.main_interface.show_main_menu()
