from random import randint


class GameResponder:
    def __init__(self, game):
        self.game = game

    def generate_ghost_place(self, min_way):
        i = randint(0, self.game.maze.height - 1)
        j = randint(0, self.game.maze.width - 1)

        while len(self.game.maze.way(i, j, 0, 0)) < min_way:
            i = randint(0, self.game.maze.height - 1)
            j = randint(0, self.game.maze.width - 1)

        return i, j

    def get_target(self, precision):
        i = max(0, min(self.game.maze.height - 1, self.game.pacman.i + randint(-precision, precision)))
        j = max(0, min(self.game.maze.width - 1, self.game.pacman.j + randint(-precision, precision)))
        return i, j
