import pygame

from GameFiles.Maze import Maze
from GameFiles.Pacman import MazePacman
from GameFiles.Star import Star
from GameFiles.Ghost import Ghost
import GameFiles.SpritesClasses as SpritesClasses


class Game:
    def __init__(self, screen):
        self.score = 0
        # We use 12 *, just because it is better for game. If you choose something like 77 or 113, game will be started,
        # but you can find some problems, because of float numbers, that will be in GeneralSprite.
        self.maze = Maze(x=20, y=100, width=16, height=8, cell_width=12 * 5, cell_height=12 * 5, screen=screen)
        self.maze.generate()

        self.pacman = MazePacman(i=0, j=0, sprite_size_x=50, sprite_size_y=50, cycle_time=12 * 20, maze=self.maze)
        self.pacman_sprite = pygame.sprite.GroupSingle(self.pacman)

        self.star_sprites = pygame.sprite.Group()
        for i in range(self.maze.height):
            for j in range(self.maze.width):
                star = Star(i, j, width=8, maze=self.maze)
                self.star_sprites.add(star)


        '''self.ghost = Ghost(x=145, y=220, frames=(('data/sprites/ghosts/ghost_up1.png', ), ),
                           sprite_size=50, cycle_iterations=12, cycle_time=360, step=60)
        self.ghost_sprites = pygame.sprite.Group()
        self.ghost_sprites.add(self.ghost)'''

    def draw(self, screen):
        self.maze.draw()
        self.star_sprites.draw(screen)
        self.pacman_sprite.draw(screen)
        # self.ghost_sprites.draw(screen)

    def update(self):
        blocks_hit_list = pygame.sprite.spritecollide(self.pacman, self.star_sprites, True)
        for block in blocks_hit_list:
            self.score += 1
        self.pacman.update()
        self.star_sprites.update()
        # self.ghost_sprites.update()

    def handle(self, event):
        self.pacman.handle(event)
