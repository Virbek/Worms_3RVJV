import pygame
import math
import random
from armes import Grenade
from armes import LanceGrenade
from player import Player
from terrain import Ground

vitesse = 10
GROUND_COLOR = (91, 60, 17)  # Vert
SKY_COLOR = (135, 206, 250)  # Bleu ciel

class Evenement:

    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720))
        self.ground = Ground(1280,720)
        self.clock = pygame.time.Clock()
        player = []
        self.equipe = []
        self.nbr_equipe = 2
        self.nbr_plr = 2
        for i in range(self.nbr_equipe):
            for i in range(self.nbr_plr):
                positionX = random.randrange(20, 1180, 50)
                player.append(Player(positionX, 600))
            self.equipe.append(player)
            
        self.nbr_tour = self.nbr_equipe * self.nbr_plr
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
        self.n_equipe = 0
        self.point_trajectoire = []    
           
    def handle_event(self):
        print(self.tour, self.nbr_tour)
        
        for equipe in self.equipe:
            for player in equipe:
                pygame.draw.circle(self.screen, (0, 0, 0), (player.x, player.y), 20)
            #if len(self.player) < self.nbr_plr:
              #  self.running = False
            
        self.event()
        self.booleen()



    def event(self):
        player = self.equipe[0][int(self.tour)]
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if self.grenade is not None:
                self.grenade.ajout_de_force()
                self.reset_traj(self.grenade)
            if self.lanceGrenade is not None:
                self.lanceGrenade.ajout_de_force()
                self.reset_traj(self.lanceGrenade)       
        if keys[pygame.K_d]:
            if self.exist_gre != True and self.exist_langre != True:
                player.x += vitesse 
                player.set_direction("DROITE") 
                self.bord(player, player.y)
                
        if keys[pygame.K_q]:
            if self.exist_gre != True and self.exist_langre != True:
                player.x -= vitesse 
                player.set_direction("GAUCHE")
                self.bord(player, player.y)
            
           
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    self.grenade = Grenade( player.x + 5, player.y)
                    self.balle = Grenade(self.grenade.x, self.grenade.y)
                    self.exist_gre = True  
                if event.key == pygame.K_l:
                    self.lanceGrenade = LanceGrenade(player.x + 5, player.y)
                    self.balle = LanceGrenade(self.lanceGrenade.x, self.lanceGrenade.y)
                    self.exist_langre = True
                if event.key == pygame.K_SPACE:
                    if self.jump != True:
                        if self.exist_gre != True and self.exist_langre != True :
                            player.setPositionInitiale(player.x, player.y)
                            self.jump = True
                            self.jump_direction = 0
                            if keys[pygame.K_d] :
                                self.jump_direction = 1
                            elif keys[pygame.K_q]:
                                self.jump_direction = 2
                
                            
                if event.key == pygame.K_LEFT:
                    if self.exist_gre:
                        self.grenade.angle += 10
                        self.reset_traj(self.grenade)
                    if self.exist_langre:
                        self.lanceGrenade.angle += 10
                        self.reset_traj(self.lanceGrenade)
                if event.key == pygame.K_RIGHT:
                    if self.exist_gre:
                        self.grenade.angle -= 10
                        self.reset_traj(self.grenade)
                    if self.exist_langre:
                        self.lanceGrenade.angle -= 10
                        self.reset_traj(self.lanceGrenade)
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
                        self.reset_traj(self.grenade)
                    if self.exist_langre:
                        self.temps_ecoule = 0.0
                        self.lancer = True
                        self.lanceGrenade.setPositionInitiale(self.lanceGrenade.x, self.lanceGrenade.y)
                        self.reset_traj(self.lanceGrenade)
        if self.tour == self.nbr_tour :
            self.tour = 0


    def booleen(self):
        player = self.equipe[0][int(self.tour)]
        #Si une arme est lancé
        if self.lancer:
            
            #si grenade lancer
            if self.exist_gre:
                
                #lancer de la gravite
                self.equation_traj(math.radians(self.grenade.angle), self.grenade._InitialX, self.grenade._InitialY, self.temps_ecoule, self.grenade._vitesseX, self.grenade._vitesseY, self.grenade)
                self.temps_ecoule += self.dt
                
                #Si plus assez de vitesse pour rebondir
                if self.grenade.get_vitesseX() < 5:
                    self.lancer = False
                    self.grenade.x += self.grenade.get_vitesseX()
                    self.grenade.reset_force() 
                    
                #la grenade touche le sol
                if self.grenade.y > 610 :
                    self.grenade.y = 610
                    self.grenade.rebond()
                    self.temps_ecoule= 0.0
                    self.grenade.setPositionInitiale(self.grenade.x, self.grenade.y)
                    
                    
            #si lance grenade lancer
            if self.exist_langre:
                self.equation_traj_frott(math.radians(self.lanceGrenade.angle), self.lanceGrenade._InitialX,self.lanceGrenade._InitialY, self.temps_ecoule, self.lanceGrenade._vitesseX, self.lanceGrenade._vitesseY, self.lanceGrenade, 0.5, self.ground.ventX, self.ground.ventY)
                self.temps_ecoule += self.dt
                
                #la grenade touche le sol
                if self.lanceGrenade.y > 610 :
                    for equipe in self.equipe:
                        for player in equipe:
                            self.ranged(player, self.lanceGrenade)
                            #if player.pv == 0 :
                                #equipe[player].remove(player)
                    self.exist_langre = False
                    self.lancer = False
                    self.tour += 1
                
        #Si une grenade existe        
        if self.grenade is not None:
            #Si la grenade est lancé et n'a pas explosé
            if self.grenade.delay:
                self.grenade.impact += self.dt
                #temps d'explosion 3 sec
                if self.grenade.impact >= 100.0:
                    for equipe in self.equipe:
                        for player in equipe:
                            self.ranged(player, self.grenade)
                            #if player.pv == 0 :
                                #self.equipe[equipe].remove(player)
                                #self.nbr_tour -= 1
                        self.exist_gre = False
                        self.lancer = False
                        self.tour += 0.5     
                        self.grenade.delay = False   
        #Si la touche saut est pressé      
        if self.jump:
            #jump vers le haut
            if self.jump_direction == 0:
                self.equation_traj(math.radians(-90), player.get_initialX(), player.get_initialY(), self.temps_ecoule, 70, 70, player)
            #jump vers la droite  
            if self.jump_direction == 1 :
                self.equation_traj(math.radians(-55), player.get_initialX(), player.get_initialY(), self.temps_ecoule, 60, 60, player)
            #jump vers la gauche
            if self.jump_direction == 2:
                self.equation_traj(math.radians(-135), player.get_initialX(), player.get_initialY(), self.temps_ecoule, 60, 60, player)
            self.temps_ecoule += self.dt
            if( player.y > 610):
                player.y = 600
                self.jump = False
                self.temps_ecoule = 0.0
                 
        #rentre des que la grenade est créé
        if self.exist_gre:
            pygame.draw.circle(self.screen, (0, 0, 255), (self.grenade.x, self.grenade.y), 10)
            if self.lancer != True :
                self.trajectoire_gre(self.grenade, self.balle)
        if self.exist_langre:
            pygame.draw.circle(self.screen, (255,0,0),(self.lanceGrenade.x, self.lanceGrenade.y), 10)
            if self.lancer != True :
                self.trajectoire_lan(self.lanceGrenade, self.balle)
        if int(self.tour) == self.nbr_tour :
            self.tour = 0



    #gere la zone d'explosion de la grenade
    def ranged(self, player, objet):
        distance = pygame.math.Vector2(objet.x - player.x, objet.y - player.y).length()
        pygame.draw.circle(self.screen, (0, 0, 255), (objet.x, objet.y), objet.radius)
        if distance <= objet.radius:
            player.pv -= 100
    
    #gere la gravité terrestre sans frottement  
    def equation_traj(self,angle_radian, initialX, initialY, temps, vitesseX, vitesseY, objet):
        objet.x = float(vitesseX)*math.cos(angle_radian)*float(temps) + initialX
        objet.y = 0.5*(9.8)*float(temps**2) + float(vitesseY)*math.sin(angle_radian)*float(temps) + initialY
        self.bord(objet, initialY)
        
    #gere equation de trajectoire avec frottement
    def equation_traj_frott(self,angle_radian, initialX, initialY, temps, vitesseX, vitesseY, objet, coef_frott, ventX, ventY):
        densite_air = 1.2
        
        vitX = float(vitesseX) - ventX
        vitY = float(vitesseY) - ventY
        
        force_frottX = -coef_frott * densite_air * vitX * abs(vitX)
        force_frottY = -coef_frott * densite_air * vitY * abs(vitY)
        
        vitesseX += force_frottX/ objet.masse * temps
        vitesseY += (force_frottY + 9.8 * objet.masse) / objet.masse * temps
        
        objet.x = float(vitesseX)*math.cos(angle_radian)*float(temps) + initialX
        objet.y = 0.5*(9.8 * objet.masse) * float(temps**2) + float(vitesseY)*math.sin(angle_radian)*float(temps) + initialY
        self.bord(objet, initialY)
    
    #defini les bord du terrain
    def bord(self, objet, y):
        if objet.x > 1280:
            objet.x = 10
            objet.setPositionInitiale(objet.x, y)
        if objet.x < 0:
            objet.x = 1270
            objet.setPositionInitiale(objet.x, y)
            
    def trajectoire_gre(self, objet, balle):
        if balle.y > 610 :
            if len(self.point_trajectoire) >= 2:
                pygame.draw.lines(self.screen,(255,0,0), False, self.point_trajectoire, 2)
        else :
            self.equation_traj(math.radians(objet.angle), objet._InitialX, objet._InitialY, self.temps_ecoule, objet._vitesseX, objet._vitesseY, balle)
            self.point_trajectoire.append((int(balle.x), int(balle.y)))
            self.temps_ecoule += self.dt
    
    def trajectoire_lan(self, objet, balle):
        if balle.y > 610 :
            if len(self.point_trajectoire) >= 2:
                pygame.draw.lines(self.screen,(255,0,0), False, self.point_trajectoire, 2)
        else :
            self.equation_traj_frott(math.radians(objet.angle), objet._InitialX, objet._InitialY, self.temps_ecoule, objet._vitesseX, objet._vitesseY, balle, 0.5, self.ground.ventX, self.ground.ventY)
            self.point_trajectoire.append((int(balle.x), int(balle.y)))
            self.temps_ecoule += self.dt
    
    def reset_traj(self, objet) :
        self.point_trajectoire = []
        self.balle.x = objet.x
        self.balle.y = objet.y
        self.temps_ecoule = 0.0

    #boucle de jeu
    def run(self):
        tour_actuelle = 0
        while self.running :
            self.screen.fill(GROUND_COLOR)
            self.screen.blit(self.ground.image, self.ground.rect)
            self.handle_event()   
            if tour_actuelle != self.tour:
                self.ground.vent()
                tour_actuelle = self.tour
                 
            pygame.display.flip()
            self.clock.tick(60)
            self.dt = self.clock.tick(60)/16
        pygame.quit()
        
        
            
                    
                 

            
        