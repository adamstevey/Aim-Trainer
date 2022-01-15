import pygame

pygame.font.init()

# CONSTANTS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (255, 0, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BACKGROUND_COLOR = BLACK
TARGET_COLOR = RED
PRESSED_COLOR = BLUE

WIDTH = 900
HEIGHT = 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Target Practice")

TARGET_RADIUS = 75
RING_WIDTH = 5
SPEED = 0.3
ACCELERATION = 0.0175
PRESSED_SPEED = 1

font = pygame.font.SysFont("Comicsans", 50)