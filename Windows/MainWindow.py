import pygame


from Windows.GameWindow import GameWindow
from Windows.MenuWindow import MenuWindow


class MainWindow:
    SIZE = WIDTH, HEIGHT = 1000, 600
    FPS = 120

    def __init__(self):
        self.screen = pygame.display.set_mode(MainWindow.SIZE)
        self.time = pygame.time.Clock()

        self.game_window = GameWindow(self)
        self.main_window = MenuWindow(self)

    def show(self):
        self.game_window.show()

    def switch_to_game(self):
        self.game_window.show()

    def switch_to_menu(self):
        self.main_window.show()
