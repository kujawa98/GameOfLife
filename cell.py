import pygame
from setup import *

# Basic cell class
class Cell:
    def __init__(self, x, y):
        self.is_alive = False
        self.x = x
        self.y = y
        #every cell has its own rectangle that's controlling its rendering
        self.rect = pygame.Rect(self.x * CELL_DIAMETER, self.y * CELL_DIAMETER, CELL_DIAMETER, CELL_DIAMETER)
        self.will_be_alive = False
        #living neighbours count
        self.neighbours = 0
        self.color = self.color()

    def kill(self):
        self.will_be_alive = False

    def revive(self):
        self.will_be_alive = True

    def update(self):
        self.is_alive = self.will_be_alive

    #color resolving method based on cell x coordinate
    def color(self):
        plc = self.x * CELL_DIAMETER + CELL_RADIUS
        offset = WINDOW_WIDTH // 6
        if plc < offset:
            return RED
        elif plc < 2 * offset:
            return ORANGE
        elif plc < 3 * offset:
            return YELLOW
        elif plc < 4 * offset:
            return GREEN
        elif plc < 5 * offset:
            return BLUE
        else:
            return PURPLE

    def draw(self, window):
        if self.is_alive:
            pygame.draw.circle(window, self.color, self.rect.center, CELL_RADIUS)
        else:
            pygame.draw.circle(window, WHITE, self.rect.center, 1, 1)
