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
        #self.shipList.append(ship.Ship(4,4,[]))
        #self.shipList.append(ship.Ship(3,3,[]))
        #self.shipList.append(ship.Ship(3,3,[]))
        #self.shipList.append(ship.Ship(2,2,[]))
    def placeShip(self,place,ship,placeShipLabel,error):
        if ship == None:
            return ()
        if len(place)!= 4 and len(place) != 5:
            error.text = "Invalid input! Replace ship"
            return ()
        if place[0] not in "ABCDEFGHIJKLabcdefghijkl" or place[1:3].replace(" ","") not in "123456789101112":
            error.text = "Invalid input! Replace ship"
            return ()
        if place[place.index(" ")+1:].lower() not in "vh":
            error.text = "Invalid input! Replace ship"
            print("here")
            return ()
        y = int(place[1:place.index(" ")])-1
        x = ord(place[0].upper())-65
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
    
    def shootMissileParam(self,enemy,inp,error):
        if inp[0].upper() not in "ABCDEFGHIJKL" or inp[1:] not in "123456789101112":
            print("Invalid input! Try again")
            error.text = "Invalid input! Try again"
            return ()
        if len(inp) != 2 and len(inp) != 3:
            print("Invalid input! Try again")
            error.text = "Invalid input! Try again"
            return ()
        y = int(inp[1:])-1
        x = ord(inp[0].upper())-65
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
            elif x == "two moves":
                self.buyTwoMoves()
            elif x == "x hit":
                self.buyXHit()
        else:
            return False
        
    def buy2x2(self,cash,error):
        if self.cash < 10:
            print("Not enough cash!")
            error.text = "Not enough cash!"
            return False
        else:
            self.cash -= 10
            self.powerUps.append("2x2")
            print("2x2 power up bought!")
            error.text = "2x2 power up bought!"
        cash.text = "Cash: " + str(self.cash)
    
    def buyUAV(self,cash,error):
        if self.cash < 25:
            print("Not enough cash!")
            error.text = "Not enough cash!"
            return False
        else:
            self.cash -= 25
            self.powerUps.append("UAV")
            print("UAV power up bought!")
            error.text = "UAV power up bought!"
        cash.text = "Cash: " + str(self.cash)
    
    def buyAirstrike(self,cash,error):
        if self.cash < 50:
            print("Not enough cash!")
            error.text = "Not enough cash!"
            return False
        else:
            self.cash -= 50
            self.powerUps.append("Airstrike")
            print("Airstrike power up bought!")
            error.text = "Airstrike power up bought!"
        cash.text = "Cash: " + str(self.cash)
    
    def buyTwoMoves(self,cash,error):
        print(self.cash,self.number)
        if self.cash < 50:
            print("Not enough cash!")
            error.text = "Not enough cash!"
            return False
        else:
            self.cash -= 50
            self.powerUps.append("Two Moves")
            print("Two Moves power up bought!")
            error.text = "Two Moves power up bought!"
        cash.text = "Cash: " + str(self.cash)

    def buyXHit(self,cash,error):
        if self.cash < 50:
            print("Not enough cash!")
            error.text = "Not enough cash!"
            return False
        else:
            self.cash -= 50
            self.powerUps.append("X Hit")
            print("X Hit power up bought!")
            error.text = "X Hit power up bought!"
        cash.text = "Cash: " + str(self.cash)
    
    def useXHit(self,enemy, coord, error):
        print(coord)
        if self.powerUps.count("X Hit") == 0:
            return()
        if coord[0].upper() not in "ABCDEFGHIJKL" or coord[1:] not in "123456789101112":
            print("Invalid input! Try again")
            error.text = "Invalid input! Try again"
            return ()
        if len(coord) != 2 and len(coord) != 3:
            print("Invalid input! Try again")
            error.text = "Invalid input! Try again"
            return ()
        y,x = int(coord[1:])-1, ord(coord[0].upper())-65
        if enemy.board[y][x] == "S":
            enemy.board[y][x] = "H"
            self.firingBoard[y][x] = "H"
            for ship in enemy.shipList:
                for coord in ship.coordinates:
                    if coord == [y,x]:
                        ship.health -= 1
                        if ship.health == 0:
                            print("Sunk!")
                            self.cash += 100
        if enemy.board[y][x] == "-":
            enemy.board[y][x] = "M"
            self.firingBoard[y][x] = "M"
        if enemy.board[y+1][x+1] == "S":
            enemy.board[y+1][x+1] = "H"
            self.firingBoard[y+1][x+1] = "H"
            for ship in enemy.shipList:
                for coord in ship.coordinates:
                    if coord == [y+1,x+1]:
                        ship.health -= 1
                        if ship.health == 0:
                            print("Sunk!")
                            self.cash += 100
        if enemy.board[y+1][x+1] == "-":
            enemy.board[y+1][x+1] = "M"
            self.firingBoard[y+1][x+1] = "M"
        if enemy.board[y-1][x-1] == "S":
            enemy.board[y-1][x-1] = "H"
            self.firingBoard[y-1][x-1] = "H"
            for ship in enemy.shipList:
                for coord in ship.coordinates:
                    if coord == [y-1,x-1]:
                        ship.health -= 1
                        if ship.health == 0:
                            print("Sunk!")
                            self.cash += 100
        if enemy.board[y-1][x-1] == "-":
            enemy.board[y-1][x-1] = "M"
            self.firingBoard[y-1][x-1] = "M"
        if enemy.board[y+1][x-1] == "S":
            enemy.board[y+1][x-1] = "H"
            self.firingBoard[y+1][x-1] = "H"
            for ship in enemy.shipList:
                for coord in ship.coordinates:
                    if coord == [y+1,x-1]:
                        ship.health -= 1
                        if ship.health == 0:
                            print("Sunk!")
                            self.cash += 100
        if enemy.board[y+1][x-1] == "-":
            enemy.board[y+1][x-1] = "M"
            self.firingBoard[y+1][x-1] = "M"
        if enemy.board[y-1][x+1] == "S":
            enemy.board[y-1][x+1] = "H"
            self.firingBoard[y-1][x+1] = "H"
            for ship in enemy.shipList:
                for coord in ship.coordinates:
                    if coord == [y-1,x+1]:
                        ship.health -= 1
                        if ship.health == 0:
                            print("Sunk!")
                            self.cash += 100
        if enemy.board[y-1][x+1] == "-":
            enemy.board[y-1][x+1] = "M"
            self.firingBoard[y-1][x+1] = "M"

        for row in self.firingBoard:
            for i in range(12):
                if i != 11:
                    print(row[i], end=" ")
                else:
                    print(row[i])
        self.powerUps.remove("X Hit")
        

    def use2x2(self, enemy, coord,error):
        if self.powerUps.count("2x2") == 0:
            return()
        if coord[0].upper() not in "ABCDEFGHIJKL" or coord[1:] not in "123456789101112":
            print("Invalid input! Try again")
            error.text = "Invalid input! Try again"
            return ()
        if len(coord) != 2 and len(coord) != 3:
            print("Invalid input! Try again")
            error.text = "Invalid input! Try again"
            return ()
        y,x = int(coord[1:])-1, ord(coord[0].upper())-65
        for i in range(2):
            for j in range(2):
                if enemy.board[y-i][x+j] == "S":
                    enemy.board[y-i][x+j] = "H"
                    self.firingBoard[y-i][x+j] = "H"
                    for ship in enemy.shipList:
                        for coord in ship.coordinates:
                            if coord == [y-i,x+j]:
                                ship.health -= 1
                                if ship.health == 0:
                                    print("Sunk!")
                                    self.cash += 100
                elif enemy.board[y-i][x+j] == "-":
                    enemy.board[y-i][x+j] = "M"
                    self.firingBoard[y-i][x+j] = "M"
        self.powerUps.remove("2x2")
    def useAirstrike(self, enemy):
        coords = []
        coord_options = []
        
        if self.powerUps.count("Airstrike") == 0:
            return()
        
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
                self.firingBoard[y][x] = "H"
                for ship in enemy.shipList:
                    for coord in ship.coordinates:
                        if coord == [y,x]:
                            ship.health -= 1
                            if ship.health == 0:
                                print("Sunk!")
                                self.cash += 100
            elif enemy.board[y][x] == "-":
                enemy.board[y][x] = "M"
                self.firingBoard[y][x] = "M"
                
        self.powerUps.remove("Airstrike")

    def useUAV(self,enemy):
        if self.powerUps.count("UAV") == 0:
            return()
        choices = ["A","B","C","D","E","F","G","H","I","J","K","L","1","2","3","4","5","6","7","8","9","10","11","12"]
        choice = random.choice(choices)
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

        self.powerUps.remove("UAV")
    def useTwoMoves(self, enemy):
        self.shootMissile(enemy)
        self.shootMissile(enemy)
        self.powerUps.remove("useTwoMoves")
    