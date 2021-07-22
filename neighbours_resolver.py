from setup import BOARD_WIDTH, BOARD_HEIGHT


class NeighboursResolver:
    def __init__(self, rl_game):
        self.rl_game = rl_game

    def determine_neighbours_count(self, x, y, norm):
        for i in range(-1, 2):
            for j in range(-1, 2):
                cll = self.rl_game.cells[(y + i) % BOARD_HEIGHT][(x + j) % BOARD_WIDTH]
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
