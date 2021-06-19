from setup import *
from drawer import draw
from preparer import next_state
from generator import generate_cells
from neighbours_adder import add_neighbour


def main():
    current_states = generate_cells()
    clock = pygame.time.Clock()
    update_rect = pygame.Rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
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
                            prev = cell.is_alive
                            cell.iterate()
                            if cell.is_alive != prev:
                                if cell.is_alive:
                                    add_neighbour(current_states, cell, 1)
                                else:
                                    add_neighbour(current_states, cell, -1)
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
                    current_states[y][x].revive()
                    prev = current_states[y][x].is_alive
                    current_states[y][x].iterate()
                    if current_states[y][x].is_alive != prev:
                        if current_states[y][x].is_alive:
                            add_neighbour(current_states, current_states[y][x], 1)
                        else:
                            add_neighbour(current_states, current_states[y][x], -1)
                    draw(current_states)
        pygame.display.update(update_rect)
    pygame.quit()


if __name__ == '__main__':
    main()
