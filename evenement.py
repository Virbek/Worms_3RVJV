import pygame
import math
from armes import Grenade



class Evenement:
    
    def __init__(self,screen):
        self.running = True
        self.grenade = None
        self.screen = screen
        
    def event(self):
        clock = pygame.time.get_ticks() / 1000
        keys = pygame.key.get_pressed()
        lancer = False
        pygame.draw.circle(self.screen, (0, 0, 255), (1000, 150), 3)
        if keys[pygame.K_SPACE]:
            if self.grenade is not None:
                self.grenade.ajout_de_force()
                print(self.grenade.vitesseX, self.grenade.vitesseY)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.grenade = Grenade(50,50)
            elif event.type == pygame.KEYUP:
               if event.key == pygame.K_SPACE:
                   lancer = True
                   vitX = self.grenade.vitesseX
                   vitY = self.grenade.vitesseY
                   
        if lancer:
            x = float(vitX)*math.cos(90)*float(clock) + 1000.0
            #self.grenade._y = 
            
            pygame.draw.circle(self.screen, (0, 0, 255), (x, 150), 3)
            print(self.grenade._x)
            if self.grenade._x <= 0:
                lancer = False
                self.grenade.reset_force()
                    
                 

            
        