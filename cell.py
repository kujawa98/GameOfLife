import pygame
from pygame.sprite import Sprite
from setup import *


class Cell(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.is_alive = False
        self.x = x
        self.y = y
        self.will_be_alive = False
        self.neighbours = 0
        self.color = self.color()

    def kill(self):
        self.will_be_alive = False

    def revive(self):
        self.will_be_alive = True

    def update(self):
        self.is_alive = self.will_be_alive

    def color(self):
        plc = self.x * CELL_DIAMETER + CELL_RADIUS
        if plc < 100:
            return RED
        elif plc < 2 * 100:
            return ORANGE
        elif plc < 3 * 100:
            return YELLOW
        elif plc < 4 * 100:
            return GREEN
        elif plc < 5 * 100:
            return BLUE
        else:
            return PURPLE

    def draw(self, window):
        if self.is_alive:
            pygame.draw.circle(window, self.color,
                               (self.x * CELL_DIAMETER + CELL_RADIUS, self.y * CELL_DIAMETER + CELL_RADIUS),
                               CELL_RADIUS)
        else:
            pygame.draw.circle(window, WHITE,
                               (self.x * CELL_DIAMETER + CELL_RADIUS, self.y * CELL_DIAMETER + CELL_RADIUS),
                               1, 1)
