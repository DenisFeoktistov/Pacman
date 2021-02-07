import pygame


class Star(pygame.sprite.Sprite):
    def __init__(self, i, j, width, maze):
        super().__init__()

        self.width = width
        self.maze = maze

        self.image = pygame.Surface((self.width, self.width))
        self.image.fill((255, 255, 150))

        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()

        self.positioning(i, j)

    def positioning(self, i, j):
        self.rect.x = self.maze.x + (self.maze.cell_width * j) + ((self.maze.cell_width - self.width) // 2)
        self.rect.y = self.maze.y + (self.maze.cell_height * i) + ((self.maze.cell_height - self.width) // 2)

    def handle(self, event):
        # yes, it is empty method, but we think, that it is logical better to have method like that, even if it is
        # doing nothing
        pass
