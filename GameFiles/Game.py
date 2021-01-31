import pygame


from GameFiles.Maze import Maze
from GameFiles.Pacman import Pacman


class Game:
    def __init__(self, screen):
        self.maze = Maze(x=20, y=100, width=16, height=8, cell_width=60, cell_height=60, screen=screen)
        self.maze.generate()

        self.borders = pygame.sprite.Group()


        self.pacman = Pacman(x=25, y=105, borders=self.borders)
        self.pacman_sprite = pygame.sprite.GroupSingle(self.pacman)

    def draw(self, screen):
        self.pacman_sprite.update()
        self.maze.draw()
        self.pacman_sprite.draw(screen)
