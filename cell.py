import random


class Cell:
    def __init__(self, x, y):
        self.is_alive = random.choice(
            [True, False, False])
        self.x = x
        self.y = y
        self.will_be_alive = False

    def kill(self):
        self.will_be_alive = False

    def revive(self):
        self.will_be_alive = True

    def iterate(self):
        self.is_alive = self.will_be_alive
