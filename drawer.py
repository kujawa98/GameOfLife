from setup import *


def draw(cells):
    window.fill(WHITE)
    draw_board(cells)


def draw_board(cells):
    for i in cells:
        for cell in i:
            if cell.is_alive:
                pygame.draw.rect(window, BLACK, (cell.x * CELL_WIDTH, cell.y * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT), 2)
