from setup import *
from random import choice


def draw(cells):
    window.fill(BLACK)
    draw_board(cells)


def draw_board(cells):
    for i in cells:
        for cell in i:
            if cell.is_alive:
                pygame.draw.circle(window, choice(COLORS),
                                   (cell.x * CELL_DIAMETER + CELL_RADIUS, cell.y * CELL_DIAMETER + CELL_RADIUS),
                                   CELL_RADIUS)
