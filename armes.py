from abc import ABC, abstractmethod

class Armes(ABC):
    
    def utiliser_arme(self):
        pass
    

class Grenade(Armes):
    
    def __init__(self, x, y):
        self._x = x 
        self._y = y  
        self.vitesseX = 0
        self.vitesseY = 0
        angle = 0       
        
    def ajout_de_force(self):
        if(self.vitesseX < 1000 and self.vitesseY < 1000):
            self.vitesseX = self.vitesseX + 10
            self.vitesseY = self.vitesseY + 10
            
    def reset_force(self):
        self.vitesseX = 0
        self.vitesseY = 0
    
    
    def get_vitesseX(self):
        return self.vitesseX
    
    def get_vitesseY(self):
        return self.vitesseY
    
        
    
        
    
        
        
        
    