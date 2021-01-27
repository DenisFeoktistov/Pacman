import pygame


class GameWindow:
    def __init__(self, main_interface_class):
        self.main_interface_class = main_interface_class

    def set_responder(self, responder):
        self.responder = responder

    def show(self):
        pass

    def close(self):
        pass
