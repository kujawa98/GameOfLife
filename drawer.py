from setup import *


def draw(cells):
    window.fill(BLACK)
    draw_board(cells)


def draw_board(cells):
    for i in cells:
        for cell in i:
            if cell.is_alive:
                pygame.draw.circle(window, color(cell),
                                   (cell.x * CELL_DIAMETER + CELL_RADIUS, cell.y * CELL_DIAMETER + CELL_RADIUS),
                                   CELL_RADIUS)
            else:
                pygame.draw.circle(window, WHITE,
                                   (cell.x * CELL_DIAMETER + CELL_RADIUS, cell.y * CELL_DIAMETER + CELL_RADIUS),
                                   1, 1)


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
