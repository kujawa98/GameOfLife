from setup import *


def draw(cells):
    window.fill(WHITE)
    draw_board(cells)
    draw_menu()


def draw_grid():
    for i in range(0, BOARD_WIDTH + 1):
        pygame.draw.line(window, BLACK, (i * CELL_WIDTH, 0), (i * CELL_WIDTH, WINDOW_HEIGHT - 80))
    for i in range(0, BOARD_HEIGHT + 1):
        pygame.draw.line(window, BLACK, (0, i * CELL_HEIGHT), (WINDOW_WIDTH, i * CELL_HEIGHT))


def draw_board(cells):
    for i in cells:
        for cell in i:
            if cell.is_alive:
                pygame.draw.rect(window, BLACK, (cell.x * CELL_WIDTH, cell.y * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT),2)


def draw_menu():
    pygame.draw.rect(window, BLACK,
                     (WINDOW_WIDTH // 2 - 75, WINDOW_HEIGHT - MENU_HEIGHT + (MENU_HEIGHT - 56) // 2, 150, 56), 3,
                     border_radius=100)
    pygame.draw.rect(window, BLACK,
                     (WINDOW_WIDTH // 2 + 100, WINDOW_HEIGHT - MENU_HEIGHT + (MENU_HEIGHT - 40) // 2, 100, 40), 3,
                     border_radius=100)
    pygame.draw.rect(window, BLACK,
                     (WINDOW_WIDTH // 2 - 200, WINDOW_HEIGHT - MENU_HEIGHT + (MENU_HEIGHT - 40) // 2, 100, 40), 3,
                     border_radius=100)


def clear():
    draw_grid()
