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
        self.nbr_equipe = 3
        self.nbr_plr = 2
        for i in range(self.nbr_equipe):
            for j in range(self.nbr_plr):
                positionX = random.randrange(20, 1180, 50)
                player.append(Player(positionX, 600,"ressource\Perso_Statique.png",i+1))
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
        self.test_fin_tour()
        for equipe in self.equipe:
            for player in equipe:
                player.draw(self.screen)
                player.texte(self.screen)
                
        self.test_personnage()
             
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
        if keys[pygame.K_DOWN]:
            if self.grenade is not None:
                self.grenade.enlever_force()
                self.reset_traj(self.grenade)
            if self.lanceGrenade is not None:
                self.lanceGrenade.enlever_force()
                self.reset_traj(self.lanceGrenade)       
        if keys[pygame.K_d]:
            if self.exist_gre != True and self.exist_langre != True:
                player.move_droite(vitesse) 
                player.set_direction("DROITE")
                self.bord(player, player.y)
                
        if keys[pygame.K_q]:
            if self.exist_gre != True and self.exist_langre != True:
                player.move_gauche(vitesse) 
                player.set_direction("GAUCHE")
                self.bord(player, player.y)
            
           
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    if self.exist_langre: 
                        del self.lanceGrenade
                        self.lanceGrenade = None
                        self.exist_langre = False
                        self.grenade = Grenade( player.x + 35, player.y - 10)
                        self.balle = Grenade(self.grenade.x +35, self.grenade.y - 10)
                        self.exist_gre = True  
                    elif self.exist_gre != True :
                        self.grenade = Grenade( player.x + 35, player.y - 10)
                        self.balle = Grenade(self.grenade.x +35, self.grenade.y - 10)
                        self.exist_gre = True  
                    else :
                        del self.grenade
                        self.grenade = None
                        self.exist_gre = False
                if event.key == pygame.K_l:
                    if self.exist_gre: 
                        del self.grenade
                        self.grenade = None
                        self.exist_gre = False
                        self.lanceGrenade = LanceGrenade( player.x + 35, player.y - 10)
                        self.balle = LanceGrenade(self.lanceGrenade.x +35, self.lanceGrenade.y - 10)
                        self.exist_langre = True 
                    elif self.exist_langre != True :
                        self.lanceGrenade = LanceGrenade( player.x + 35, player.y - 10)
                        self.balle = LanceGrenade(self.lanceGrenade.x +35, self.lanceGrenade.y - 10)
                        self.exist_langre = True  
                    else :
                        del self.lanceGrenade
                        self.lanceGrenade = None
                        self.exist_langre = False
                        
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
                    if self.lancer != True :
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
        if self.tour >= self.nbr_tour :
            self.tour = 0


    def booleen(self):
        player = self.equipe[0][int(self.tour)]
        #Si une arme est lancé
        if self.lancer:
            
            #si grenade lancer
            if self.exist_gre:
                self.grenade.draw(self.screen)
                #lancer de la gravite
                self.equation_traj(math.radians(self.grenade.angle), self.grenade._InitialX, self.grenade._InitialY, self.temps_ecoule, self.grenade._vitesseX, self.grenade._vitesseY, self.grenade)
                self.grenade.maj_hitbox()
                self.temps_ecoule += self.dt
                
                #Si plus assez de vitesse pour rebondir
                if self.grenade.get_vitesseX() < 5:
                    self.grenade.x += self.grenade.get_vitesseX()
                    self.grenade.reset_force() 
                    self.grenade.maj_hitbox()
                    
                #la grenade touche le sol
                if self.grenade.y > 620 :
                    self.grenade.y = 620
                    self.grenade.rebond()
                    self.grenade.maj_hitbox()
                    self.temps_ecoule= 0.0
                    self.grenade.setPositionInitiale(self.grenade.x, self.grenade.y)
                    
                    
            #si lance grenade lancer
            if self.exist_langre:
                #le lanceGrenade touche le sol
                if self.lanceGrenade.y > 630 :
                    for equipe in self.equipe:
                        for player in equipe:
                            self.ranged(player, self.lanceGrenade)
                            if player.pv == 0 :
                                self.equipe[0].remove(player)
                                self.nbr_tour -= 1
                                self.test_fin_tour()
                    self.exist_langre = False
                    self.lancer = False
                    self.tour += 1
                else:
                    self.lanceGrenade.draw(self.screen)
                    self.equation_traj_frott(math.radians(self.lanceGrenade.angle), self.lanceGrenade._InitialX,self.lanceGrenade._InitialY, self.temps_ecoule, self.lanceGrenade._vitesseX, self.lanceGrenade._vitesseY, self.lanceGrenade, self.ground.ventX, self.ground.ventY)
                    self.temps_ecoule += self.dt
                    self.lanceGrenade.maj_hitbox()
                
        #Si une grenade existe        
        if self.grenade is not None:
            #Si la grenade est lancé et n'a pas explosé
            if self.grenade.delay:
                self.grenade.impact += self.dt
                #temps d'explosion 3 sec
                if self.grenade.impact >= 60.0:
                    for equipe in self.equipe:
                        for player in equipe:
                            self.ranged(player, self.grenade)
                            if player.pv == 0 :
                                self.equipe[0].remove(player)
                                self.nbr_tour -= 1
                                self.test_fin_tour()
                    self.exist_gre = False
                    self.lancer = False
                    self.tour += 1   
                    self.grenade.delay = False 
                        
        #Si la touche saut est pressé      
        if self.jump:
            #jump vers le haut
            if self.jump_direction == 0:
                self.affiche_ver(player,"ressource\Perso_Saut.png", "ressource\Perso_Saut_inverse.png")
                self.equation_traj(math.radians(-90), player.get_initialX(), player.get_initialY(), self.temps_ecoule, 70, 70, player)
            #jump vers la droite  
            if self.jump_direction == 1 :
                player.change_image("ressource\Perso_Saut.png") 
                self.equation_traj(math.radians(-55), player.get_initialX(), player.get_initialY(), self.temps_ecoule, 60, 60, player)
            #jump vers la gauche
            if self.jump_direction == 2:
                player.change_image("ressource\Perso_Saut_inverse.png")
                self.equation_traj(math.radians(-135), player.get_initialX(), player.get_initialY(), self.temps_ecoule, 60, 60, player)
            self.temps_ecoule += self.dt
            if( player.y > 610):
                player.y = 600
                self.jump = False
                self.temps_ecoule = 0.0 
        else:  
            self.affiche_ver(player,"ressource\Perso_Statique.png","ressource\Perso_Statique_inversee.png")
        
        if self.exist_gre:
            if self.lancer != True :
                self.trajectoire_gre(self.grenade, self.balle)
                self.affiche_ver(player,"ressource\Perso_Grenade.png","ressource\Perso_Grenade_inversee.png")
        #rentre quand le lance-grenade existe
        elif self.exist_langre:
            if self.lancer != True :
                self.trajectoire_lan(self.lanceGrenade, self.balle)
                self.affiche_ver(player,"ressource\Perso_Bazooka.png","ressource\Perso_Bazooka_inversee.png") 
                    
        if int(self.tour) >= self.nbr_tour :
            self.tour = 0


    def affiche_ver(self, player, droite, gauche):
        if player.direction == "DROITE":
            player.change_image(droite) 
        else :
            player.change_image(gauche)
             
    #gere la zone d'explosion de la grenade
    def ranged(self, player, objet):
        pygame.draw.circle(self.screen, (0, 0, 255), (objet.x, objet.y), objet.radius)
        objet.recte = pygame.Rect(objet.x - objet.radius, objet.y - objet.radius, 2* objet.radius, 2* objet.radius)
        centre = pygame.Rect(objet.x - 20, objet.y - 20, 2* 20, 2* 20)
        interieur = pygame.Rect(objet.x - 35, objet.y - 35, 2* 35, 2* 35)
        if player.player_rect.colliderect(centre):
            player.pv -= 50
            player.maj_pv()
        elif player.player_rect.colliderect(interieur):
            player.pv -= 25
            player.maj_pv()
        elif player.player_rect.colliderect(objet.recte):
            player.pv -= 10
            player.maj_pv()
    
    #gere la gravité terrestre sans frottement  
    def equation_traj(self,angle_radian, initialX, initialY, temps, vitesseX, vitesseY, objet):
        objet.x = float(vitesseX)*math.cos(angle_radian)*float(temps) + initialX
        objet.y = 0.5*(9.8)*float(temps**2) + float(vitesseY)*math.sin(angle_radian)*float(temps) + initialY
        self.bord(objet, initialY)
        
    #gere equation de trajectoire avec frottement
    def equation_traj_frott(self,angle_radian, initialX, initialY, temps, vitesseX, vitesseY, objet, ventX, ventY):
        
        vitesseX = float(vitesseX) - ventX
        vitesseY = float(vitesseY) - ventY
        
        
        objet.x = float(vitesseX)*math.cos(angle_radian)*float(temps) + initialX
        objet.y = 0.5*(9.8) * float(temps**2) + float(vitesseY)*math.sin(angle_radian)*float(temps) + initialY
        self.bord(objet, initialY)
    
    #defini les bord du terrain
    def bord(self, objet, y):
        if objet.x > 1280:
            objet.x = 10
            objet.setPositionInitiale(objet.x, y)
        if objet.x < 0:
            objet.x = 1270
            objet.setPositionInitiale(objet.x, y)
            
    #calcul la trajectoire de la grenade        
    def trajectoire_gre(self, objet, balle):
        if balle.y == 620 :
            if len(self.point_trajectoire) >= 2:
                pygame.draw.lines(self.screen,(255,0,0), False, self.point_trajectoire, 2)
        else :
            self.equation_traj(math.radians(objet.angle), objet._InitialX, objet._InitialY, self.temps_ecoule, objet._vitesseX, objet._vitesseY, balle) 
            if balle.y > 610 :
                balle.y = 620
            self.point_trajectoire.append((int(balle.x), int(balle.y)))
            self.temps_ecoule += self.dt
    
    #calcul la trajectoire du lance grenade  
    def trajectoire_lan(self, objet, balle):
        if balle.y == 620  :
            if len(self.point_trajectoire) >= 2:
                pygame.draw.lines(self.screen,(255,0,0), False, self.point_trajectoire, 2)
        else :
            self.equation_traj_frott(math.radians(objet.angle), objet._InitialX, objet._InitialY, self.temps_ecoule, objet._vitesseX, objet._vitesseY, balle, self.ground.ventX, self.ground.ventY)
            if balle.y > 610 :
                balle.y = 620
            self.point_trajectoire.append((int(balle.x), int(balle.y)))
            self.temps_ecoule += self.dt
    
    def reset_traj(self, objet) :
        self.point_trajectoire = []
        self.balle.x = objet.x
        self.balle.y = objet.y
        self.temps_ecoule = 0.0

    def initialisation_image(self):
        per_idle_path = "ressource/Perso_Statique"
        self.per_idle = pygame.image.load(per_idle_path)
        
    def test_personnage(self):
        tab = []
        for equipe in self.equipe:
            for player in equipe:
                tab.append(player.numero_equipe)
        identique = all(element == tab[0] for element in tab)
        if identique:
            self.running = False
    
    #regarde si lorsque qu'un worms est detruit, son tour n'est pas plus grand le nombre de tour possible      
    def test_fin_tour(self):
        if self.tour >= self.nbr_tour:
            self.tour = 0
            
    def text(self, color, content):
        font = pygame.font.Font(None, 36)
        
        return font.render(content, True, color)
        
            
    #boucle de jeu
    def run(self):
        tour_actuelle = 0
        while self.running :
            self.screen.fill(GROUND_COLOR)
            self.screen.blit(self.ground.image, self.ground.rect)
            vent = self.text((255,255,255), f"vent x :{self.ground.ventX}, vent y = {self.ground.ventY}")
            vent_rect = vent.get_rect()
            vent_rect.topleft = (10, 10)
            self.screen.blit(vent, vent_rect)
            self.handle_event()   
            if tour_actuelle != self.tour:
                self.ground.vent()
                tour_actuelle = self.tour
                 
            pygame.display.flip()
            self.clock.tick(60)
            self.dt = self.clock.tick(60)/16
        pygame.quit()
        
        
            
                    
                 

            
        