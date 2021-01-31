import pygame
from GameFiles.SpritesClasses import PacmanSprite


class Pacman(PacmanSprite):
    def __init__(self, x, y, sprite_size, cycle_iterations, cycle_time, step):
        super().__init__(x, y, sprite_size, cycle_iterations, cycle_time, step)

    def update(self):
        key_state = pygame.key.get_pressed()

        if self.cycle:
            self.check_cycle()
        else:
            if key_state[pygame.K_d]:
                self.cycle = True
                self.direction = (1, 0)
                self.rotation = 0
            elif key_state[pygame.K_w]:
                self.cycle = True
                self.direction = (0, -1)
                self.rotation = 1
            elif key_state[pygame.K_a]:
                self.cycle = True
                self.direction = (-1, 0)
                self.rotation = 2
            elif key_state[pygame.K_s]:
                self.cycle = True
                self.rotation = 3
                self.direction = (0, 1)
