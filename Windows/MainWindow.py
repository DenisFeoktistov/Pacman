import pygame


from Windows.GameWindow import GameWindow
from Windows.MenuWindow import MenuWindow
from Windows.ScoreTableWindow import ScoreTableWindow
from Windows.RulesWindow import RulesWindow


class MainWindow:
    SIZE = WIDTH, HEIGHT = 1000, 600
    FPS = 120

    def __init__(self):
        self.screen = pygame.display.set_mode(MainWindow.SIZE)
        self.time = pygame.time.Clock()

        self.game_window = GameWindow(self)
        self.main_window = MenuWindow(self)
        self.score_window = ScoreTableWindow(self)
        self.rules_window = RulesWindow(self)

    def show(self):
        self.game_window.show()

    def switch_to_game(self):
        self.game_window.show()

    def switch_to_menu(self):
        self.main_window.show()

    def switch_to_score(self):
        self.score_window.show()

    def switch_to_rules(self):
        self.rules_window.show()

