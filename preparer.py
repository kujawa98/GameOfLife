from setup import BOARD_HEIGHT, BOARD_WIDTH


def next_state(cells):
    new_cells = cells.copy()
    for i, row in enumerate(cells):
        for j, cell in enumerate(row):
            nei = neighboors(cells, cell)
            if (nei > 3 or nei < 2) and cell.is_alive:
                new_cells[i][j].kill()
            elif nei == 3 and not cell.is_alive:
                new_cells[i][j].revive()
            else:
                pass
    for i, row in enumerate(cells):
        for j, cell in enumerate(row):
            new_cells[i][j].iterate()
    return new_cells


def neighboors(cells, cell):
    how_many = -1 if cell.is_alive else 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if cells[(cell.y + i) % BOARD_HEIGHT][(cell.x + j) % BOARD_WIDTH].is_alive:
                how_many += 1
    return how_many
