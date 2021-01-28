import random
import pygame


class Cell:
    WIDTH, HEIGHT = 50, 50
    COLOR = (138, 43, 226)
    LINE_WIDTH = 5

    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen

        self.left = False
        self.right = False
        self.top = False
        self.bottom = False
        self.dict = {"left": self.left, "right": self.right, "top": self.top, "bottom": self.bottom}

    def set_border(self, border):
        try:
            self.dict[border] = True
        except Exception:
            raise Exception(f"Border {border} is not from the list ['left', 'right', 'top', 'bottom']")

    def set_randomly(self, chance):
        self.left = random.choices([True, False], weights=[chance, 100 - chance], k=1)[0]
        self.right = random.choices([True, False], weights=[chance, 100 - chance], k=1)[0]
        self.top = random.choices([True, False], weights=[chance, 100 - chance], k=1)[0]
        self.bottom = random.choices([True, False], weights=[chance, 100 - chance], k=1)[0]

    def draw(self):
        if self.left:
            pygame.draw.line(self.screen, Cell.COLOR, (self.x, self.y), (self.x, self.y + Cell.HEIGHT), Cell.LINE_WIDTH)
        if self.right:
            pygame.draw.line(self.screen, Cell.COLOR, (self.x + self.WIDTH, self.y),
                             (self.x + self.WIDTH, self.y + Cell.HEIGHT), Cell.LINE_WIDTH)
        if self.top:
            pygame.draw.line(self.screen, Cell.COLOR, (self.x, self.y), (self.x + Cell.WIDTH, self.y), Cell.LINE_WIDTH)
        if self.bottom:
            pygame.draw.line(self.screen, Cell.COLOR, (self.x, self.y + Cell.HEIGHT),
                             (self.x + Cell.WIDTH, self.y + Cell.HEIGHT), Cell.LINE_WIDTH)


class Maze:
    WIDTH, HEIGHT = 20, 12

    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen

        self.matrix = [[Cell(self.x + Cell.WIDTH * j, self.y + Cell.HEIGHT * i, self.screen) for j in range(Maze.WIDTH)]
                       for i in range(Maze.HEIGHT)]

    def generate(self):
        for i in range(Maze.HEIGHT):
            for j in range(Maze.WIDTH):
                self.matrix[i][j].set_randomly(30)

    def draw(self):
        for i in range(Maze.HEIGHT):
            for j in range(Maze.WIDTH):
                self.matrix[i][j].draw()
