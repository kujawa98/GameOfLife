from setup import *


def draw(cells, iteration):
    window.fill(BLUE)
    draw_board(cells)


def draw_board(cells):
    for i in cells:
        for cell in i:
            if cell.is_alive:
                pygame.draw.circle(window, WHITE,
                                   (cell.x * 2 * CELL_RADIUS + CELL_RADIUS, cell.y * 2 * CELL_RADIUS + CELL_RADIUS),
                                   CELL_RADIUS)
