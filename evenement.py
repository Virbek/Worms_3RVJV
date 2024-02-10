import pygame
import math
import random
from armes import Grenade
from player import Player

vitesse = 10

class Evenement:

    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720))
        self.clock = pygame.time.Clock()
        self.player = []
        self.equipe = []
        nbr_equipe = 2
        nbr_plr = 2
        for i in range(nbr_plr):
            positionX = random.randrange(20, 1180, 50)
            self.player.append(Player(positionX, 700))
        
            
        self.tour = 0
        self.running = True
        self.lancer = False
        self.grenade = None
        self.exist = False
    
           
    def event(self):
        for player in self.player:
            pygame.draw.circle(self.screen, (0, 0, 0), (player.x, player.y), 20)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if self.grenade is not None:
                self.grenade.ajout_de_force()
        if keys[pygame.K_d]:
            self.player[self.tour].x += vitesse
        if keys[pygame.K_q]:
            self.player[self.tour].x -= vitesse 
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.grenade = Grenade( self.player[self.tour].x + 5, self.player[self.tour].y)
                    self.exist = True  
                    self.change = True
                if event.key == pygame.K_RIGHT:
                    self.grenade.angle -= 10
                    self.change = True
                if event.key == pygame.K_LEFT:
                    self.grenade.angle += 10
                    self.change = True   
                if event.key == pygame.K_r:
                    self.tour += 1
                    if self.tour == 2 :
                        self.tour = 0
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                   self.lancer = True 
                   self.temps_ecoule = 0.0
                
        if self.lancer:
            self.equation_traj(math.radians(self.grenade.angle), self.grenade._InitialX, self.grenade._InitialY, self.temps_ecoule, self.grenade._vitesseX, self.grenade._vitesseY, self.grenade)
            self.temps_ecoule += self.dt
            if self.grenade.y > 700 :
                for player in self.player:
                    print("pv avant :", player.pv)
                    self.ranged(player)
                    if player.pv == 0 :
                        self.player.remove(player)    
                self.grenade.reset_force()
                self.lancer = False
                self.exist = False
                self.grenade.angle = 0
        if self.exist:
            pygame.draw.circle(self.screen, (0, 0, 255), (self.grenade.x, self.grenade.y), 10)
            print(self.grenade.x,self.grenade.y,self.grenade._vitesseX,self.grenade._vitesseY,self.grenade.angle)

    
    def ranged(self, player):
        distance = pygame.math.Vector2(self.grenade.x - player.x, self.grenade.y - player.y).length()
        pygame.draw.circle(self.screen, (0, 0, 255), (self.grenade.x, self.grenade.y), self.grenade.radius)
        if distance <= self.grenade.radius:
            print("je suis dedans")
            player.pv -= 100
        print(" pv apres :", player.pv)
     
    def equation_traj(self,angle_radian, initialX, initialY, temps, vitesseX, vitesseY, objet):
        objet.x = float(vitesseX)*math.cos(angle_radian)*float(temps) + initialX
        objet.y = 0.5*(9.8)*float(temps**2) + float(vitesseY)*math.sin(angle_radian)*float(temps) + initialY
    
           
    def run(self):
        while self.running :
            self.screen.fill("purple")
            self.event()   
                
            pygame.display.flip()
            self.clock.tick(60)
            self.dt = self.clock.tick(60)/16
        pygame.quit()
        
        
            
                    
                 

            
        