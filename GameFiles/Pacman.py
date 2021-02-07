import pygame
from GameFiles.SpritesClasses import PacmanSprite


class Pacman(PacmanSprite):
    # We won't use this class, but it is a good prototype, so we will just leave it here :)
    def __init__(self, x, y, sprite_size_x, sprite_size_y, cycle_time, step_x, step_y):
        super().__init__(x, y, sprite_size_x, sprite_size_y, cycle_time)
        self.step_x = step_x
        self.step_y = step_y

    def update(self):
        super().update()
        key_state = pygame.key.get_pressed()

        if key_state[pygame.K_d]:
            self.start_moving(self.step_x, 0)
        elif key_state[pygame.K_w]:
            self.start_moving(0, -self.step_y)
        elif key_state[pygame.K_a]:
            self.start_moving(-self.step_x, 0)
        elif key_state[pygame.K_s]:
            self.start_moving(0, self.step_y)


class MazePacman(PacmanSprite):
    def __init__(self, i, j, sprite_size_x, sprite_size_y, cycle_time, maze):
        self.i = i
        self.j = j
        self.maze = maze

        x = maze.x + maze.cell_width * j + maze.cell_width / 2 - sprite_size_x / 2  # last part for centered position
        y = maze.y + maze.cell_height * i + maze.cell_height / 2 - sprite_size_y / 2  # last part for centered position
        super().__init__(x, y, sprite_size_x, sprite_size_y, cycle_time)
        self.step_x = maze.cell_width
        self.step_y = maze.cell_height

    def update(self):
        super().update()
        key_state = pygame.key.get_pressed()

        # second if in every part is checking that pacman can go (there is no wall on his way).
        # yes, may be it is better not to use self.maze.nearby, because it is attribute of class, but we didn't find a
        # better way (because in Python we can't do method, that returns const link to list or something like that).
        # May be we should make a method like "way_from(self, i1, j2, i2, j2), but... We weren't sure, so we made this"
        if key_state[pygame.K_d]:
            if (self.i, self.j + 1) in self.maze.nearby[self.i][self.j]:
                if not self.in_cycle():
                    self.j += 1
                    self.start_moving(self.step_x, 0)
        elif key_state[pygame.K_w]:
            if (self.i - 1, self.j) in self.maze.nearby[self.i][self.j]:
                if not self.in_cycle():
                    self.i -= 1
                    self.start_moving(0, -self.step_y)
        elif key_state[pygame.K_a]:
            if (self.i, self.j - 1) in self.maze.nearby[self.i][self.j]:
                if not self.in_cycle():
                    self.j -= 1
                    self.start_moving(-self.step_x, 0)
        elif key_state[pygame.K_s]:
            if (self.i + 1, self.j) in self.maze.nearby[self.i][self.j]:
                if not self.in_cycle():
                    self.i += 1
                    self.start_moving(0, self.step_y)
