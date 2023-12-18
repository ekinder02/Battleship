#creates ship class and adds health, length, and coordinates to each ship
class Ship:
    def __init__(self, health, length, coordinates):
        self.health = health
        self.length = length
        self.coordinates = coordinates
    
    #checks the ships health
    def checkHealth(self):
        if self.health == 0:
            return True
        else:
            return False
    
    #return true if ship is sunk
    def sink(self):
        self.health = 0
        return True