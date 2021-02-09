import pygame

import SubsidiaryFiles.Sounds as Sounds
from random import randint
import datetime as dt


class GameResponder:
    def __init__(self, game):
        self.game = game

    def generate_ghost_place(self, min_way):
        # this method generate place for ghost and a way from this place to pacman (0, 0) includes more than min_way
        # cells.
        i = randint(0, self.game.maze.height - 1)
        j = randint(0, self.game.maze.width - 1)

        while len(self.game.maze.way(i, j, 0, 0)) < min_way:
            i = randint(0, self.game.maze.height - 1)
            j = randint(0, self.game.maze.width - 1)

        return i, j

    def get_target(self, precision, follow_pacman):
        # this method return cell coordinates like pacman.i += precision, pacman.j += precision

        if follow_pacman:
            i = max(0, min(self.game.maze.height - 1, self.game.pacman.i + randint(-precision, precision)))
            j = max(0, min(self.game.maze.width - 1, self.game.pacman.j + randint(-precision, precision)))
        else:
            i = randint(0, self.game.maze.height - 1)
            j = randint(0, self.game.maze.width - 1)
        return i, j

    def check_pacman_collides_star(self):
        for star in self.game.star_sprites:
            if pygame.sprite.collide_mask(self.game.pacman, star):
                self.game.points -= 1
                star.kill()
                Sounds.chomp_sound.play()

    def check_pacman_collides_ghost(self):
        # actually, this method realized in self.lose_check()
        pass

    def lose(self):
        self.game.pacman.die()
        self.game.lose = True
        self.game.end_time = dt.datetime.now()

        self.kill_ghosts()

    def win_check(self):
        if not self.game.star_sprites:
            self.win()

    def win(self):
        self.game.win = True
        self.game.end_time = dt.datetime.now()

    def lose_check(self):
        for ghost in self.game.ghost_sprites:
            if pygame.sprite.collide_mask(self.game.pacman, ghost):
                self.lose()

    def kill_ghosts(self):
        self.game.ghost_sprites.empty()

    def get_minutes(self):
        if not (self.game.lose or self.game.win):
            return ((dt.datetime.now() - self.game.start_time).seconds // 60) % 60
        return ((self.game.end_time - self.game.start_time).seconds // 60) % 60

    def get_seconds(self):
        if not (self.game.lose or self.game.win):
            return (dt.datetime.now() - self.game.start_time).seconds % 60
        return (self.game.end_time - self.game.start_time).seconds % 60
