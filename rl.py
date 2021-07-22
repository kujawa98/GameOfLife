import pygame
from random import choice

from setup import *
from cell import Cell
from event_handler import EventHandler


class RainbowLife:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.update_rect = pygame.Rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
        pygame.display.set_caption("Rainbow Life")

        self.cells = []
        self.generate_cells()

        self.is_running = True
        self.pause = False

        self.event_handler = EventHandler(self)

    def run(self):
        while self.is_running:
            if not self.pause:
                self.update_cells()
            self.event_handler.handle_event()
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

    def generate_cells(self):
        self.cells = [[Cell(i, j) for i in range(BOARD_WIDTH)] for j in range(BOARD_HEIGHT)]
        for row in self.cells:
            for cell in row:
                if choice([True, False, False, False]):
                    cell.is_alive = True
                    self.determine_neighbours_count(cell.x, cell.y, 1)

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

    def mouse_add(self):
        poz = pygame.mouse.get_pos()
        x = poz[0] // CELL_DIAMETER
        y = poz[1] // CELL_DIAMETER
        cell = self.cells[y][x]
        cell.kill() if cell.is_alive else cell.revive()
        self.iterate_over_neighbours(cell)


if __name__ == '__main__':
    rl = RainbowLife()
    rl.run()
