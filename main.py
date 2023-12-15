import player
player1 = player.Player([],[],100,1,[],[])
player1.createCleanBoard()
player1.createShipList()
player2 = player.Player([],[],100,2,[],[])
player2.createCleanBoard()
player2.createShipList()

from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.clock import Clock
import math
from kivy.config import Config
import random
from kivy.animation import Animation
from kivy.uix.label import Label
import time
from functools import partial
from kivy.uix.progressbar import ProgressBar
from kivy.core.window import Window

Config.set('graphics', 'resizable', True)
class BattleshipApp(App): 
    def build(self):
        Window.size = (1800, 950)
        Window.resizable = True
        game = GameManager()
        return game
    
class GameManager(Widget):
    def __init__(self, **args):
        super(GameManager, self).__init__(**args)
        self.startGame()
        
    def startGame(self):
        global playerTurn
        global currentPlayer
        global showBackground
        global placePhase
        global press2
        global press1
        global errorBox
        global player1ExtraTurn
        global player2ExtraTurn
        press1 = lambda x: player1.shootMissileParam(player2,t.text,errorBox)
        press2 = lambda x: player2.shootMissileParam(player1,t.text,errorBox)
        placePhase = True
        showBackground = True
        player1ExtraTurn = 0
        player2ExtraTurn = 0
        playerTurn = 1
        currentPlayer = player1
        self.makeBoard(player1)
        self.placeShip()
        self.placeShipText()
        self.label()
        self.instructions()
        self.errorBox()
        self.backgroundImageButton()
        self.clock = Clock.schedule_interval(self.update, 1.0/360.0)

    def make_shop(self, player):
        global cash     
        global errorBox
        global enemy
        global btn
        global shoplayout
        cash = Label(text = "Cash: " + str(player.cash), font_size = 50, size_hint = (1, 1), pos_hint = {"x":0, "y":0}, pos = (250, 825))

        self.add_widget(cash)
        
        shoplayout = GridLayout(cols = 3, rows = 5,size = (400, 200), pos = (100,650))
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

        self.add_widget(shoplayout)
    
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
        
    def updateCash(self,player):
        global cash
        cash.text = "Cash: " + str(player.cash)
    
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

    def backgroundImageButton(self):
        self.backgroundImage = Button(text ="", size = (2000, 1000),
                     background_normal = 'battleshipBG2.jpg',
                     size_hint = (2000, 1000),
                     pos_hint = {"x":100, "y":100}
                   )
        self.backgroundImage.bind(on_press = lambda x: self.clickedBackground(self.backgroundImage))
        self.add_widget(self.backgroundImage)
    
    def clickedBackground(self,btn):
        global showBackground
        self.remove_widget(btn)
        showBackground = False
        
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
        placeButton.bind(on_press = lambda x: currentPlayer.placeShip(shipLabel.text,currentPlayer.shipList[currentPlayer.ships - 1],placeShipLabel,errorBox))
        placeShipLayout.add_widget(placeButton)
        placeShipLayout.add_widget(shipLabel)
        self.add_widget(placeShipLayout)
    
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
            
    def checkInput(self):
        global t
        if len(t.text) != 2 and len(t.text) != 3:
            return (False)
        if t.text[0].upper() not in "ABCDEFGHIJKL" or t.text[1:] not in "123456789101112":
            return (False)
        return (True)
        
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
            self.backgroundImageButton()
            showBackground = True
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
            self.backgroundImageButton()
            showBackground = True
            
    def label(self):
        global mainLabel
        mainLabel = Label(text = "Player " + str(currentPlayer.number) + "'s turn", font_size = 50, size_hint = (1, 1), pos_hint = {"x":0, "y":0}, pos = (850, 675))
        self.add_widget(mainLabel)
    def instructions(self):
        global instruct
        instruct = Label(text = "To place a ship, input the spot [A1].\nThis will be the bottom or left corner of your ship.\nThen put a space followed by an 'h' for horziontal or a 'v' for vertical.\nExample: [A1 h]", font_size = 25, size_hint = (1, 1), pos_hint = {"x":0, "y":0}, pos = (1300, 250))
        self.add_widget(instruct)
    def placeShipText(self):
        global placeShipLabel
        placeShipLabel = Label(text = f"Place your {currentPlayer.shipList[-1].length} long ship", font_size = 50, size_hint = (1, 1), pos_hint = {"x":0, "y":0}, pos = (850, 600))
        self.add_widget(placeShipLabel)
    def errorBox(self):
        global errorBox
        errorBox = Label(text = "", font_size = 50, pos = (830, 750))
        self.add_widget(errorBox)
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
    
    def updateInput(self):
        global btn
        global currentPlayer
        if currentPlayer == player1:
            btn.unbind(on_press = press1)
            btn.bind(on_press = press2)
        elif currentPlayer == player2:
            btn.unbind(on_press = press2)
            btn.bind(on_press = press1)
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
            placeShipLabel.text = "Place your " + str(currentPlayer.shipList[0].length) + " length ship"
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
            
root = BattleshipApp() 
root.run()