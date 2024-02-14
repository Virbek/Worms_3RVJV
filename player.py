class Player:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self._initialX = x
        self._initialY = y
        self.pv = 100
        self.direction = "DROITE"
        
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
        
    
    