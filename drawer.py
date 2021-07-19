from setup import *
import pygame


def draw(cells, window):
    window.fill(BLACK)
    draw_board(cells, window)


def draw_board(cells, window):
    for i in cells:
        for cell in i:
            cell.draw(window)


def color(cell):
    plc = cell.x * CELL_DIAMETER + CELL_RADIUS
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
