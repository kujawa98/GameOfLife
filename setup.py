import pygame

# screen setup
pygame.init()

# window properties
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 570 + 150
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('GoL')

# colors
BLUE = (65, 105, 225)
WHITE = (255, 255, 255)
LIMON = (147, 246, 0)

# board properties
BOARD_WIDTH, BOARD_HEIGHT = 128, 57

# others
FPS = 60
CELL_WIDTH, CELL_HEIGHT = 10, 10
FONT = pygame.font.Font('ARCADECLASSIC.TTF', 32)
