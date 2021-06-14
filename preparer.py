from setup import BOARD_HEIGHT, BOARD_WIDTH
from generator import add_neighbour, sub_neighbour


def next_state(cells):
    for row in cells:
        for cell in row:
            if cell.neighbours > 0:
                nei = neighboors(cells, cell)
                if (nei > 3 or nei < 2) and cell.is_alive:
                    cell.kill()
                elif nei == 3 and not cell.is_alive:
                    cell.revive()
                else:
                    pass
            elif cell.neighbours == 0 and cell.is_alive:
                cell.kill()

    for row in cells:
        for cell in row:
            prev = cell.is_alive
            cell.iterate()
            if cell.is_alive and cell.is_alive != prev:
                add_neighbour(cells, cell)
            elif not cell.is_alive and cell.is_alive != prev:
                sub_neighbour(cells, cell)


def neighboors(cells, cell):
    how_many = -1 if cell.is_alive else 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if cells[(cell.y + i) % BOARD_HEIGHT][(cell.x + j) % BOARD_WIDTH].is_alive:
                how_many += 1
    return how_many
