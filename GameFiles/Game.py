import pygame


from GameFiles.Maze import Maze


class Game:
    def __init__(self, screen):
        self.maze = Maze(0, 0, screen)
        self.maze.generate()

    def draw(self):
        self.maze.draw()
