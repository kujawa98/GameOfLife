from setup import *


def draw(cells, iteration):
    window.fill(BLUE)
    draw_board(cells)
    draw_menu()
    write(iteration)


def draw_board(cells):
    for i in cells:
        for cell in i:
            if cell.is_alive:
                pygame.draw.rect(window, WHITE, (cell.x * CELL_WIDTH, cell.y * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT))


def draw_menu():
    pygame.draw.rect(window, LIMON, (0, 570, WINDOW_WIDTH, 150))


def write(iteration):
    it = FONT.render("Iteration     " + str(iteration), True, (0, 0, 0))
    space = FONT.render("Space     to     pause", True, (0, 0, 0))
    c = FONT.render("C    to     clear    screen", True, (0, 0, 0))
    n = FONT.render("N     to     next    step", True, (0, 0, 0))
    r = FONT.render("R     to     randomize",True,(0, 0, 0))
    window.blit(it, (100, 585))
    window.blit(space, (500, 585))
    window.blit(c, (500, 615))
    window.blit(n, (500, 645))
    window.blit(r, (500, 675))
