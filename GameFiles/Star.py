import pygame


class Star(pygame.sprite.Sprite):
    def __init__(self, i, j, width, maze):
        super().__init__()

        self.width = width
        self.maze = maze

        self.image = pygame.Surface((self.width, self.width))
        self.image.fill('white')

        self.rect = self.image.get_rect()

        self.positioning(i, j)

    def positioning(self, i, j):
        self.rect.x = self.maze.x + (self.maze.cell_width * j) + ((self.maze.cell_width - self.width) // 2)
        self.rect.y = self.maze.y + (self.maze.cell_height * i) + ((self.maze.cell_height - self.width) // 2)
        print(1)
