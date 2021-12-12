from setup import BOARD_WIDTH, BOARD_HEIGHT

#class for resolving living neighbours count
class NeighboursResolver:
    def __init__(self, rl_game):
        self.rl_game = rl_game

    #this method determines neighbours that are alive
    #if norm is 1 that means that neighbour is alive
    #otherwise it's dead
    def determine_neighbours_count(self, x, y, norm):
        for i in range(-1, 2):
            for j in range(-1, 2):
                cll = self.rl_game.cells[(y + i) % BOARD_HEIGHT][(x + j) % BOARD_WIDTH]
                if i == 0:
                    if j != 0:
                        cll.neighbours += 1 * norm
                else:
                    cll.neighbours += 1 * norm

    #this method iterates over neighbours and based
    #on it's state it calls determine_neighbours_count
    #with appropiate norm
    def iterate_over_neighbours(self, cell):
        previous_state = cell.is_alive
        cell.update()
        if cell.is_alive != previous_state:
            if cell.is_alive:
                self.determine_neighbours_count(cell.x, cell.y, 1)
            else:
                self.determine_neighbours_count(cell.x, cell.y, -1)
