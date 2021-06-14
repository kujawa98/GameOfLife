class Cell:
    def __init__(self, x, y, is_alive):
        self.is_alive = is_alive
        self.x = x
        self.y = y
        self.will_be_alive = False
        self.neighbours = 0

    def kill(self):
        self.will_be_alive = False

    def revive(self):
        self.will_be_alive = True

    def iterate(self):
        self.is_alive = self.will_be_alive
