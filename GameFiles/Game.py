import pygame

from GameFiles.Maze import Maze
from GameFiles.Pacman import MazePacman
from GameFiles.Ghost import MazeGhost
from Responders.GameResponder import GameResponder


class Game:
    def __init__(self, screen):
        self.responder = GameResponder(self)
        # We use 12 *, just because it is better for game. If you choose something like 77 or 113, game will be started,
        # but you can find some problems, because of float numbers, that will be in GeneralSprite.
        self.maze = Maze(x=20, y=100, height=8, width=16, cell_width=12 * 5, cell_height=12 * 5, screen=screen,
                         game=self)
        self.maze.generate()

        self.pacman = MazePacman(i=0, j=0, sprite_size_x=50, sprite_size_y=50, cycle_time=12 * 20, maze=self.maze)
        self.pacman_sprite = pygame.sprite.GroupSingle(self.pacman)

        self.ghosts = list()
        self.ghost_sprites = pygame.sprite.Group()

        self.ghosts_colors = ["red", "blue"]
        for color in self.ghosts_colors:
            self.ghosts.append(
                MazeGhost(i=5, j=10, sprite_size_x=50, sprite_size_y=50, cycle_time=12 * 20, maze=self.maze,
                          color=color))
            self.ghost_sprites.add(self.ghosts[-1])

    def draw(self, screen):
        self.maze.draw()
        self.pacman_sprite.draw(screen)
        self.ghost_sprites.draw(screen)

    def update(self):
        self.pacman.update()
        self.ghost_sprites.update()

    def handle(self, event):
        self.pacman.handle(event)
        for ghost in self.ghosts:
            ghost.update()
