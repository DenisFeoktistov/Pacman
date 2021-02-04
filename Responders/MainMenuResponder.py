class MainMenuResponder:
    def __init__(self, main_responder):
        self.main_responder = main_responder

    def set_interface(self, interface):
        self.interface = interface

    def play(self):
        self.interface.main_interface.close_main_menu()
        self.interface.main_interface.show_game_window()
