from PyQt5.QtWidgets import QApplication
import pygame
import sys

from MainClasses.Responder import MainResponder
from MainClasses.Interface import MainInterface


class Game:
    def __init__(self):
        self.responder = MainResponder()
        self.interface = MainInterface()

        self.interface.set_responder(self.responder)
        self.responder.set_interface(self.interface)

    def show(self):
        self.interface.show()


if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    app = QApplication(sys.argv)

    game = Game()
    game.show()

    pygame.quit()
    sys.exit(app.exec())
