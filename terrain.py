import pygame

# Définir quelques constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GROUND_HEIGHT = 100
GROUND_COLOR = (0, 255, 0)  # Vert
SKY_COLOR = (135, 206, 250)  # Bleu ciel


# Définir une classe pour le sol
class Ground:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.image = pygame.Surface((width, height))
        self.image.fill(GROUND_COLOR)
        self.rect = self.image.get_rect()
        self.rect.bottom = SCREEN_HEIGHT