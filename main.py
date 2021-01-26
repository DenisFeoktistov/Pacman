from PyQt5.QtWidgets import QApplication
import sys

from Main.Responder import MainResponder
from Main.Interface import MainInterface


class Game:
    def __init__(self):
        self.responder = MainResponder()
        self.interface = MainInterface()

        self.interface.set_responder(self.responder)
        self.responder.set_interface(self.interface)

    def show(self):
        self.interface.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = Game()
    game.show()
    sys.exit(app.exec())
