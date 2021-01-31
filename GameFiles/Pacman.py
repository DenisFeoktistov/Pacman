import pygame


class Pacman(pygame.sprite.Sprite):
    FRAMES = ['data/sprites/pacman/pacman_sprite1.png', 'data/sprites/pacman/pacman_sprite2.png',
              'data/sprites/pacman/pacman_sprite3.png']

    def __init__(self, x, y, cycle_iterations, cycle_time, step):
        super().__init__()

        self.image_counter = 0
        self.angle = 0
        self.image = pygame.image.load(Pacman.FRAMES[0])
        self.transform_image()

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.duration = (0, 0)
        self.step = step

        self.cycle_iterations = cycle_iterations
        self.cycle_time = cycle_time
        self.clock = pygame.time.Clock()
        self.cycle = False
        self.cycle_counter = 0

        self.timer = 0
        self.reset_timer()

        self.start = False

    def reset_timer(self):
        self.timer = self.cycle_time / self.cycle_iterations

    def check_cycle(self):
        self.timer -= self.clock.tick()

        if self.timer <= 0:
            if self.cycle_counter % (self.cycle_iterations // 4) == 0:
                print(self.cycle_counter)
                self.animation()
            self.move(self.duration, self.step / self.cycle_iterations)
            self.cycle_counter += 1
            self.reset_timer()

            if self.cycle_counter == self.cycle_iterations:
                self.cycle_counter = 0
                self.cycle = False

    def move(self, duration, step):
        if not self.start:
            self.start = True
            self.animation()

        self.rect.x += duration[0] * step
        self.rect.y += duration[1] * step

    def update(self):
        key_state = pygame.key.get_pressed()

        if self.cycle:
            self.check_cycle()
        else:
            if key_state[pygame.K_d]:
                self.cycle = True
                self.duration = (1, 0)
                self.angle = 0
            elif key_state[pygame.K_w]:
                self.cycle = True
                self.duration = (0, -1)
                self.angle = 90
            elif key_state[pygame.K_a]:
                self.cycle = True
                self.duration = (-1, 0)
                self.angle = 180
            elif key_state[pygame.K_s]:
                self.cycle = True
                self.duration = (0, 1)
                self.angle = 270

    def animation(self):
        self.image = pygame.image.load(Pacman.FRAMES[1:][self.image_counter])
        
        self.transform_image()
        self.image_counter = (self.image_counter + 1) % len(Pacman.FRAMES[1:])

    def transform_image(self):
        self.image.set_colorkey(self.image.get_at((0, 0)))
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image = pygame.transform.rotate(self.image, self.angle)
