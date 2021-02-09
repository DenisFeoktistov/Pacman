from PyQt5.QtWidgets import QApplication
import pygame
import sys


from Windows.GameWindow import GameWindow


class App:
    def __init__(self):
        self.game = GameWindow()
        self.game.show()


if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()

    app = QApplication(sys.argv)
    game = App()

    pygame.quit()
    sys.exit(app.exec())
