import pygame
import math
import random
from armes import Grenade
from armes import LanceGrenade
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
            self.player.append(Player(positionX, 690))
        
        self.temps_ecoule = 0.0    
        self.tour = 0
        self.running = True
        self.lancer = False
        self.grenade = None
        self.lanceGrenade = None
        self.exist_gre = False
        self.exist_langre = False
        self.jump = False
        self.jump_direction = 0
    
           
    def handle_event(self):
        for player in self.player:
            pygame.draw.circle(self.screen, (0, 0, 0), (player.x, player.y), 20)
        if len(self.player) < 2:
            self.running = False
            
        self.event()
        
        self.booleen()



    def event(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if self.grenade is not None:
                self.grenade.ajout_de_force()
            if self.lanceGrenade is not None:
                self.lanceGrenade.ajout_de_force()
                print(self.lanceGrenade._vitesseX, self.lanceGrenade._vitesseY)
        if keys[pygame.K_d]:
            if self.exist_gre != True and self.exist_langre != True:
                self.player[self.tour].x += vitesse  
        if keys[pygame.K_q]:
            if self.exist_gre != True and self.exist_langre != True:
                self.player[self.tour].x -= vitesse 
            
           
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    self.grenade = Grenade( self.player[self.tour].x + 5, self.player[self.tour].y)
                    self.exist_gre = True  
                if event.key == pygame.K_l:
                    self.lanceGrenade = LanceGrenade(self.player[self.tour].x + 5, self.player[self.tour].y)
                    self.exist_langre = True
                if event.key == pygame.K_SPACE:
                    if self.exist_gre != True and self.exist_langre != True :
                        self.player[self.tour].setPositionInitiale(self.player[self.tour].x, self.player[self.tour].y)
                        self.jump = True
                        self.jump_direction = 0
                        if keys[pygame.K_d] :
                            self.jump_direction = 1
                        elif keys[pygame.K_q]:
                            self.jump_direction = 2
                            
                if event.key == pygame.K_LEFT:
                    if self.exist_gre:
                        self.grenade.angle += 10
                    if self.exist_langre:
                        self.lanceGrenade.angle += 10
                if event.key == pygame.K_RIGHT:
                    if self.exist_gre:
                        self.grenade.angle -= 10
                    if self.exist_langre:
                        self.lanceGrenade.angle -= 10
                if event.key == pygame.K_r:
                    self.tour += 1
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    if self.exist_gre:
                        self.grenade.setPositionInitiale(self.grenade.x, self.grenade.y)
                        self.lancer = True 
                        self.grenade.delay = True
                        self.temps_ecoule = 0.0
                        self.grenade.impact = 0.0
                    if self.exist_langre:
                        self.temps_ecoule = 0.0
                        self.lancer = True
                        self.lanceGrenade.setPositionInitiale(self.lanceGrenade.x, self.lanceGrenade.y)


    def booleen(self):
        if self.lancer:
            if self.exist_gre:
            #lancer de la gravite
                self.equation_traj(math.radians(self.grenade.angle), self.grenade._InitialX, self.grenade._InitialY, self.temps_ecoule, self.grenade._vitesseX, self.grenade._vitesseY, self.grenade)
                self.temps_ecoule += self.dt
                if self.grenade.get_vitesseX() < 5:
                    self.lancer = False
                #la grenade touche le sol
                if self.grenade.y > 695 :
                    self.grenade.y = 690
                    self.grenade.rebond()
                    self.temps_ecoule= 0.0
                    self.grenade.setPositionInitiale(self.grenade.x, self.grenade.y)
                    self.grenade.angle = 0
            if self.exist_langre:
                self.equation_traj_frott(math.radians(self.lanceGrenade.angle), self.lanceGrenade._InitialX,self.lanceGrenade._InitialY, self.temps_ecoule, self.lanceGrenade._vitesseX, self.lanceGrenade._vitesseY, self.lanceGrenade, 0.5)
                self.temps_ecoule += self.dt
                
        if self.grenade is not None:
            if self.grenade.delay:
                self.grenade.impact += self.dt
                print(self.grenade.impact)
                if self.grenade.impact >= 200.0:
                        for player in self.player:
                            self.ranged(player)
                            if player.pv == 0 :
                                self.player.remove(player)
                        self.exist_gre = False
                        self.tour += 1     
                        self.grenade.delay = False   
                
        if self.jump:
            #jump vers le haut
            if self.jump_direction == 0:
                self.equation_traj(math.radians(-90), self.player[self.tour].get_initialX(), self.player[self.tour].get_initialY(), self.temps_ecoule, 70, 70, self.player[self.tour])
            #jump vers la droite  
            if self.jump_direction == 1 :
                self.equation_traj(math.radians(-55), self.player[self.tour].get_initialX(), self.player[self.tour].get_initialY(), self.temps_ecoule, 60, 60, self.player[self.tour])
            #jump vers la gauche
            if self.jump_direction == 2:
                self.equation_traj(math.radians(-135), self.player[self.tour].get_initialX(), self.player[self.tour].get_initialY(), self.temps_ecoule, 60, 60, self.player[self.tour])
        
            self.temps_ecoule += self.dt
            print(self.temps_ecoule)
            if( self.player[self.tour].y > 700):
                self.player[self.tour].y = 690
                self.jump = False
                self.temps_ecoule = 0.0
                 
        #rentre des que la grenade est créé
        if self.exist_gre:
            pygame.draw.circle(self.screen, (0, 0, 255), (self.grenade.x, self.grenade.y), 10)
        if self.exist_langre:
            pygame.draw.circle(self.screen, (255,0,0),(self.lanceGrenade.x, self.lanceGrenade.y), 10)
        if self.tour == 2 :
            self.tour = 0




    #gere la zone d'explosion de la grenade
    def ranged(self, player):
        distance = pygame.math.Vector2(self.grenade.x - player.x, self.grenade.y - player.y).length()
        pygame.draw.circle(self.screen, (0, 0, 255), (self.grenade.x, self.grenade.y), self.grenade.radius)
        if distance <= self.grenade.radius:
            player.pv -= 100
    
    #gere la gravité terrestre sans frottement  
    def equation_traj(self,angle_radian, initialX, initialY, temps, vitesseX, vitesseY, objet):
        objet.x = float(vitesseX)*math.cos(angle_radian)*float(temps) + initialX
        objet.y = 0.5*(9.8)*float(temps**2) + float(vitesseY)*math.sin(angle_radian)*float(temps) + initialY
    
    def equation_traj_frott(self,angle_radian, initialX, initialY, temps, vitesseX, vitesseY, objet, coef_frott):
        densite_air = 1.2
        
        vitX = float(vitesseX) - 0
        vitY = float(vitesseY) - 10
        
        force_frottX = -coef_frott * densite_air * vitX * abs(vitX)
        force_frottY = -coef_frott * densite_air * vitY * abs(vitY)
        
        vitesseX = force_frottX/ objet.masse * temps
        vitesseY = (force_frottY + 9.8 * objet.masse) / objet.masse * temps
        
        objet.x = float(vitesseX)*math.cos(angle_radian)*float(temps) + initialX
        objet.y = 0.5*(9.8 * objet.masse) * float(temps**2) + float(vitesseY)*math.sin(angle_radian)*float(temps) + initialY
        
        
    #boucle de jeu
    def run(self):
        while self.running :
            self.screen.fill("purple")
            self.handle_event()   
                
            pygame.display.flip()
            self.clock.tick(60)
            self.dt = self.clock.tick(60)/16
        pygame.quit()
        
        
            
                    
                 

            
        