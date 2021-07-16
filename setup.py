import pygame

# screen setup
pygame.init()

# window properties
WINDOW_WIDTH, WINDOW_HEIGHT = 600, 800
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('GoL')

# colors
WHITE = (255, 255, 255)
LIMON = (147, 246, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (65, 105, 225)
ORANGE = (254, 127, 0)
YELLOW = (255, 255, 255)
GREEN = (0, 255, 0)
NAVY = (47, 119, 147)
PURPLE = (150, 75, 132)
COLORS = [RED, BLUE, ORANGE, YELLOW, GREEN, NAVY, PURPLE]

# board properties
BOARD_WIDTH, BOARD_HEIGHT = 60, 80

# others
FPS = 60
CELL_RADIUS = 5
CELL_DIAMETER = CELL_RADIUS * 2
