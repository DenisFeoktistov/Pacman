import pygame


from GameFiles.Maze import Maze


class Game:
    def __init__(self, screen):

        self.maze = Maze(x=20, y=100, width=16, height=8, cell_width=60, cell_height=60, screen=screen)
        self.maze.generate()

    def draw(self):
        self.maze.draw()
