import pygame

from GameFiles.Maze import Maze
from GameFiles.Pacman import Pacman


class Game:
    def __init__(self, screen):
        self.maze = Maze(x=20, y=100, width=16, height=8, cell_width=60, cell_height=60, screen=screen)
        self.maze.generate()

        self.pacman = Pacman(x=25, y=105, cycle_iterations=12, cycle_time=240, step=60)
        self.pacman_sprite = pygame.sprite.GroupSingle(self.pacman)

    def draw(self, screen):
        self.maze.draw()
        self.pacman_sprite.draw(screen)

    def update(self):
        self.pacman.update()
