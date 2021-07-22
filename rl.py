import pygame
from random import choice

from setup import *
from cell import Cell
from event_handler import EventHandler
from neighbours_resolver import NeighboursResolver


class RainbowLife:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.update_rect = pygame.Rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
        pygame.display.set_caption("Rainbow Life")

        self.event_handler = EventHandler(self)
        self.neighbours_resolver = NeighboursResolver(self)

        self.cells = []
        self.generate_cells()

        self.is_running = True
        self.pause = False

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
                self.neighbours_resolver.iterate_over_neighbours(cell)

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
                    self.neighbours_resolver.determine_neighbours_count(cell.x, cell.y, 1)

    def mouse_add(self):
        poz = pygame.mouse.get_pos()
        x = poz[0] // CELL_DIAMETER
        y = poz[1] // CELL_DIAMETER
        cell = self.cells[y][x]
        cell.kill() if cell.is_alive else cell.revive()
        self.neighbours_resolver.iterate_over_neighbours(cell)


if __name__ == '__main__':
    rl = RainbowLife()
    rl.run()
