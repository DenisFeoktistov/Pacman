import pygame

from GameFiles.Maze import Maze
from GameFiles.Pacman import Pacman
from GameFiles.Ghost import Ghost
import GameFiles.SpritesClasses as SpritesClasses


class Game:
    def __init__(self, screen):
        self.maze = Maze(x=20, y=100, width=16, height=8, cell_width=60, cell_height=60, screen=screen)
        self.maze.generate()

        self.pacman = Pacman(x=25, y=105, sprite_size=50, cycle_iterations=12,
                             cycle_time=240, step=60)
        self.pacman_sprite = pygame.sprite.GroupSingle(self.pacman)

        '''self.ghost = Ghost(x=145, y=220, frames=(('data/sprites/ghosts/ghost_up1.png', ), ),
                           sprite_size=50, cycle_iterations=12, cycle_time=360, step=60)
        self.ghost_sprites = pygame.sprite.Group()
        self.ghost_sprites.add(self.ghost)'''

    def draw(self, screen):
        self.maze.draw()
        self.pacman_sprite.draw(screen)
        # self.ghost_sprites.draw(screen)

    def update(self):
        self.pacman.update()
        # self.ghost_sprites.update()
