from setup import BOARD_HEIGHT, BOARD_WIDTH
from cell import Cell
from random import choice


def generate_cells():
    cells = [[Cell(i, j, False) for i in range(BOARD_WIDTH)] for j in range(BOARD_HEIGHT)]
    for row in cells:
        for cell in row:
            state = choice([True, False, False, False])
            if state:
                cell.is_alive = True
                add_neighbour(cells, cell)
    return cells


def add_neighbour(cells, cell):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0:
                if j != 0:
                    cells[(cell.y + i) % BOARD_HEIGHT][(cell.x + j) % BOARD_WIDTH].neighbours += 1
            else:
                cells[(cell.y + i) % BOARD_HEIGHT][(cell.x + j) % BOARD_WIDTH].neighbours += 1


def sub_neighbour(cells, cell):
    for i in range(-1, 2):
        for j in range(-1, 2):
            cll = cells[(cell.y + i) % BOARD_HEIGHT][(cell.x + j) % BOARD_WIDTH]
            if i == 0:
                if j != 0:
                    cll.neighbours -= 1
            else:
                cll.neighbours -= 1
