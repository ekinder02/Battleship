import ship
class Player:
    def __init__(self, shipList, board, cash, number, powerUps):
        self.shipList = shipList
        self.board = board
        self.cash = cash
        self.number = number
        self.powerUps = powerUps
    def createCleanBoard(self):
        board = []
        for i in range(12):
            board.append(["-"]*12)
        self.board = board
    def createShipList(self):
        self.shipList.append(ship.Ship(5,5,[]))
        #self.shipList.append(ship.Ship(4,4,[]))
        #self.shipList.append(ship.Ship(3,3,[]))
        #self.shipList.append(ship.Ship(3,3,[]))
        #self.shipList.append(ship.Ship(2,2,[]))
    def placeShip(self):
        for i in self.shipList:
            coord = input(f"Place the bottom left corner of your {i.length} length ship: (A1 - L12) ").upper()
            if len(coord) == 2:
                y,x = int(coord[1])-1, ord(coord[0])-65
                allignment = input("Vertical or Horizontal: ").lower()
                if allignment == "vertical":
                    for j in range(i.length):
                        self.board[y-j][x] = "S"
                        i.coordinates.append([y-j,x])
                elif allignment == "horizontal":
                    for j in range(i.length):
                        self.board[y][x+j] = "S"
                        i.coordinates.append([y,x+j])
                for row in self.board:
                    for i in range(12):
                        if i != 11:
                            print(row[i], end=" ")
                        else:
                            print(row[i])
            else:
                y,x = int(coord[1:])-1, ord(coord[0])-65
                allignment = input("Vertical or Horizontal: ").lower()
                if allignment == "vertical":
                    for j in range(i.length):
                        self.board[y-j][x] = "S"
                        i.coordinates.append([y-j,x])
                elif allignment == "horizontal":
                    for j in range(i.length):
                        self.board[y][x+j] = "S"
                        i.coordinates.append([y,x+j])
                for row in self.board:
                    for i in range(12):
                        if i != 11:
                            print(row[i], end=" ")
                        else:
                            print(row[i])
    def usePowerUp(self):
        x = input("Do you want to use a power up? (Y/N) ").lower()
        if x == "y":
            return True
        else:
            return False

    def choosePowerUp(self):
        print("You have the following power ups: ")
        for i in self.powerUps:
            print(i)
        x = input("Which power up do you want to use? ").lower()
        if x == "2x2":
            self.use2x2()
        elif x == "uav":
            self.useUAV()
        elif x == "airstrike":
            self.useAirstrike()
        elif x == "boat upgrade":
            self.useBoatUpgrade()
        elif x == "move boat":
            self.useMoveBoat()
        elif x == "two moves":
            self.useTwoMoves()
        elif x == "x hit":
            self.useXHit()
    
    def shootMissile(self, enemy):
        coord = input("Shoot your missile: (A1) ").upper()
        x,y = ord(coord[0])-65, int(coord[1])-1
        if enemy.board[y][x] == "S":
            enemy.board[y][x] = "H"
            print("Hit!")
            for i in enemy.shipList:
                for coord in i.coordinates:
                    if coord == [y,x]:
                        i.health -= 1
                        if i.health == 0:
                            print("Sunk!")
                            self.cash += 100
        else:
            print("Miss!")
    def shootMissile(self, enemy):
        coord = input("Shoot your missile: (A1) ").upper()
        if len(coord) == 2:
            x,y = ord(coord[0])-65, int(coord[1])-1
            if enemy.board[y][x] == "S":
                enemy.board[y][x] = "H"
                print("Hit!")
                for i in enemy.shipList:
                    for coord in i.coordinates:
                        if coord == [y,x]:
                            i.health -= 1
                            if i.health == 0:
                                print("Sunk!")
                                self.cash += 100
            else:
                print("Miss!")
        else:
            x,y = ord(coord[0])-65, int(coord[1:])-1
            if enemy.board[y][x] == "S":
                enemy.board[y][x] = "H"
                print("Hit!")
                for i in enemy.shipList:
                    for coord in i.coordinates:
                        if coord == [y,x]:
                            i.health -= 1
                            if i.health == 0:
                                print("Sunk!")
                                self.cash += 100
            else:
                print("Miss!")
    def checkWin(self):
        for i in self.shipList:
            if i.checkHealth() == False:
                return False
        return True
    
    def buyPowerUps(self):
        print("You have " + str(self.cash) + " cash.")
        print("2x2 -> 10 cash")
        print("UAV -> 25 cash")
        print("Airstrike -> 50 cash")
        print("Boat Upgrade -> 50 cash")
        print("Move Boat -> 50 cash")
        print("Two Moves -> 50 cash")
        print("X Hit -> 50 cash")

        z = input("Do you want to buy a power up? (Y/N) ").lower()
        if z == "y":
            x = input("Which power up do you want to buy? ").lower()
            if x == "2x2":
                self.buy2x2()
            elif x == "uav":
                self.buyUAV()
            elif x == "airstrike":
                self.buyAirstrike()
            elif x == "boat upgrade":
                self.buyBoatUpgrade()
            elif x == "move boat":
                self.buyMoveBoat()
            elif x == "two moves":
                self.buyTwoMoves()
            elif x == "x hit":
                self.buyXHit()
        else:
            return False