import pygame


class Player:
    
    def __init__(self, x, y, image_path, numero_equipe):
        self.x = x
        self.y = y
        self._initialX = x
        self._initialY = y
        self.pv = 100
        self.direction = "DROITE"
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - 60
        self.numero_equipe = numero_equipe
        
    def set_x(self, x):
        self.x = x
        
    def set_y(self, y):
        self.y = y
    
    def get_initialX(self):
        return self._initialX 
    
    def get_initialY(self):
        return self._initialY
        
    def setPositionInitiale(self, x, y):
        self._initialX = x
        self._initialY = y
    
    def set_direction(self, direction):
        self.direction = direction
    
    def change_image(self, image_path):
        self.image = pygame.image.load(image_path)
    
    def draw(self,screen):
        screen.blit(self.image, self.rect)
        self.rect.x = self.x
        self.rect.y = self.y - 60
        
    
    