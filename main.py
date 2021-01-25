from PyQt5.QtWidgets import QApplication
import sys

from Windows.GameWindow import GameWindow
from Windows.MainMenu import MainMenu


class Game:
    def __init__(self):
        self.menu = MainMenu()
        self.game_window = GameWindow()

    def show(self):
        self.menu.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = Game()
    game.show()
    sys.exit(app.exec())
