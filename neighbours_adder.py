from setup import BOARD_HEIGHT, BOARD_WIDTH


def add_neighbour(cells, cell, norm):
    for i in range(-1, 2):
        for j in range(-1, 2):
            cll = cells[(cell.y + i) % BOARD_HEIGHT][(cell.x + j) % BOARD_WIDTH]
            if i == 0:
                if j != 0:
                    cll.neighbours += 1 * norm
            else:
                cll.neighbours += 1 * norm
