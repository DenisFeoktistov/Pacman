import pygame
from GameFiles.GeneralSprite import GeneralSprite


class Ghost(GeneralSprite):
    def __init__(self, x, y, frames, sprite_size, cycle_iterations, cycle_time, step):
        super().__init__(x, y, frames, sprite_size, cycle_iterations, cycle_time, step)

    def update(self):
        if self.cycle:
            self.check_cycle()
        else:
            self.cycle = True
            self.direction = (0, 1)
