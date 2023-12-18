import player
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.config import Config
from kivy.uix.label import Label
from kivy.core.window import Window

#create player variables
player1 = player.Player([],[],100,1,[],[])
player1.createCleanBoard()
player1.createShipList()
player2 = player.Player([],[],100,2,[],[])
player2.createCleanBoard()
player2.createShipList()

#set up config
Config.set('graphics', 'resizable', True)

#set up the AppWindow
class BattleshipApp(App): 
    def build(self):
        #Set Window size variables
        Window.size = (1800, 950)
        Window.resizable = True
        game = GameManager()
        return game

#Game Class
class GameManager(Widget):
    # when the program starts, run the start game function
    def __init__(self, **args):
        super(GameManager, self).__init__(**args)
        self.startGame()
        
    #start game function
    def startGame(self):
        #sets up global varaibles
        global playerTurn
        global currentPlayer
        global showBackground
        global placePhase
        global press2
        global press1
        global errorBox
        global player1ExtraTurn
        global player2ExtraTurn
        #sets up the functions for the buttons
        press1 = lambda x: player1.shootMissileParam(player2,t.text,errorBox)
        press2 = lambda x: player2.shootMissileParam(player1,t.text,errorBox)
        #sets up the game variables
        placePhase = True
        showBackground = True
        player1ExtraTurn = 0
        player2ExtraTurn = 0
        playerTurn = 1
        currentPlayer = player1
        #creates the game objects
        self.makeBoard(player1)
        self.placeShip()
        self.placeShipText()
        self.label()
        self.instructions2()
        self.errorBox()
        self.instructions()
        self.backgroundImageButton()
        #sets up a clock that runs a function every 1/360th of a second
        self.clock = Clock.schedule_interval(self.update, 1.0/360.0)

    #creates the instructions button
    def instructions2(self):
        instructionslayout = GridLayout(cols = 1, rows = 1,size = (100, 100), pos = (1500,650))
        button = Button(text ="Instructions", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        button.bind(on_press = lambda x: self.instructionsImageButton())
        instructionslayout.add_widget(button)
        self.add_widget(instructionslayout)


    #creates the shop layout
    def make_shop(self, player):
        #sets up global variables
        global cash     
        global errorBox
        global enemy
        global btn
        global shoplayout
        #creates cash label
        cash = Label(text = "Cash: " + str(player.cash), font_size = 50, size_hint = (1, 1), pos_hint = {"x":0, "y":0}, pos = (250, 825))
        self.add_widget(cash)
        #creates the shop layout
        shoplayout = GridLayout(cols = 3, rows = 5,size = (400, 200), pos = (100,650))
        btns = []
        twobytwoAmount = player.powerUps.count("2x2")
        airStrikeAmount = player.powerUps.count("Airstrike")
        UAVAmount = player.powerUps.count("UAV")
        twoMovesAmount = player.powerUps.count("Two Moves")
        xHitAmount = player.powerUps.count("X Hit")
        #creates the buttons
        btn1 = Button(text = f"Use 2x2: {twobytwoAmount}x", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn1.bind(on_press = lambda x: player.use2x2(enemy,t.text,errorBox))
        btn1.bind(on_release = lambda x: self.updateScreen())
        btn2 = Button(text = "Price: 40", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn3 = Button(text = "Buy 2x2", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn3.bind(on_press = lambda x: player.buy2x2(cash,errorBox))
        btn3.bind(on_release = lambda x: self.updateScreen())
        btn4 = Button(text = f"Use Air Strike: {airStrikeAmount}x", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn4.bind(on_press = lambda x: player.useAirstrike(enemy,errorBox))
        btn4.bind(on_release = lambda x: self.updateScreen())
        btn5 = Button(text = "Price: 40", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn6 = Button(text = "Buy Air Strike", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn6.bind(on_press = lambda x: player.buyAirstrike(cash,errorBox))
        btn6.bind(on_release = lambda x: self.updateScreen())
        btn7 = Button(text = f"Use UAV: {UAVAmount}x", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn7.bind(on_press = lambda x: player.useUAV(enemy, t.text, errorBox))
        btn7.bind(on_release = lambda x: self.updateScreen())
        btn8 = Button(text = "Price: 50", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn9 = Button(text = "Buy UAV", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn9.bind(on_press = lambda x: player.buyUAV(cash,errorBox))
        btn9.bind(on_release = lambda x: self.updateScreen())
        btn10 = Button(text = f"Use Extra Move: {twoMovesAmount}x", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn10.bind(on_press = lambda x: self.getExtraMove())
        btn10.bind(on_release = lambda x: self.updateScreen())
        btn11 = Button(text = "Price: 20", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn12 = Button(text = "Buy Extra Move", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn12.bind(on_press = lambda x: player.buyTwoMoves(cash,errorBox))
        btn12.bind(on_release = lambda x: self.updateScreen())
        btn13 = Button(text = f"Use X Hit: {xHitAmount}x", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn13.bind(on_press = lambda x: player.useXHit(enemy, t.text, errorBox))
        btn13.bind(on_release = lambda x: self.updateScreen())
        btn14 = Button(text = "Price: 40", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn15 = Button(text = "Buy X Hit", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn15.bind(on_press = lambda x: player.buyXHit(cash,errorBox))
        btn15.bind(on_release = lambda x: self.updateScreen())
        #adds the buttons to the layout
        btns.append(btn2)
        btns.append(btn3)
        btns.append(btn1)
        btns.append(btn5)
        btns.append(btn6)
        btns.append(btn4)
        btns.append(btn8)
        btns.append(btn9)
        btns.append(btn7)
        btns.append(btn11)
        btns.append(btn12)
        btns.append(btn10)
        btns.append(btn14)
        btns.append(btn15)
        btns.append(btn13)
        for i in btns:
            shoplayout.add_widget(i)

        self.add_widget(shoplayout)
    
    #updates the shop
    def update_shop(self,player):
        global cash     
        global errorBox
        global enemy
        global btn
        global shoplayout
        cash.text = "Cash: " + str(player.cash)
        shoplayout.clear_widgets()
        btns = []
        twobytwoAmount = player.powerUps.count("2x2")
        airStrikeAmount = player.powerUps.count("Airstrike")
        UAVAmount = player.powerUps.count("UAV")
        twoMovesAmount = player.powerUps.count("Two Moves")
        xHitAmount = player.powerUps.count("X Hit")
        btn1 = Button(text = f"Use 2x2: {twobytwoAmount}x", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn1.bind(on_press = lambda x: player.use2x2(enemy,t.text,errorBox))
        btn1.bind(on_release = lambda x: self.updateScreen())
        btn2 = Button(text = "Price: 40", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn3 = Button(text = "Buy 2x2", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn3.bind(on_press = lambda x: player.buy2x2(cash,errorBox))
        btn3.bind(on_release = lambda x: self.updateScreen())
        btn4 = Button(text = f"Use Air Strike: {airStrikeAmount}x", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn4.bind(on_press = lambda x: player.useAirstrike(enemy,errorBox))
        btn4.bind(on_release = lambda x: self.updateScreen())
        btn5 = Button(text = "Price: 40", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn6 = Button(text = "Buy Air Strike", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn6.bind(on_press = lambda x: player.buyAirstrike(cash,errorBox))
        btn6.bind(on_release = lambda x: self.updateScreen())
        btn7 = Button(text = f"Use UAV: {UAVAmount}x", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn7.bind(on_press = lambda x: player.useUAV(enemy, t.text, errorBox))
        btn7.bind(on_release = lambda x: self.updateScreen())
        btn8 = Button(text = "Price: 50", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn9 = Button(text = "Buy UAV", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn9.bind(on_press = lambda x: player.buyUAV(cash,errorBox))
        btn9.bind(on_release = lambda x: self.updateScreen())
        btn10 = Button(text = f"Use Extra Move: {twoMovesAmount}x", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn10.bind(on_press = lambda x: self.getExtraMove())
        btn10.bind(on_release = lambda x: self.updateScreen())
        btn11 = Button(text = "Price: 20", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn12 = Button(text = "Buy Extra Move", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn12.bind(on_press = lambda x: player.buyTwoMoves(cash,errorBox))
        btn12.bind(on_release = lambda x: self.updateScreen())
        btn13 = Button(text = f"Use X Hit: {xHitAmount}x", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn13.bind(on_press = lambda x: player.useXHit(enemy, t.text, errorBox))
        btn13.bind(on_release = lambda x: self.updateScreen())
        btn14 = Button(text = "Price: 40", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn15 = Button(text = "Buy X Hit", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn15.bind(on_press = lambda x: player.buyXHit(cash,errorBox))
        btn15.bind(on_release = lambda x: self.updateScreen())
        btns.append(btn2)
        btns.append(btn3)
        btns.append(btn1)
        btns.append(btn5)
        btns.append(btn6)
        btns.append(btn4)
        btns.append(btn8)
        btns.append(btn9)
        btns.append(btn7)
        btns.append(btn11)
        btns.append(btn12)
        btns.append(btn10)
        btns.append(btn14)
        btns.append(btn15)
        btns.append(btn13)
        for i in btns:
            shoplayout.add_widget(i)
        
    #updates the cash label
    def updateCash(self,player):
        global cash
        cash.text = "Cash: " + str(player.cash)
    
    #gets the extra move powerup
    def getExtraMove(self):
        global errorBox
        if currentPlayer.powerUps.count("Two Moves") == 0:
            errorBox.text = "You do not have an extra move!"
        if currentPlayer.powerUps.count("Two Moves") > 0:
            currentPlayer.powerUps.remove("Two Moves")
        else:
            errorBox.text = "You do not have an extra move!"
        if currentPlayer == player1:
            global player1ExtraTurn
            player1ExtraTurn += 1
        elif currentPlayer == player2:
            global player2ExtraTurn
            player2ExtraTurn += 1

    #creates instructions image button
    def instructionsImageButton(self):
        self.instructionImageButton = Button(text ="", size = (2000, 1000),
                     background_normal = 'instructions3.jpg',
                     size_hint = (2000, 1000),
                     pos_hint = {"x":100, "y":100}
                   )
        self.instructionImageButton.bind(on_press = lambda x: self.clickedBackground(self.instructionImageButton))
        self.add_widget(self.instructionImageButton)

    #creates background image button
    def nextTurnImageButton(self):
        self.nextTurnImage = Button(text ="", size = (2000, 1000),
                     background_normal = 'metalBG2.jpg',
                     size_hint = (2000, 1000),
                     pos_hint = {"x":100, "y":100}
                   )
        self.nextTurnImage.bind(on_press = lambda x: self.clickedBackground(self.nextTurnImage))
        self.add_widget(self.nextTurnImage)

    #creates background image button
    def backgroundImageButton(self):
        self.backgroundImage = Button(text ="", size = (2000, 1000),
                     background_normal = 'battleshipBG2.jpg',
                     size_hint = (2000, 1000),
                     pos_hint = {"x":100, "y":100}
                   )
        self.backgroundImage.bind(on_press = lambda x: self.clickedBackground(self.backgroundImage))
        self.add_widget(self.backgroundImage)
    
    #removes the background image button when clicked
    def clickedBackground(self,btn):
        global showBackground
        self.remove_widget(btn)
        showBackground = False
        
    #creates the place ship input and button
    def placeShip(self):
        global placeShipLayout
        global placeShipLabel
        placeShipLayout = GridLayout(cols = 1, rows = 2,size = (150, 200), pos = (800,200))
        shipLabel = TextInput(font_size = 50, 
                      size_hint_y = None, 
                      height = 100)
        placeButton = Button(text ="Place Ship",
                        background_color =(255, 1, 1, 1),
                        size = (100, 100),
                        pos = (0,0),
                    )
        global currentPlayer
        placeButton.bind(on_press = lambda x: currentPlayer.placeShip(shipLabel.text,currentPlayer.shipList[-currentPlayer.ships],placeShipLabel,errorBox))
        placeShipLayout.add_widget(placeButton)
        placeShipLayout.add_widget(shipLabel)
        self.add_widget(placeShipLayout)
    
    #makes the players board
    def makeBoard(self,player):
        global layout
        layout = GridLayout(cols = 12, rows = 12,size = (500, 500), pos = (200,0))
        for y,row in enumerate(player.board):
            for x,cell in enumerate(row):
                if cell == "-":
                    layout.add_widget(Button(text ="",
                        background_color =(1, 1, 1, 1),
                        size = (100, 100),
                        pos = (0,0),
                    ))
                elif cell == "S":
                    layout.add_widget(Button(text ="",
                        background_color =(1, 1, 255, 1),
                        size = (100, 100),
                        pos = (0,0),
                    ))
                elif cell == "M":
                    layout.add_widget(Button(text ="",
                        background_color =(255, 255, 255, 1),
                        size = (100, 100),
                        pos = (0,0),
                    ))
                elif cell == "H":
                    layout.add_widget(Button(text ="",
                        background_color =(255, 1, 1, 1),
                        size = (100, 100),
                        pos = (0,0),
                    ))
        #creates the labels for the board
        labelLayoutY = GridLayout(cols = 12, rows = 1,size = (500, 500), pos = (200,275))
        letters = ["A","B","C","D","E","F","G","H","I","J","K","L"]
        for i in letters:
            labelLayoutY.add_widget(Label(text = i, font_size = 32))
        
        labelLayoutX = GridLayout(cols = 1, rows = 12,size = (500, 500), pos = (475,0))
        for i in range(12):
            labelLayoutX.add_widget(Label(text = str(i+1), font_size = 32)) 
        self.add_widget(labelLayoutY)
        self.add_widget(labelLayoutX)
        self.add_widget(layout)
    
    #creates the firing board
    def makeFiringBoard(self,player):
        global firingLayout
        firingLayout = GridLayout(cols = 12, rows = 12,size = (500, 500), pos = (1050,0))
        for y,row in enumerate(player.firingBoard):
            for x,cell in enumerate(row):
                if cell == "-":
                    firingLayout.add_widget(Button(text ="",
                        background_color =(1, 1, 1, 1),
                        size = (100, 100),
                        pos = (0,0),
                    ))
                elif cell == "S":
                    firingLayout.add_widget(Button(text ="",
                        background_color =(1, 1, 255, 1),
                        size = (100, 100),
                        pos = (0,0),
                    ))
                elif cell == "M":
                    firingLayout.add_widget(Button(text ="",
                        background_color =(255, 255, 255, 1),
                        size = (100, 100),
                        pos = (0,0),
                    ))
                elif cell == "H":
                    firingLayout.add_widget(Button(text ="",
                        background_color =(255, 1, 1, 1),
                        size = (100, 100),
                        pos = (0,0),
                    ))
        
        #creates the labels for the board
        labelLayoutY = GridLayout(cols = 12, rows = 1,size = (500, 500), pos = (1050,275))
        letters = ["A","B","C","D","E","F","G","H","I","J","K","L"]
        for i in letters:
            labelLayoutY.add_widget(Label(text = i, font_size = 32))
        
        labelLayoutX = GridLayout(cols = 1, rows = 12,size = (500, 500), pos = (1325,0))
        for i in range(12):
            labelLayoutX.add_widget(Label(text = str(i+1), font_size = 32)) 
        self.add_widget(labelLayoutY)
        self.add_widget(labelLayoutX)
        self.add_widget(firingLayout)
    
    #creates the input and button for the firing function
    def takeInput(self,player):
        layout = GridLayout(cols = 1, rows = 2,size = (150, 200), pos = (800,200))
        global t
        t = TextInput(font_size = 50, 
                      size_hint_y = None, 
                      height = 100)
        global btn
        btn = Button(text ="Fire!",
                        background_color =(255, 1, 1, 1),
                        size = (100, 100),
                        pos = (0,0),
                    )
        
        if currentPlayer == player1:
            btn.bind(on_press = press1)
        elif currentPlayer == player2:
            btn.bind(on_press = press2)
        btn.bind(on_release = lambda x: self.release())
        layout.add_widget(btn)
        layout.add_widget(t)
        self.add_widget(layout)
    
    #updates the screen
    def updateScreen(self):
        print(currentPlayer.number,enemy.number)
        if playerTurn == player1:
            if currentPlayer.checkWin(enemy) == True:
                print("Player" + str(currentPlayer.number) + " wins!")
                errorBox.text = str(currentPlayer.number) + " wins!"
            mainLabel.text = "Player " + str(currentPlayer.number) + "'s turn"
            self.updateFiringBoard(currentPlayer)
            self.updateMyBoard(currentPlayer)
            self.updateCash(currentPlayer)
            self.update_shop(currentPlayer)
        elif playerTurn == player2:
            if currentPlayer.checkWin(enemy) == True:
                print(str(currentPlayer.number) + " wins!")
            mainLabel.text = "Player " + str(currentPlayer.number) + "'s turn"
            self.updateFiringBoard(currentPlayer)
            self.updateMyBoard(currentPlayer)
            self.updateCash(currentPlayer)
            self.update_shop(currentPlayer)
            
    #checks if the input is valid
    def checkInput(self):
        global t
        if len(t.text) != 2 and len(t.text) != 3:
            return (False)
        if t.text[0].upper() not in "ABCDEFGHIJKL" or t.text[1:] not in "123456789101112":
            return (False)
        return (True)
        
    #on rlease of a button, switch turns
    def release(self):
        global currentPlayer
        global playerTurn
        global btn
        global firingLayout
        global mainLabel
        global enemy
        global errorBox
        global showBackground
        global player1ExtraTurn
        global player2ExtraTurn
        #if the player has an extra turn, give them an extra turn
        if player1ExtraTurn > 0:
            if self.checkInput() == False:
                return()
            player1ExtraTurn -= 1
            self.updateFiringBoard(currentPlayer)
            self.updateMyBoard(currentPlayer)
            self.updateCash(currentPlayer)
            errorBox.text = ""
            if currentPlayer.checkWin(enemy) == True:
                print("Player" + str(currentPlayer.number) + " wins!")
                errorBox.text = str(currentPlayer.number) + " wins!"
            return()
        elif playerTurn == player1:
            if self.checkInput() == False:
                return()
            self.updateInput()
            if currentPlayer.checkWin(enemy) == True:
                print("Player" + str(currentPlayer.number) + " wins!")
                errorBox.text = str(currentPlayer.number) + " wins!"
            currentPlayer = player2
            mainLabel.text = "Player " + str(currentPlayer.number) + "'s turn"
            enemy = player1
            self.updateFiringBoard(currentPlayer)
            self.updateMyBoard(currentPlayer)
            self.updateCash(currentPlayer)
            errorBox.text = ""
            self.update_shop(currentPlayer)
            self.nextTurnImageButton()
            showBackground = True
        #if the player has an extra turn, give them an extra turn
        elif player2ExtraTurn > 0:
            if self.checkInput() == False:
                return()
            player2ExtraTurn -= 1
            self.updateFiringBoard(currentPlayer)
            self.updateMyBoard(currentPlayer)
            self.updateCash(currentPlayer)
            errorBox.text = ""
            if currentPlayer.checkWin(enemy) == True:
                print(str(currentPlayer.number) + " wins!")
            return()
        elif playerTurn == player2:
            if self.checkInput() == False:
                return()
            self.updateInput()
            if currentPlayer.checkWin(enemy) == True:
                print(str(currentPlayer.number) + " wins!")
            currentPlayer = player1
            mainLabel.text = "Player " + str(currentPlayer.number) + "'s turn"
            enemy = player2
            self.updateFiringBoard(currentPlayer)
            self.updateMyBoard(currentPlayer)
            self.updateCash(currentPlayer)
            errorBox.text = ""
            self.update_shop(currentPlayer)
            self.nextTurnImageButton()
            showBackground = True
            
    #shows which players turn it is
    def label(self):
        global mainLabel
        mainLabel = Label(text = "Player " + str(currentPlayer.number) + "'s turn", font_size = 50, size_hint = (1, 1), pos_hint = {"x":0, "y":0}, pos = (850, 675))
        self.add_widget(mainLabel)
    #shows base instructions
    def instructions(self):
        global instruct
        instruct = Label(text = "To place a ship, input the spot [A1].\nThis will be the bottom or left corner of your ship.\nThen put a space followed by an 'h' for horziontal or a 'v' for vertical.\nExample: [A1 h]", font_size = 25, size_hint = (1, 1), pos_hint = {"x":0, "y":0}, pos = (1300, 250))
        self.add_widget(instruct)
    #shows the place ship text
    def placeShipText(self):
        global placeShipLabel
        placeShipLabel = Label(text = f"Place your {currentPlayer.shipList[-currentPlayer.ships].length} long ship", font_size = 50, size_hint = (1, 1), pos_hint = {"x":0, "y":0}, pos = (850, 600))
        self.add_widget(placeShipLabel)
    #shows errors
    def errorBox(self):
        global errorBox
        errorBox = Label(text = "", font_size = 50, pos = (830, 750))
        self.add_widget(errorBox)
    #updates the players board
    def updateMyBoard(self,player):
        global layout
        layout.clear_widgets()
        for y,row in enumerate(player.board):
            for x,cell in enumerate(row):
                if cell == "-":
                    layout.add_widget(Button(text ="",
                        background_color =(1, 1, 1, 1),
                        size = (100, 100),
                        pos = (0,0),
                    ))
                elif cell == "S":
                    layout.add_widget(Button(text ="",
                        background_color =(1, 1, 255, 1),
                        size = (100, 100),
                        pos = (0,0),
                    ))
                elif cell == "M":
                    layout.add_widget(Button(text ="",
                        background_color =(255, 255, 255, 1),
                        size = (100, 100),
                        pos = (0,0),
                    ))
                elif cell == "H":
                    layout.add_widget(Button(text ="",
                        background_color =(255, 1, 1, 1),
                        size = (100, 100),
                        pos = (0,0),
                    ))
    #updates the firing board
    def updateFiringBoard(self,player):
        global firingLayout
        firingLayout.clear_widgets()
        for y,row in enumerate(player.firingBoard):
            for x,cell in enumerate(row):
                if cell == "-":
                    firingLayout.add_widget(Button(text ="",
                        background_color =(1, 1, 1, 1),
                        size = (100, 100),
                        pos = (0,0),
                    ))
                elif cell == "S":
                    firingLayout.add_widget(Button(text ="",
                        background_color =(1, 1, 255, 1),
                        size = (100, 100),
                        pos = (0,0),
                    ))
                elif cell == "M":
                    firingLayout.add_widget(Button(text ="",
                        background_color =(255, 255, 255, 1),
                        size = (100, 100),
                        pos = (0,0),
                    ))
                elif cell == "H":
                    firingLayout.add_widget(Button(text ="",
                        background_color =(255, 1, 1, 1),
                        size = (100, 100),
                        pos = (0,0),
                    ))
    #updates the input label and box
    def updateInput(self):
        global btn
        global currentPlayer
        if currentPlayer == player1:
            btn.unbind(on_press = press1)
            btn.bind(on_press = press2)
        elif currentPlayer == player2:
            btn.unbind(on_press = press2)
            btn.bind(on_press = press1)
    #runs every 1/360th of a second and manages each game state
    def update(self,ndt):
        global currentPlayer
        global showBackground
        global placePhase
        global playerTurn
        global instruct
        global enemy
        if showBackground == False and placePhase == True:
            self.updateMyBoard(currentPlayer)
        if placePhase == False and showBackground == False:
            playerTurn = currentPlayer
        if player1.ships == 0 and player2.ships != 0 and currentPlayer == player1 and placePhase == True:
            currentPlayer = player2
            mainLabel.text = "Player " + str(currentPlayer.number) + "'s turn"
            placeShipLabel.text = "Place your " + str(currentPlayer.shipList[-currentPlayer.ships].length) + " length ship"
        elif player2.ships == 0 and placePhase == True:
            currentPlayer = player1
            enemy = player2
            mainLabel.text = "Player " + str(currentPlayer.number) + "'s turn"
            placePhase = False
            self.makeBoard(currentPlayer)
            self.makeFiringBoard(currentPlayer)
            self.remove_widget(placeShipLayout)
            self.make_shop(currentPlayer)
            self.takeInput(currentPlayer)
            instruct.text = "To fire, input the spot [A1].\nThis will be the spot you fire at."
            instruct.pos = (825, 550)
            self.remove_widget(placeShipLabel)
            self.instructions2()
            
root = BattleshipApp() 
root.run()