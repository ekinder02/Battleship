from player import Player
class powerUps:
    powerUps = ["2x2", "UAV", "Airstrike", "Boat Upgrade", "Move Boat", "Two Moves", "X Hit"]
    def __init__(self, powerUps):
        self.powerUps = powerUps
    
    def buy2x2(self):
        if Player.cash < 10:
            return False
        else:
            Player.cash -= 10
            Player.powerUps.append("2x2")
    
    def buyUAV(self):
        if Player.cash < 25:
            return False
        else:
            Player.cash -= 25
            Player.powerUps.append("UAV")

    def buyAirstrike(self):
        if Player.cash < 50:
            return False
        else:
            Player.cash -= 50
            Player.powerUps.append("Airstrike")

    def buyBoatUpgrade(self):
        if Player.cash < 50:
            return False
        else:
            Player.cash -= 50
            Player.powerUps.append("Boat Upgrade")
    
    def buyMoveBoat(self):
        if Player.cash < 50:
            return False
        else:
            Player.cash -= 50
            Player.powerUps.append("Move Boat")

    def buyTwoMoves(self):
        if Player.cash < 50:
            return False
        else:
            Player.cash -= 50
            Player.powerUps.append("Two Moves")

    def buyXHit(self):
        if Player.cash < 50:
            return False
        else:
            Player.cash -= 50
            Player.powerUps.append("X Hit")


