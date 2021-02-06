from random import randint


class GameResponder:
    def __init__(self, game):
        self.game = game

    def get_target(self):
        i = max(0, min(self.game.maze.height - 1, self.game.pacman.i + randint(-1, 1)))
        j = max(0, min(self.game.maze.width - 1, self.game.pacman.j + randint(-1, 1)))
        return i, j
