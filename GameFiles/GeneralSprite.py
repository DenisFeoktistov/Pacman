import pygame


class GeneralSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, sprite_size, cycle_iterations, cycle_time, step, frames):
        super().__init__()

        self.image_counter = 0
        self.sprite_size = sprite_size
        self.image = pygame.image.load(frames[0][0])
        self.transform_image()

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.cycle_iterations = cycle_iterations
        self.cycle_time = cycle_time
        self.cycle_counter = 0
        self.cycle = False

        self.clock = pygame.time.Clock()
        self.timer = 0
        self.reset_timer()

        self.direction = (0, 0)
        self.step = step

        self.frames = frames
        self.rotation = 0

    def reset_timer(self):
        self.timer = self.cycle_time / self.cycle_iterations

    def check_cycle(self):
        self.timer -= self.clock.tick()

        if self.timer <= 0:
            if self.cycle_counter % (self.cycle_iterations // 4) == 0:
                self.animation()
            self.move(self.direction, self.step / self.cycle_iterations)
            self.cycle_counter += 1
            self.reset_timer()

            if self.cycle_counter == self.cycle_iterations:
                self.cycle_counter = 0
                self.cycle = False

    def move(self, duration, step):

        self.rect.x += duration[0] * step
        self.rect.y += duration[1] * step

    def animation(self):
        self.image = pygame.image.load(self.frames[self.rotation][self.image_counter])
        self.transform_image()
        self.image_counter = (self.image_counter + 1) % len(self.frames[self.rotation])

    def transform_image(self):
        self.image.set_colorkey(self.image.get_at((0, 0)))
        self.image = pygame.transform.scale(self.image, (self.sprite_size, self.sprite_size))
