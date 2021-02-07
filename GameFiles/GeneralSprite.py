import pygame


class GeneralSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, sprite_size_x, sprite_size_y, cycle_iterations, switches_for_cycle, cycle_time,
                 default_frame, frames):
        super().__init__()

        self.sprite_size_x = sprite_size_x
        self.sprite_size_y = sprite_size_y

        self.image_counter = 0
        self.frames = frames
        self.rotation = 0

        self.default_frame = default_frame
        if self.default_frame:
            self.set_default_frame()
        else:
            self.set_frame(self.frames[0][0])

        self.transform_image()

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.switches_for_cycle = switches_for_cycle
        self.cycle_iterations = cycle_iterations
        self.cycle_time = cycle_time
        self.cycle_counter = 0
        self.cycle = False

        self.clock = pygame.time.Clock()
        self.timer = 0
        self.reset_timer()

        self.cycle_v_x = 0
        self.cycle_v_y = 0

    def update(self):
        if self.cycle:
            self.check_cycle()

    def handle(self, event):
        # yes, it is empty method, but we think, that it is logical better to have method like that, even if it is
        # doing nothing
        pass

    def start_moving(self, x, y):
        # it is better to do this check, because it can be something really bad without it
        if not self.cycle:
            self.start_cycle(x, y)

    def in_cycle(self):
        # returning bool is ok as attribute, because it is primitive type and returning value isn't a link, but it is
        # better, we think, to use methods
        return self.cycle

    def start_cycle(self, x, y):
        self.set_rotation(x, y)

        self.cycle_v_x = x / self.cycle_iterations
        self.cycle_v_y = y / self.cycle_iterations

        self.cycle = True
        self.reset_timer()

    def set_rotation(self, x, y):
        if x > 0:
            self.rotation = 0
        elif x < 0:
            self.rotation = 2
        elif y > 0:
            self.rotation = 3
        elif y < 0:
            self.rotation = 1

    def reset_timer(self):
        self.timer = self.cycle_time / self.cycle_iterations

    def iteration_is_over(self):
        return self.timer <= 0

    def check_cycle(self):
        self.timer -= self.clock.tick()

        if self.iteration_is_over():
            self.reset_timer()

            if self.cycle_counter % (self.cycle_iterations // self.switches_for_cycle) == 0:
                self.switch_frame()

            self.move(self.cycle_v_x, self.cycle_v_y)

            self.cycle_counter += 1
            if self.cycle_counter == self.cycle_iterations:
                self.cycle_end()

    def cycle_end(self):
        self.cycle_counter = 0
        self.cycle = False
        self.set_default_frame()

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def set_default_frame(self):
        if self.default_frame:
            self.set_frame(self.default_frame)

    def switch_frame(self):
        self.image_counter = (self.image_counter + 1) % len(self.frames[self.rotation])
        frame = self.frames[self.rotation][self.image_counter]

        self.set_frame(frame)

    def set_frame(self, frame):
        self.image = pygame.image.load(frame)
        self.transform_image()
        self.mask = pygame.mask.from_surface(self.image)

    def transform_image(self):
        self.image.set_colorkey(self.image.get_at((0, 0)))
        self.image = pygame.transform.scale(self.image, (self.sprite_size_x, self.sprite_size_y))
