import pygame


class Player:
    
    def __init__(self, x, y, image_path, numero_equipe):
        self.x = x
        self.y = y
        self._initialX = x
        self._initialY = y
        self.pv = 100
        self.direction = "DROITE"
        self.player_rect = pygame.Rect(x,y - 50 ,100, 70)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - 60
        self.numero_equipe = numero_equipe
        equipe_content = f"equipe {self.numero_equipe}"
        equipe_color = (0,0,0)
        font = pygame.font.Font(None, 25)
        self.equipe_render = font.render(equipe_content, True, equipe_color)
        self.equipe_rect = self.equipe_render.get_rect()
        pv_content = f"PV : {self.pv}"
        pv_color = (255,0,0)
        self.pv_render = font.render(pv_content, True, pv_color)
        self.pv_rect = self.pv_render.get_rect()
      
        
        
    def move_gauche(self, vitesse):
        self.x -= vitesse
        self.player_rect.x = self.x
        
    def move_droite(self, vitesse):
        self.x += vitesse
        self.player_rect.x = self.x
    
      
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
    
    def texte(self, screen):
    
        self.equipe_rect.topleft = (self.x, self.y - 90)
        screen.blit(self.equipe_render, self.equipe_rect)
        
        self.pv_rect.topleft = (self.x, self.y - 70)
        screen.blit(self.pv_render, self.pv_rect)
        
    def maj_pv(self):
        font = pygame.font.Font(None, 25)
        self.pv_render = font.render(f"PV : {self.pv}", True, (255,0,0))

    
    