import pygame

# screen setup
pygame.init()

# window properties
WINDOW_WIDTH, WINDOW_HEIGHT = 960, 720
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('GoL')

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# board properties
BOARD_WIDTH, BOARD_HEIGHT = 192, 144

# others
FPS = 60
CELL_WIDTH, CELL_HEIGHT = 5, 5
