import pygame
from random import randint

from GameFiles.Maze import Maze
from GameFiles.Pacman import MazePacman
from GameFiles.Star import Star
from GameFiles.Ghost import MazeGhost
from Responders.GameResponder import GameResponder


class Game:
    def __init__(self, screen):
        self.score = 0
        self.responder = GameResponder(self)
        self.create_maze(screen)
        self.create_pacman()
        self.create_ghosts()
        self.create_stars()

    def create_stars(self):
        self.star_sprites = pygame.sprite.Group()
        for i in range(self.maze.height):
            for j in range(self.maze.width):
                star = Star(i, j, width=8, maze=self.maze)
                self.star_sprites.add(star)

    def create_pacman(self):
        self.pacman = MazePacman(i=0, j=0, sprite_size_x=50, sprite_size_y=50, cycle_time=12 * 20, maze=self.maze)
        self.pacman_sprite = pygame.sprite.GroupSingle(self.pacman)

    def create_maze(self, screen):
        # We use 12 *, just because it is better for game. If you choose something like 77 or 113, game will be started,
        # but you can find some problems, because of float numbers, that will be in GeneralSprite.
        self.maze = Maze(x=20, y=100, height=8, width=16, cell_width=12 * 5, cell_height=12 * 5, screen=screen,
                         density=20, game=self)
        self.maze.generate()

    def draw(self, screen):
        self.maze.draw()
        self.star_sprites.draw(screen)
        self.pacman_sprite.draw(screen)
        self.ghost_sprites.draw(screen)

    def update(self):
        blocks_hit_list = pygame.sprite.spritecollide(self.pacman, self.star_sprites, True)
        for block in blocks_hit_list:
            self.score += 1
        self.pacman.update()
        self.ghost_sprites.update()
        self.star_sprites.update()
        self.ghost_sprites.update()

    def handle(self, event):
        self.pacman.handle(event)
        for ghost in self.ghosts:
            ghost.update()

    def create_ghosts(self):
        self.ghosts = list()
        self.ghost_sprites = pygame.sprite.Group()

        ghosts_colors = ["red", "blue", "orange", "pink"]
        max_precisions = [2, 4, 7, 10]
        min_ways = [15, 13, 10, 7]
        recount_times = [randint(3, 7) for i in range(4)]

        info = [(ghosts_colors[i], max_precisions[i], min_ways[i], recount_times[i]) for i in range(4)]
        for color, precision, min_way, recount_time in info:
            i, j = self.responder.generate_ghost_place(min_way)
            self.ghosts.append(
                MazeGhost(i=i, j=j, sprite_size_x=50, sprite_size_y=50, cycle_time=12 * 32, maze=self.maze,
                          color=color, max_precision=precision, recount_time=recount_time))
            self.ghost_sprites.add(self.ghosts[-1])
