import pygame
import random


GROUND_HEIGHT = 100
GROUND_COLOR = (91, 60, 17)  # Vert
SKY_COLOR = (135, 206, 250)  # Bleu ciel


# Définir une classe pour le sol
class Ground:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.image = pygame.Surface((width, height))
        self.image.fill(SKY_COLOR)
        self.rect = self.image.get_rect()
        self.rect.bottom = 620
        self.ventX = 0
        self.ventY = 0

    def vent(self):
        self.ventX = random.randrange(-50, 50, 5)
        self.ventY = random.randrange(-50,50 , 5)
        print("vent :" ,self.ventX, self.ventY)