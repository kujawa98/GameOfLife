from neighbours_adder import add_neighbour
from setup import BOARD_HEIGHT, BOARD_WIDTH
from cell import Cell
from random import choice


def generate_cells():
    cells = [[Cell(i, j, False) for i in range(BOARD_WIDTH)] for j in range(BOARD_HEIGHT)]
    for row in cells:
        for cell in row:
            if choice([True, False, False, False]):
                cell.is_alive = True
                add_neighbour(cells, cell, 1)
    return cells
