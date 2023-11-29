class Ship:
    def __init__(self, health, length, coordinates):
        self.health = health
        self.length = length
        self.coordinates = coordinates
    
    def checkHealth(self):
        if self.health == 0:
            return True
        else:
            return False
    
    def sink(self):
        self.health = 0
        return True

