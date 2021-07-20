import pygame
from random import choice

from setup import *
from cell import Cell


class RainbowLife:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.update_rect = pygame.Rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
        pygame.display.set_caption("Rainbow Life")

        self.generate_cells()

        self.is_running = True
        self.pause = False

    def run(self):
        while self.is_running:
            if not self.pause:
                self.update_cells()
            self.handle_event()
            self.update_screen()
        pygame.quit()

    def update_cells(self):
        for row in self.cells:
            for cell in row:
                if cell.neighbours > 0:
                    nei = cell.neighbours
                    if (nei > 3 or nei < 2) and cell.is_alive:
                        cell.kill()
                    elif nei == 3 and not cell.is_alive:
                        cell.revive()
                elif cell.neighbours == 0 and cell.is_alive:
                    cell.kill()
        for row in self.cells:
            for cell in row:
                self.iterate_over_neighbours(cell)

    def update_screen(self):
        self.screen.fill(BLACK)
        for row in self.cells:
            for cell in row:
                cell.draw(self.screen)
        pygame.display.update(self.update_rect)

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.pause = False if self.pause else True
                if self.pause:
                    self.handle_keydown_pause_events(event)
            if event.type == pygame.MOUSEBUTTONDOWN and self.pause:
                poz = pygame.mouse.get_pos()
                x = poz[0] // CELL_DIAMETER
                y = poz[1] // CELL_DIAMETER
                self.mouse_draw(x, y)
            if event.type == pygame.MOUSEMOTION and self.pause:
                if pygame.mouse.get_pressed(3)[0]:
                    poz = pygame.mouse.get_pos()
                    x = poz[0] // CELL_DIAMETER
                    y = poz[1] // CELL_DIAMETER
                    self.mouse_draw(x, y)

    def handle_keydown_pause_events(self, event):
        if event.key == pygame.K_n:
            self.update_cells()
        if event.key == pygame.K_c:
            for row in self.cells:
                for cell in row:
                    cell.kill()
                    self.iterate_over_neighbours(cell)
        if event.key == pygame.K_r:
            self.generate_cells()

    def generate_cells(self):
        self.cells = [[Cell(i, j) for i in range(BOARD_WIDTH)] for j in range(BOARD_HEIGHT)]
        for row in self.cells:
            for cell in row:
                if choice([True, False, False, False]):
                    cell.is_alive = True
                    self.determine_neighbours_count(cell.x, cell.y, 1)
        return self.cells

    def determine_neighbours_count(self, x, y, norm):
        for i in range(-1, 2):
            for j in range(-1, 2):
                cll = self.cells[(y + i) % BOARD_HEIGHT][(x + j) % BOARD_WIDTH]
                if i == 0:
                    if j != 0:
                        cll.neighbours += 1 * norm
                else:
                    cll.neighbours += 1 * norm

    def iterate_over_neighbours(self, cell):
        previous_state = cell.is_alive
        cell.update()
        if cell.is_alive != previous_state:
            if cell.is_alive:
                self.determine_neighbours_count(cell.x, cell.y, 1)
            else:
                self.determine_neighbours_count(cell.x, cell.y, -1)

    def mouse_draw(self, x, y):
        cell = self.cells[y][x]
        cell.kill() if cell.is_alive else cell.revive()
        self.iterate_over_neighbours(cell)


if __name__ == '__main__':
    rl = RainbowLife()
    rl.run()
