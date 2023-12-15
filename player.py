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
        self.ships = 0
    def createCleanBoard(self):
        self.board = []
        self.firingBoard = []
        for i in range(12):
            self.board.append(["-"]*12)
            self.firingBoard.append(["-"]*12)
            
    def createShipList(self):
        self.shipList.append(ship.Ship(5,5,[]))
        self.ships += 1
        self.shipList.append(ship.Ship(4,4,[]))
        self.ships += 1
        #self.shipList.append(ship.Ship(3,3,[]))
        #self.ships += 1
        #self.shipList.append(ship.Ship(3,3,[]))
        #self.ships += 1
        #self.shipList.append(ship.Ship(2,2,[]))
        #self.ships += 1
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
        error.text = ""
        self.ships -= 1
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
        if len(inp) != 2 and len(inp) != 3:
            error.text = "Invalid input! Try again"
            return ()
        if inp[0].upper() not in "ABCDEFGHIJKL" or inp[1:] not in "123456789101112":
            error.text = "Invalid input! Try again"
            return ()
        y = int(inp[1:])-1
        x = ord(inp[0].upper())-65
        if enemy.board[y][x] == "S":
            self.firingBoard[y][x] = "H"
            enemy.board[y][x] = "H"
            self.cash += 10
            for i in enemy.shipList:
                for coord in i.coordinates:
                    if coord == [y,x]:
                        i.health -= 1
                        if i.health == 0:
                            print("Sunk!")
        elif enemy.board[y][x] == "H":
            print("Already hit!")
        elif enemy.board[y][x] == "-":
            self.firingBoard[y][x] = "M"
            enemy.board[y][x] = "M"
            print("Miss!")
    
    def buyPowerUps(self):

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
        if self.cash < 40:
            print("Not enough cash!")
            error.text = "Not enough cash!"
            return False
        else:
            self.cash -= 40
            self.powerUps.append("2x2")
            print("2x2 power up bought!")
            error.text = "2x2 power up bought!"
        cash.text = "Cash: " + str(self.cash)
    
    def buyUAV(self,cash,error):
        if self.cash < 50:
            print("Not enough cash!")
            error.text = "Not enough cash!"
            return False
        else:
            self.cash -= 50
            self.powerUps.append("UAV")
            print("UAV power up bought!")
            error.text = "UAV power up bought!"
        cash.text = "Cash: " + str(self.cash)
    
    def buyAirstrike(self,cash,error):
        if self.cash < 40:
            print("Not enough cash!")
            error.text = "Not enough cash!"
            return False
        else:
            self.cash -= 40
            self.powerUps.append("Airstrike")
            print("Airstrike power up bought!")
            error.text = "Airstrike power up bought!"
        cash.text = "Cash: " + str(self.cash)
    
    def buyTwoMoves(self,cash,error):
        print(self.cash,self.number)
        if self.cash < 20:
            print("Not enough cash!")
            error.text = "Not enough cash!"
            return False
        else:
            self.cash -= 20
            self.powerUps.append("Two Moves")
            print("Two Moves power up bought!")
            error.text = "Two Moves power up bought!"
        cash.text = "Cash: " + str(self.cash)

    def buyXHit(self,cash,error):
        if self.cash < 40:
            print("Not enough cash!")
            error.text = "Not enough cash!"
            return False
        else:
            self.cash -= 40
            self.powerUps.append("X Hit")
            print("X Hit power up bought!")
            error.text = "X Hit power up bought!"
        cash.text = "Cash: " + str(self.cash)
    
    def useXHit(self,enemy, coord, error):
        print(coord)
        if self.powerUps.count("X Hit") == 0:
            error.text = "You don't have an X Hit!"
            return()
        if len(coord) != 2 and len(coord) != 3:
            error.text = "Invalid input! Try again"
            return ()
        if coord[0].upper() not in "ABCDEFGHIJKL" or coord[1:] not in "123456789101112":
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
            error.text = "You don't have a 2x2!"
            return()
        if len(coord) != 2 and len(coord) != 3:
            error.text = "Invalid input! Try again"
            return ()
        if coord[0].upper() not in "ABCDEFGHIJKL" or coord[1:] not in "123456789101112":
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
    def useAirstrike(self, enemy, error):
        coords = []
        coord_options = []
        if self.powerUps.count("Airstrike") == 0:
            error.text = "You don't have an Airstrike!"
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

    def useUAV(self,enemy, coord,error):
        print(coord)
        if self.powerUps.count("UAV") == 0:
            error.text = "You don't have a UAV!"
            return()
        if len(coord) != 1:
            error.text = "Invalid input! Try again"
            return ()
        if str(coord[0]) not in "abcdefghijklABCDEFGHIJKL123456789101112":
            error.text = "Invalid input! Try again"
            return ()
        if coord.isnumeric():
            y = int(coord)-1
            for x in range(12):
                if enemy.board[y][x] == "S":
                    self.firingBoard[y][x] = "S"
                elif enemy.board[y][x] == "-":
                    self.firingBoard[y][x] = "M"
        else:
            x=coord.upper()
            x = ord(x)-65
            for y in range(12):
                if enemy.board[y][x] == "S":
                    self.firingBoard[y][x] = "S"
                elif enemy.board[y][x] == "-":
                    self.firingBoard[y][x] = "M"

        self.powerUps.remove("UAV")
    def useTwoMoves(self, enemy,error):
        if self.powerUps.count("Two Moves") == 0:
            error.text = "You don't have a Two Moves!"
            return()
        self.shootMissile(enemy)
        self.shootMissile(enemy)
        self.powerUps.remove("useTwoMoves")

   
        
    def checkWin(self,enemy):
        for i in enemy.shipList:
            if i.health != 0:
                return False
        return True
        
