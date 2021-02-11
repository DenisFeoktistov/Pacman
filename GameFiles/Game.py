import pygame
from random import randint
import datetime as dt

from GameFiles.Maze import Maze
from GameFiles.Pacman import MazePacman
from GameFiles.Star import Star
from GameFiles.Ghost import MazeGhost
from Responders.GameResponder import GameResponder


class Game:
    def __init__(self, screen):
        # datetime for timer
        self.start_time = dt.datetime.now()
        self.end_time = dt.datetime.now()

        self.screen = screen

        self.responder = GameResponder(self)

        self.create_components()

        self.lose = False
        self.win = False
        self.score = 0
        self.points = len(self.star_sprites.sprites())

    def create_components(self):
        self.create_maze(self.screen)
        self.create_pacman()
        self.create_ghosts()
        self.create_stars()

    def restart(self):
        self.start_time = dt.datetime.now()
        self.end_time = dt.datetime.now()

        self.create_components()

        self.lose = False
        self.win = False
        self.score = 0
        self.points = len(self.star_sprites.sprites())

    def create_stars(self):
        self.stars = list()
        self.star_sprites = pygame.sprite.Group()
        for i in range(self.maze.height):
            for j in range(self.maze.width):
                if not (i == self.pacman.i and j == self.pacman.j):
                    star = Star(i, j, width=8, maze=self.maze)
                    self.star_sprites.add(star)
                    self.stars.append(star)

    def create_pacman(self):
        self.pacman = MazePacman(i=0, j=0, sprite_size_x=50, sprite_size_y=50, cycle_time=12 * 20,
                                 dead_cycle_time=12 * 40, maze=self.maze)
        self.pacman_sprite = pygame.sprite.GroupSingle(self.pacman)

    def create_maze(self, screen):
        # We use 12 *, just because it is better for game. If you choose something like 77 or 113, game will be started,
        # but you can find some problems, because of float numbers, that will be in GeneralSprite.
        self.maze = Maze(x=10, y=100, height=8, width=16, cell_width=12 * 5, cell_height=12 * 5, screen=screen,
                         density=20, game=self)
        self.maze.generate()

    def draw(self, screen):
        self.maze.draw()
        self.star_sprites.draw(screen)
        self.pacman_sprite.draw(screen)
        self.ghost_sprites.draw(screen)

    def update(self):
        if not self.lose and not self.win:
            self.responder.check_pacman_collides_star()
            self.responder.check_pacman_collides_ghost()

            self.responder.lose_check()
            self.responder.win_check()

            self.ghost_sprites.update()
            self.star_sprites.update()
            self.pacman.update()
        elif self.lose:
            self.pacman.update()
        else:
            pass

    def handle(self, event):
        self.pacman.handle(event)
        for ghost in self.ghosts:
            ghost.handle(event)
        for star in self.stars:
            star.handle(event)

    def create_ghosts(self):
        self.ghosts = list()
        self.ghost_sprites = pygame.sprite.Group()

        ghosts_colors = ["red", "blue", "orange", "pink"]
        # precisions shows range in which ghost can choose cell to go, if the ghost is following pacman
        max_precisions = [2, 4, 7, 10]
        # it is parameter that shows minimum way from ghost to pacman at the start of the game
        min_ways = [15, 13, 10, 7]
        # every "recount_time" ghost will choose new cell for following
        recount_times = [randint(7, 12) for i in range(4)]
        follow_pacman = [False, False, True, False]

        info = [(ghosts_colors[i], max_precisions[i], min_ways[i], recount_times[i], follow_pacman[i]) for i in
                range(4)]
        for color, precision, min_way, recount_time, follow_pacman in info:
            i, j = self.responder.generate_ghost_place(min_way)
            self.ghosts.append(
                MazeGhost(i=i, j=j, sprite_size_x=50, sprite_size_y=50, cycle_time=12 * 40, maze=self.maze,
                          color=color, max_precision=precision, recount_time=recount_time, follow_pacman=follow_pacman))
            self.ghost_sprites.add(self.ghosts[-1])
