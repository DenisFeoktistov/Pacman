import random
import pygame


class Cell:
    COLOR = (138, 43, 226)
    LINE_WIDTH = 7

    def __init__(self, x, y, width, height, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen

        self.left = True
        self.right = True
        self.top = True
        self.bottom = True

    def draw(self):
        if self.left:
            pygame.draw.line(self.screen, Cell.COLOR, (self.x, self.y), (self.x, self.y + self.height), Cell.LINE_WIDTH)
        if self.right:
            pygame.draw.line(self.screen, Cell.COLOR, (self.x + self.width, self.y),
                             (self.x + self.width, self.y + self.height), Cell.LINE_WIDTH)
        if self.top:
            pygame.draw.line(self.screen, Cell.COLOR, (self.x, self.y), (self.x + self.width, self.y), Cell.LINE_WIDTH)
        if self.bottom:
            pygame.draw.line(self.screen, Cell.COLOR, (self.x, self.y + self.height),
                             (self.x + self.width, self.y + self.height), Cell.LINE_WIDTH)

    def set_randomly(self, chance):
        values = [random.choices([True, False], weights=[chance, 100 - chance], k=1)[0] for _ in range(4)]
        self.left = values[0]
        self.right = values[1]
        self.top = values[2]
        self.bottom = values[3]

    # actually, it is ok to return a bool, but method is better, at least because its name is more understandably
    def get_left_border(self):
        return self.left

    def get_right_border(self):
        return self.right

    def get_top_border(self):
        return self.top

    def get_bottom_border(self):
        return self.bottom

    def set_left_border(self, value):
        self.left = value

    def set_right_border(self, value):
        self.right = value

    def set_top_border(self, value):
        self.top = value

    def set_bottom_border(self, value):
        self.bottom = value


class Maze:
    DFS_COLOR = 1
    CHANCE_VALUE = 40

    def __init__(self, x, y, width, height, cell_width, cell_height, screen, game):
        self.x = x
        self.y = y

        self.width = width
        self.height = height
        self.cell_width = cell_width
        self.cell_height = cell_height

        self.screen = screen
        self.game = game

        self.matrix = [[Cell(self.x + cell_width * j, self.y + cell_height * i, cell_width, cell_height, self.screen)
                        for j in range(self.width)] for i in range(self.height)]
        self.nearby = self.update_nearby_list()

    def generate(self):
        # I am sure, that's my algorithm isn't perfect, but I found it the easiest.
        # I regenerate all cells, that aren't attainable from the (0, 0), (regenerate_some_cells) and
        # I regenerate some boards that are between attainable cells and not attainable cells ('cause sometimes
        # only regenerating not attainable wouldn't work, 'cause two cells got two borders between and it can
        # disturb)(remove_some_boards_in_maze).

        # I am using DFS in this, so i need color matrix and list of related vertices.
        color_matrix = self.update_color_matrix()
        self.nearby = self.update_nearby_list()

        while not self.check(color_matrix):
            self.remove_some_boards_in_maze(color_matrix)
            self.regenerate_some_cells(color_matrix)

            color_matrix = self.update_color_matrix()
            self.nearby = self.update_nearby_list()

        self.add_borders()

    def regenerate_some_cells(self, color_matrix):
        for i in range(self.height):
            for j in range(self.width):
                if color_matrix[i][j] != Maze.DFS_COLOR:
                    self.matrix[i][j].set_randomly(Maze.CHANCE_VALUE)

    def get_nearby_cells(self, i, j):
        # Maybe it is a little bit strange, but I don't find a way to improve it
        answer = list()

        actual = i, j  # Sometimes I use i, j, because [i][j] is better than [actual[0]][actual[1]]. Yes, it would be
        # better, but int this code part it can only make code less readable.
        if self.has_left_cell(*actual):
            if not self.matrix[i][j].get_left_border() and not self.get_left_cell(*actual).get_right_border():
                answer.append((i, j - 1))
        if self.has_right_cell(*actual):
            if not self.matrix[i][j].get_right_border() and not self.get_right_cell(*actual).get_left_border():
                answer.append((i, j + 1))
        if self.has_top_cell(*actual):
            if not self.matrix[i][j].get_top_border() and not self.get_top_cell(*actual).get_bottom_border():
                answer.append((i - 1, j))
        if self.has_bottom_cell(*actual):
            if not self.matrix[i][j].get_bottom_border() and not self.get_bottom_cell(*actual).get_top_border():
                answer.append((i + 1, j))
        return answer

    def check(self, color_matrix):
        self.DFS(0, 0, color_matrix)  # coloring

        # then checking
        for j in range(self.width):
            for i in range(self.height):
                if color_matrix[i][j] != Maze.DFS_COLOR:
                    return False
        return True

    def DFS(self, i, j, color_matrix):
        # simple DFS
        color_matrix[i][j] = Maze.DFS_COLOR
        for next in self.nearby[i][j]:
            if color_matrix[next[0]][next[1]] != Maze.DFS_COLOR:
                self.DFS(next[0], next[1], color_matrix)

    def remove_some_boards_in_maze(self, color_matrix):
        for i in range(self.height):
            for j in range(self.width):
                if color_matrix[i][j] != Maze.DFS_COLOR:
                    self.remove_some_boards_for_cell(i, j)

    def remove_some_boards_for_cell(self, i, j):
        # Maybe it is a little bit strange, but I don't find a way to improve it
        chance = Maze.CHANCE_VALUE
        values = [random.choices([True, False], weights=[chance, 100 - chance], k=1)[0] for _ in range(4)]

        actual = i, j
        if self.has_left_cell(*actual) and self.get_left_cell(*actual).get_right_border():
            self.get_left_cell(*actual).set_right_border(values[0])
        if self.has_right_cell(*actual) and self.get_right_cell(*actual).get_left_border():
            self.get_right_cell(*actual).set_left_border(values[1])
        if self.has_top_cell(*actual) and self.get_top_cell(*actual).get_bottom_border():
            self.get_top_cell(*actual).set_bottom_border(values[2])
        if self.has_bottom_cell(*actual) and self.get_bottom_cell(*actual).get_top_border():
            self.get_bottom_cell(*actual).set_bottom_border(values[3])

    def update_nearby_list(self):
        return [[self.get_nearby_cells(i, j) for j in range(self.width)] for i in range(self.height)]

    def update_color_matrix(self):
        return [[-1 for j in range(self.width)] for i in range(self.height)]

    def add_borders(self):
        for i in range(self.width):
            self.matrix[0][i].set_top_border(True)
        for i in range(self.width):
            self.matrix[self.height - 1][i].set_bottom_border(True)
        for i in range(self.height):
            self.matrix[i][0].set_left_border(True)
        for i in range(self.height):
            self.matrix[i][self.width - 1].set_right_border(True)

    def draw(self):
        for i in range(self.height):
            for j in range(self.width):
                self.matrix[i][j].draw()

    def has_left_cell(self, i, j):
        return j > 0

    def has_right_cell(self, i, j):
        return j < self.width - 1

    def has_top_cell(self, i, j):
        return i > 0

    def has_bottom_cell(self, i, j):
        return i < self.height - 1

    def get_right_cell(self, i, j):
        return self.matrix[i][j + 1]

    def get_left_cell(self, i, j):
        return self.matrix[i][j - 1]

    def get_top_cell(self, i, j):
        return self.matrix[i - 1][j]

    def get_bottom_cell(self, i, j):
        return self.matrix[i + 1][j]

    def way(self, i1, j1, i2, j2):
        way = list()

        visited = [[False for j in range(self.width)] for i in range(self.height)]
        visited[i1][j1] = True
        prev = [[-1 for j in range(self.width)] for i in range(self.height)]
        queue = list()
        queue.append((i1, j1))

        while queue:
            actual = queue.pop(0)
            for nearby in self.nearby[actual[0]][actual[1]]:
                if not visited[nearby[0]][nearby[1]]:
                    queue.append((nearby[0], nearby[1]))
                    visited[nearby[0]][nearby[1]] = True
                    prev[nearby[0]][nearby[1]] = actual

        while not (i2, j2) == (i1, j1):
            way.append((i2, j2))
            i2, j2 = prev[i2][j2]

        way.reverse()
        return way
