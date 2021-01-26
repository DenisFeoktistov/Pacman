class MainMenuResponder:
    def __init__(self, main_responder):
        self.main_responder = main_responder

    def set_interface(self, interface):
        self.interface = interface

    def play(self):
        self.interface.main_interface_class.close_main_menu()
        self.interface.main_interface_class.show_game_window()
