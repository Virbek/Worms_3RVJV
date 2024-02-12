
class Grenade:
    
    def __init__(self, x, y):
        self.x = x 
        self.y = y  
        self.radius = 50
        self._InitialX = x
        self._InitialY = y
        self._vitesseX = 0
        self._vitesseY = 0
        self.angle = 0   
        self.impact = 0.0
        self.delay = False    
        
    def ajout_de_force(self):
        if(self._vitesseX < 100 and self._vitesseY < 100):
            self._vitesseX = self._vitesseX + 1
            self._vitesseY = self._vitesseY + 1
            
    def reset_force(self):
        self._vitesseX = 0
        self._vitesseY = 0
        
    def setPositionInitiale(self, x, y):
        self._InitialX = x
        self._InitialY = y
    
        
    
        
    
        
    
        
        
        
    