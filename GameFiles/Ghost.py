import pygame
from GameFiles.SpritesClasses import GhostSprite


class MazeGhost(GhostSprite):
    def __init__(self, i, j, sprite_size_x, sprite_size_y, cycle_time, color, maze):
        self.i = i
        self.j = j
        self.maze = maze

        x = maze.x + maze.cell_width * j + maze.cell_width / 2 - sprite_size_x / 2  # last part for centered position
        y = maze.y + maze.cell_height * i + maze.cell_height / 2 - sprite_size_y / 2  # last part for centered position
        super().__init__(x, y, sprite_size_x, sprite_size_y, cycle_time, color)

        self.step_x = maze.cell_width
        self.step_y = maze.cell_height

        self.way = list()

    def update(self):
        super().update()

        if self.way:
            if not self.in_cycle():
                next_cell = self.way.pop(0)

                v1 = self.step_x * (next_cell[1] - self.j)
                v2 = self.step_y * (next_cell[0] - self.i)
                self.start_moving(self.step_x * (next_cell[1] - self.j), self.step_y * (next_cell[0] - self.i))
                self.i, self.j = next_cell
        else:
            target = self.maze.game.responder.get_target()
            self.way = self.maze.way(self.i, self.j, target[0], target[1])[:10]
