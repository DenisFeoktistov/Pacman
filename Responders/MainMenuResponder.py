class MainMenuResponder:
    def __init__(self, main_responder):
        self.main_responder = main_responder

    def set_interface(self, interface):
        self.interface = interface

    def play(self):
        self.main_responder.from_menu_to_game()
