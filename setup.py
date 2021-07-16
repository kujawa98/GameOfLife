import pygame

# screen setup
pygame.init()

# window properties
WINDOW_WIDTH, WINDOW_HEIGHT = 600, 800
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('GoL')

# colors
BLUE = (65, 105, 225)
WHITE = (255, 255, 255)
LIMON = (147, 246, 0)
BLACK = (0, 0, 0)

# board properties
BOARD_WIDTH, BOARD_HEIGHT = 60, 80

# others
FPS = 60
CELL_RADIUS = 5
