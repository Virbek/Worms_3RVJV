import pygame
from evenement import Evenement

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
evenement = Evenement(screen)

while evenement.running :
    
    evenement.event()   
    pygame.draw.circle(screen, (255, 255, 255), (500, 150), 10)
    screen.fill("purple")
         
    pygame.display.flip()
           
    clock.tick(60)
        
pygame.quit()    
    
