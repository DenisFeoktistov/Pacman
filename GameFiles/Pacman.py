import pygame


class Pacman(pygame.sprite.Sprite):
    SPEED = 4
    FRAMES = ['data\sprites\pacman\pacman_sprite1.png', 'data\sprites\pacman\pacman_sprite2.png',
              'data\sprites\pacman\pacman_sprite3.png']

    def __init__(self, x, y, borders):
        super().__init__()
        self.image = pygame.image.load(Pacman.FRAMES[0])
        self.image.set_colorkey(self.image.get_at((0, 0)))
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.borders = borders

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.last_x = x
        self.last_y = y

        self.counter = 0

    def update(self):
        self.speed = Pacman.SPEED
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_d]:
            self.rotate_image(0)
            self.rect.x += self.speed
        elif keystate[pygame.K_w]:
            self.rotate_image(90)
            self.rect.y -= self.speed
        elif keystate[pygame.K_a]:
            self.rotate_image(180)
            self.rect.x -= self.speed
        elif keystate[pygame.K_s]:
            self.rotate_image(270)
            self.rect.y += self.speed
        if pygame.sprite.spritecollideany(self, self.borders):
            self.rect.x = self.last_x
            self.rect.y = self.last_y
        self.last_x = self.rect.x
        self.last_y = self.rect.y


    def rotate_image(self, angle):
        self.image = pygame.image.load(Pacman.FRAMES[1:][self.counter])
        self.image.set_colorkey(self.image.get_at((0, 0)))
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image = pygame.transform.rotate(self.image, angle)
        self.counter = (self.counter + 1) % len(Pacman.FRAMES[1:])
