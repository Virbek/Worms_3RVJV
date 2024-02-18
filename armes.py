import pygame

class Grenade:
    
    def __init__(self, x, y):
        self.x = x 
        self.y = y  
        self.radius = 50
        self._InitialX = x
        self._InitialY = y
        self._vitesseX = 0
        self._vitesseY = 0
        self.recte = pygame.Rect(x,y  ,20, 20)
        self.angle = 0   
        self.impact = 0.0
        self.delay = False  
        self.image = pygame.image.load("ressource\Grenade.png")
        self.rect = self.image.get_rect()  
        
    def ajout_de_force(self):
        if(self._vitesseX < 100 and self._vitesseY < 100):
            self._vitesseX = self._vitesseX + 1
            self._vitesseY = self._vitesseY + 1
            
    def enlever_force(self):
        if(self._vitesseX > 0 and self._vitesseY > 0):
            self._vitesseX = self._vitesseX - 1
            self._vitesseY = self._vitesseY - 1
            
    def reset_force(self):
        self._vitesseX = 0
        self._vitesseY = 0
        self.angle = 0
        
    def rebond(self):
        self._vitesseX = 0.4*self._vitesseX
        self._vitesseY = 0.4*self._vitesseY
        
    def setPositionInitiale(self, x, y):
        self._InitialX = x
        self._InitialY = y
    
    def get_vitesseX(self):
        return self._vitesseX
    
    def draw(self,screen):
        screen.blit(self.image, self.rect)
        self.rect.x = self.x - 50
        self.rect.y = self.y - 60
        
    def maj_hitbox(self):
        self.recte.x = self.x +50
        self.recte.y = self.y - 50
        
class LanceGrenade :
    
    def __init__(self, x, y):
        self.x = x + 20
        self.y = y -20
        self.radius = 150
        self.angle = 0
        self._InitialX = x
        self._InitialY = y
        self._vitesseX = 0
        self._vitesseY = 0
        self.image = pygame.image.load("ressource\Missile.png")
        self.rect = self.image.get_rect()
        self.recte = pygame.Rect(x,y  ,20, 20)
        
       
    def ajout_de_force(self):
        if(self._vitesseX < 500 and self._vitesseY < 500):
            self._vitesseX = self._vitesseX + 5
            self._vitesseY = self._vitesseY + 5
    
    def setPositionInitiale(self, x, y):
        self._InitialX = x
        self._InitialY = y   
        
    def draw(self,screen):
        screen.blit(self.image, self.rect)
        self.rect.x = self.x - 50
        self.rect.y = self.y - 60
        
    def enlever_force(self):
        if(self._vitesseX > 0 and self._vitesseY > 0):
            self._vitesseX = self._vitesseX - 1
            self._vitesseY = self._vitesseY - 1
    
    def maj_hitbox(self):
        self.recte.x = self.x +50
        self.recte.y = self.y - 50
        
        
        
    