import pygame
from GameFiles.SpritesClasses import PacmanSprite


class Pacman(PacmanSprite):
    def __init__(self, x, y, sprite_size, cycle_time, step):
        super().__init__(x, y, sprite_size, cycle_time)
        self.step = step

    def handle(self, event):
        pass

    def update(self):
        super().update()
        key_state = pygame.key.get_pressed()

        if key_state[pygame.K_d]:
            self.start_moving(self.step, 0)
        elif key_state[pygame.K_w]:
            self.start_moving(0, -self.step)
        elif key_state[pygame.K_a]:
            self.start_moving(-self.step, 0)
        elif key_state[pygame.K_s]:
            self.start_moving(0, self.step)
