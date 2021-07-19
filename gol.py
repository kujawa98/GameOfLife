import pygame

from setup import *
from drawer import draw
from preparer import next_state, neigh_iterate
from generator import generate_cells


class RainbowLife:
    def __init__(self):
        pygame.init()
        self.cells = generate_cells()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.update_rect = pygame.Rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
        pygame.display.set_caption("Rainbow Life")

        self.is_running = True
        self.pause = False

    def run(self):
        while self.is_running:
            if not self.pause:
                draw(self.cells, self.screen)
                next_state(self.cells)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.pause = False if self.pause else True
                        draw(self.cells, self.screen)
                    if self.pause:
                        if event.key == pygame.K_n:
                            next_state(self.cells)
                            draw(self.cells, self.screen)
                        if event.key == pygame.K_c:
                            for row in self.cells:
                                for cell in row:
                                    cell.kill()
                                    neigh_iterate(self.cells, cell)
                            draw(self.cells, self.screen)
                        if event.key == pygame.K_r:
                            self.cells = generate_cells()
                            draw(self.cells, self.screen)
                if event.type == pygame.MOUSEBUTTONDOWN and self.pause:
                    poz = pygame.mouse.get_pos()
                    x = poz[0] // CELL_DIAMETER
                    y = poz[1] // CELL_DIAMETER
                    mouse_draw(self.cells, x, y)
                    draw(self.cells, self.screen)
                if event.type == pygame.MOUSEMOTION and self.pause:
                    if pygame.mouse.get_pressed(3)[0]:
                        poz = pygame.mouse.get_pos()
                        x = poz[0] // CELL_DIAMETER
                        y = poz[1] // CELL_DIAMETER
                        mouse_draw(self.cells, x, y)
                        draw(self.cells, self.screen)
            pygame.display.update(self.update_rect)
        pygame.quit()


def mouse_draw(cells, x, y):
    cell = cells[y][x]
    cell.kill() if cell.is_alive else cell.revive()
    neigh_iterate(cells, cell)


if __name__ == '__main__':
    rl = RainbowLife()
    rl.run()
