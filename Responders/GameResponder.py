import pygame

import SubsidiaryFiles.Sounds as Sounds
from random import randint


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

    def get_target(self, precision):
        # this method return cell coordinates like pacman.i += precision, pacman.j += precision

        i = max(0, min(self.game.maze.height - 1, self.game.pacman.i + randint(-precision, precision)))
        j = max(0, min(self.game.maze.width - 1, self.game.pacman.j + randint(-precision, precision)))
        return i, j

    def check_pacman_collides_star(self):
        pygame.mixer.init()
        for star in self.game.star_sprites:
            if pygame.sprite.collide_mask(self.game.pacman, star):
                star.kill()
                Sounds.chomp_sound.play()

    def check_pacman_collides_ghost(self):
        for ghost in self.game.ghost_sprites:
            if pygame.sprite.collide_mask(self.game.pacman, ghost):
                self.end_of_the_game()

    def end_of_the_game(self):
        self.game.pacman.die()
        self.game.ended = True

        self.kill_ghosts()

    def kill_ghosts(self):
        self.game.ghost_sprites.empty()
