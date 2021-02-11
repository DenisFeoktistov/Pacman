from PyQt5.QtWidgets import QApplication
import pygame
import sys


from Windows.MainWindow import MainWindow


class App:
    def __init__(self):
        self.game = MainWindow()
        self.game.show()


if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()

    app = QApplication(sys.argv)
    game = App()

    pygame.quit()
    pygame.font.quit()
    pygame.mixer.quit()
    sys.exit(app.exec())
