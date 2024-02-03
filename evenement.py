import pygame
import math
from armes import Grenade



class Evenement:
    
    #Initialise le jeu
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720))
        self.clock = pygame.time.Clock()
        self.running = True
        self.lancer = False
        self.grenade = None
        self.exist = False
    
    #Gere les evenement choisi par le joueur  
    def event(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if self.grenade is not None:
                self.grenade.ajout_de_force()
                print(self.grenade.vitesseX, self.grenade.vitesseY)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.grenade = Grenade(250,250)
                    self.exist = True   
                if event.key == pygame.K_LEFT:
                    if self.grenade is not None:
                        self.grenade.angle += 10
                if event.key == pygame.K_RIGHT:
                    if self.grenade is not None:
                        self.grenade.angle -= 10
            elif event.type == pygame.KEYUP:
               if event.key == pygame.K_SPACE:
                   self.lancer = True 
                   self.temps_ecoule = 0.0
                
        if self.lancer:
            self.mouvement_gre
        if self.exist:
            pygame.draw.circle(self.screen, (0, 0, 255), (self.grenade._x, self.grenade._y), 10)
            print(self.grenade._x,self.grenade._y,self.grenade.vitesseX,self.grenade.vitesseY, self.grenade.angle)
    
    
    #mouvement que la grenade fait une fois lancer
    def mouvement_gre(self):
        angle_radian = math.radians(self.grenade.angle)
        self.grenade._x = float(self.grenade.vitesseX)*math.cos(angle_radian)*float(self.temps_ecoule) + self.grenade.InitialX
        self.grenade._y = 0.5*(9.8)*float(self.temps_ecoule**2) + float(self.grenade.vitesseY)*math.sin(angle_radian)*float(self.temps_ecoule) + self.grenade.InitialY
        self.temps_ecoule += self.dt
        if self.grenade._y > 710 :
            self.grenade.reset_force()
            self.lancer = False
    
    
    
    #boucle de jeu    
    def run(self):
        while self.running :
            self.screen.fill("purple")
            self.event()   
                
            pygame.display.flip()
            self.clock.tick(60)
            self.dt = self.clock.tick(60)/16.0
        pygame.quit()
        
        
            
                    
                 

            
        