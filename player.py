class Player:
    def __init__(self, shipList, board, cash, number, powerUps):
        self.shipList = shipList
        self.board = board
        self.cash = cash
        self.number = number
        self.powerUps = powerUps
    def createCleanBoard(self):
        for i in range(12):
            self.board.append([["-"]]*12)
    def createShipList(self):
        return(0)
    def placeShip(self):
        for i in self.shipList:
            coord = input("Place the bottom left corner of your ship: (A1) ").upper()
            x,y = ord(coord[0])-65, int(coord[1])-1
            allignment = input("Vertical or Horizontal: ").lower()
            if allignment == "vertical":
                for j in range(i.length):
                    self.board[y+j][x] = "S"
            elif allignment == "horizontal":
                for j in range(i.length):
                    self.board[y][x+j] = "S"
    def shootMissile(self, enemy):
        coord = input("Shoot your missile: (A1) ").upper()
        x,y = ord(coord[0])-65, int(coord[1])-1
        if enemy.board[y][x] == "S":
            enemy.board[y][x] = "H"
            print("Hit!")
        else:
            print("Miss!")
    