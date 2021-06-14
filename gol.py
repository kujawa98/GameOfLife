from setup import *
from drawer import draw
from preparer import next_state
from generator import generate_cells


def main():
    current_states = generate_cells()
    clock = pygame.time.Clock()
    draw(current_states)
    update_rect = pygame.Rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
    pygame.display.update(update_rect)
    run = True
    pause = False
    while run:
        clock.tick(FPS)
        if not pause:
            draw(current_states)
            next_state(current_states)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = False if pause else True
                    draw(current_states)
                if pause and event.key == pygame.K_n:
                    next_state(current_states)
                    draw(current_states)
                if pause and event.key == pygame.K_c:
                    for row in current_states:
                        for cell in row:
                            cell.kill()
                            cell.iterate()
                    draw(current_states)
                if pause and event.key == pygame.K_r:
                    poz = pygame.mouse.get_pos()
                    x = poz[0] // CELL_WIDTH
                    y = poz[1] // CELL_HEIGHT
                    print(current_states[y][x].neighbours)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pause:
                    poz = pygame.mouse.get_pos()
                    x = poz[0] // CELL_WIDTH
                    y = poz[1] // CELL_HEIGHT
                    current_states[y][x].is_alive = True
                    draw(current_states)
        pygame.display.update(update_rect)
        print(clock.get_fps())
    pygame.quit()


if __name__ == '__main__':
    main()
