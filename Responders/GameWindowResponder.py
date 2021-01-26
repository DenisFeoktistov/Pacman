class GameWindowResponder:
    def __init__(self, main_responder):
        self.main_responder = main_responder

    def set_interface(self, interface):
        self.interface = interface
