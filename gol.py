from setup import *
from drawer import draw
from preparer import next_state
from cell import Cell


def main():
    cells = [[Cell(i, j) for i in range(BOARD_WIDTH)] for j in range(BOARD_HEIGHT)]
    clock = pygame.time.Clock()
    run = True
    pause = False
    update_rect = pygame.Rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
    while run:
        clock.tick(FPS)
        if not pause:
            draw(cells)
            cells = next_state(cells)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = False if pause else True
                    draw(cells)
                if pause and event.key == pygame.K_n:
                    cells = next_state(cells)
                    draw(cells)
                if pause and event.key == pygame.K_c:
                    for row in cells:
                        for cell in row:
                            cell.kill()
                            cell.iterate()
                    draw(cells)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pause:
                    poz = pygame.mouse.get_pos()
                    x = poz[0] // CELL_WIDTH
                    y = poz[1] // CELL_HEIGHT
                    cells[y][x].revive()
                    cells[y][x].iterate()
                    draw(cells)
        pygame.time.wait(10)
        pygame.display.update(update_rect)
        print(clock.get_fps())
    pygame.quit()


# TODO: optymalizacja renderingu (nie renderuj tego co już jest wyrenderowane)
# TODO: zamiast tablicy użyj sparse matrix
if __name__ == '__main__':
    main()
