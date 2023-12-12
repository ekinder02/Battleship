import ship
import random
class Player:
    def __init__(self, shipList, board, cash, number, powerUps,firingBoard):
        self.shipList = shipList
        self.board = board
        self.cash = cash
        self.firingBoard = firingBoard
        self.number = number
        self.powerUps = powerUps
    def createCleanBoard(self):
        self.board = []
        self.firingBoard = []
        for i in range(12):
            self.board.append(["-"]*12)
            self.firingBoard.append(["-"]*12)
            
    def createShipList(self):
        self.shipList.append(ship.Ship(5,5,[]))
        self.shipList.append(ship.Ship(4,4,[]))
        #self.shipList.append(ship.Ship(3,3,[]))
        #self.shipList.append(ship.Ship(3,3,[]))
        #self.shipList.append(ship.Ship(2,2,[]))
    def placeShip(self,place,ship,placeShipLabel,error):
        if ship == None:
            return ()
        if len(place)!= 4 and len(place) != 5:
            error.text = "Invalid input! Replace ship"
            print("1")
            return ()
        if place[0].upper() not in "ABCDEFGHIJKL" or place[1:3].replace(" ","") not in "123456789101112":
            error.text = "Invalid input! Replace ship"
            print(place[0])
            return ()
        if place[place.index(" ")+1:].lower() not in "vh":
            error.text = "Invalid input! Replace ship"
            print("3")
            return ()
        y = int(place[1:place.index(" ")])-1
        x = ord(place[0])-65
        allignment = place[place.index(" ")+1:]
        if allignment.lower() == "v":
            if y-ship.length < 0:
                error.text = "Ship out of bounds! Replace ship"
                return ()
            for i in range(ship.length):
                if self.board[y-i][x] == "S":
                    error.text = "Ship overlapping! Replace ship"
                    return ()
            for j in range(ship.length):
                self.board[y-j][x] = "S"
                ship.coordinates.append([y-j,x])
        elif allignment.lower() == "h":
            if x+ship.length > 12:
                error.text = "Ship out of bounds! Replace ship"
                return ()
            for i in range(ship.length):
                if self.board[y][x+i] == "S":
                    error.text = "Ship overlapping! Replace ship"
                    return ()
            for j in range(ship.length):
                self.board[y][x+j] = "S"
                ship.coordinates.append([y,x+j])
        self.shipList.remove(ship)
        error.text = ""
        if self.shipList != []:
            placeShipLabel.text = "Place your " + str(self.shipList[0].length) + " length ship"
    def usePowerUp(self):
        x = input("Do you want to use a power up? (Y/N) ").lower()
        if x == "y":
            return True
        else:
            return False

    def choosePowerUp(self,enemy):
        print("You have the following power ups: ")

        for i in self.powerUps:
            print(i)
        x = input("Which power up do you want to use? ").lower()
        if x == "2x2":
            self.use2x2(enemy)
        elif x == "uav":
            self.useUAV(enemy)
        elif x == "airstrike":
            self.useAirstrike(enemy)
        elif x == "boat upgrade":
            self.useBoatUpgrade()
        elif x == "move boat":
            self.useMoveBoat()
        elif x == "two moves":
            self.useTwoMoves(enemy)
        elif x == "x hit":
            self.useXHit(enemy)
    
    def shootMissile(self, enemy):
        coord = input("Shoot your missile: (A1) ").upper()
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
        elif enemy.board[y][x] == "H":
            print("Already hit!")
        else:
            enemy.board[y][x] = "M"
            print("Miss!")
        for row in enemy.board:
                    for i in range(12):
                        if i != 11:
                            print(row[i], end=" ")
                        else:
                            print(row[i])
    
    def shootMissileParam(self,enemy,inp):
        print("shot on " + str(enemy.number))
        if inp[0] not in "ABCDEFGHIJKL" or inp[1:] not in "123456789101112":
            print("Invalid input! Try again")
            return ()
        if len(inp) != 2:
            print("Invalid input! Try again")
            return ()
        y = int(inp[1:])-1
        x = ord(inp[0])-65
        if enemy.board[y][x] == "S":
            self.firingBoard[y][x] = "H"
            enemy.board[y][x] = "H"
            for i in enemy.shipList:
                for coord in i.coordinates:
                    if coord == [y,x]:
                        i.health -= 1
                        if i.health == 0:
                            print("Sunk!")
                            self.cash += 100
        elif enemy.board[y][x] == "H":
            print("Already hit!")
        elif enemy.board[y][x] == "-":
            self.firingBoard[y][x] = "M"
            enemy.board[y][x] = "M"
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
        
    def buy2x2(self):
        if self.cash < 10:
            print("Not enough cash!")
            return False
        else:
            self.cash -= 10
            self.powerUps.append("2x2")
            print("2x2 power up bought!")
    
    def buyUAV(self):
        if self.cash < 25:
            print("Not enough cash!")
            return False
        else:
            self.cash -= 25
            self.powerUps.append("UAV")
            print("UAV power up bought!")
    
    def buyAirstrike(self):
        if self.cash < 50:
            print("Not enough cash!")
            return False
        else:
            self.cash -= 50
            self.powerUps.append("Airstrike")
            print("Airstrike power up bought!")

    def buyBoatUpgrade(self):
        if self.cash < 50:
            print("Not enough cash!")
            return False
        else:
            self.cash -= 50
            self.powerUps.append("Boat Upgrade")
            print("Boat Upgrade power up bought!")
    
    def buyMoveBoat(self):
        if self.cash < 50:
            print("Not enough cash!")
            return False
        else:
            self.cash -= 50
            self.powerUps.append("Move Boat")
            print("Move Boat power up bought!")
    
    def buyTwoMoves(self):
        if self.cash < 50:
            print("Not enough cash!")
            return False
        else:
            self.cash -= 50
            self.powerUps.append("Two Moves")
            print("Two Moves power up bought!")

    def buyXHit(self):
        if self.cash < 50:
            print("Not enough cash!")
            return False
        else:
            self.cash -= 50
            self.powerUps.append("X Hit")
            print("X Hit power up bought!")
    def use2x2(self, enemy):
        coord = input("Place the bottom left corner of your 2x2: (A1 - L12) ").upper()
        if len(coord) == 2:
            y,x = int(coord[1])-1, ord(coord[0])-65
            for i in range(2):
                for j in range(2):
                    if enemy.board[y-i][x+j] == "S":
                        enemy.board[y-i][x+j] = "H"
                        for ship in enemy.shipList:
                            for coord in ship.coordinates:
                                if coord == [y-i,x+j]:
                                    ship.health -= 1
                                    if ship.health == 0:
                                        print("Sunk!")
                                        self.cash += 100
                    elif enemy.board[y-i][x+j] == "-":
                        enemy.board[y-i][x+j] = "M"
            #Can delete this later just showing if it works right now
            for row in enemy.board:
                for i in range(12):
                    if i != 11:
                        print(row[i], end=" ")
                    else:
                        print(row[i])
        else:
            y,x = int(coord[1:])-1, ord(coord[0])-65
            for i in range(2):
                for j in range(2):
                    if enemy.board[y-i][x+j] == "S":
                        enemy.board[y-i][x+j] = "H"
                        for ship in enemy.shipList:
                            for coord in ship.coordinates:
                                if coord == [y-i,x+j]:
                                    ship.health -= 1
                                    if ship.health == 0:
                                        print("Sunk!")
                                        self.cash += 100
                    elif enemy.board[y-i][x+j] == "-":
                        enemy.board[y-i][x+j] = "M"
            for row in enemy.board:
                for i in range(12):
                    if i != 11:
                        print(row[i], end=" ")
                    else:
                        print(row[i])
        self.powerUps.remove("2x2")
    def useAirstrike(self, enemy):
        coords = []
        coord_options = []
        
        for letter in range(ord('A'), ord('M')):
            for number in range(1, 13):
                coord_options.append(chr(letter) + str(number))

        while len(coords) < 5:
            coord = random.choice(coord_options)
            if coord not in coords:
                coords.append(coord)
            if enemy.board[int(coord[1:])-1][ord(coord[0])-65] == "M":
                coords.remove(coord)
            if enemy.board[int(coord[1:])-1][ord(coord[0])-65] == "H":
                coords.remove(coord)



        for num in coords:
            y,x = int(num[1:])-1, ord(num[0])-65
            if enemy.board[y][x] == "S":
                enemy.board[y][x] = "H"
                for ship in enemy.shipList:
                    for coord in ship.coordinates:
                        if coord == [y,x]:
                            ship.health -= 1
                            if ship.health == 0:
                                print("Sunk!")
                                self.cash += 100
            elif enemy.board[y][x] == "-":
                enemy.board[y][x] = "M"
        for row in enemy.board:
                    for i in range(12):
                        if i != 11:
                            print(row[i], end=" ")
                        else:
                            print(row[i])
        self.powerUps.remove("useAirstrike")
    def useUAV(self,enemy):
        choice = input("Which row[1]/column[A] do you want to reveal? ").upper()
        if choice.isdigit():
            y = int(choice)-1
            for x,v in enumerate(enemy.board):
                if v[y] == "S":
                    self.firingBoard[x][y] = "S"
                elif v[y] == "-":
                    self.firingBoard[x][y] = "M"
        else:
            x = ord(choice)-65
            for i,v in enumerate(enemy.board):
                if i == x:
                    for y,j in enumerate(v):
                        print(j)
                        if j == "S":
                            self.firingBoard[x][y] = "S"
                        if j == "-":
                            self.firingBoard[x][y] = "M"
                            
        for row in self.firingBoard:
                for i in range(12):
                    if i != 11:
                        print(row[i], end=" ")
                    else:
                        print(row[i])
        self.powerUps.remove("UAV")
    def useTwoMoves(self, enemy):
        self.shootMissile(enemy)
        self.shootMissile(enemy)
        self.powerUps.remove("useTwoMoves")
    def useXHit(self,enemy):
        coord = input("Place the center of your X strike: (A1 - L12) ").upper()
        if len(coord) == 2:
            y,x = int(coord[1])-1, ord(coord[0])-65
        self.shootMissileParam(enemy,y,x)
        if y-1 >= 0 and x-1 >= 0:
            self.shootMissileParam(enemy,y-1,x-1)
        if y+1 <= 11 and x+1 <= 11:
            self.shootMissileParam(enemy,y+1,x+1)
        if y-1 >= 0 and x+1 <= 11:
            self.shootMissileParam(enemy,y-1,x+1)
        if y+1 <= 11 and x-1 >= 0:
            self.shootMissileParam(enemy,y+1,x-1)
        for row in self.firingBoard:
            for i in range(12):
                if i != 11:
                    print(row[i], end=" ")
                else:
                    print(row[i])
        self.powerUps.remove("X Hit")
        