import pygame
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

class BattleshipApp(App): 
    def build(self):
        game = GameManager()
        return game
    


class GameManager(Widget):
    def __init__(self, **args):
        super(GameManager, self).__init__(**args)
        self.startGame()


    def startGame(self):
        self.makeBoard(player1)
        self.placeShip()
        self.backgroundImageButton()
        global playerTurn
        global currentPlayer
        global showBackground
        global placePhase
        placePhase = True
        showBackground = True
        playerTurn = 1
        currentPlayer = player1
        self.clock = Clock.schedule_interval(self.update, 1.0/360.0)

    def make_shop(self, player):
        layout = GridLayout(cols = 3, rows = 5,size = (200, 200), pos = (100,750))
        btns = []
        btn1 = Button(text = "2x2", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn2 = Button(text = "Price: 50", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn3 = Button(text = "Buy", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn3.bind(on_press = lambda x: player.buy2x2())
        btn4 = Button(text = "Air Strike", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn5 = Button(text = "Price: 50", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn6 = Button(text = "Buy", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn6.bind(on_press = lambda x: player.buyAirStrike())   
        btn7 = Button(text = "UAV", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn8 = Button(text = "Price: 50", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn9 = Button(text = "Buy", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn9.bind(on_press = lambda x: player.buyUAV())
        btn10 = Button(text = "2 Moves", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn11 = Button(text = "Price: 50", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn12 = Button(text = "Buy", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn12.bind(on_press = lambda x: player.buyTwoMoves())
        btn13 = Button(text = "X Hit", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn14 = Button(text = "Price: 50", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn15 = Button(text = "Buy", background_color =(255, 1, 1, 1), size = (100, 100), pos = (0,0))
        btn15.bind(on_press = lambda x: player.buyXHit())
        btns.append(btn1)
        btns.append(btn2)
        btns.append(btn3)
        btns.append(btn4)
        btns.append(btn5)
        btns.append(btn6)
        btns.append(btn7)
        btns.append(btn8)
        btns.append(btn9)
        btns.append(btn10)
        btns.append(btn11)
        btns.append(btn12)
        btns.append(btn13)
        btns.append(btn14)
        btns.append(btn15)
        for i in btns:
            layout.add_widget(i)


        global cash       
        cash = Label(text = "Cash: " + str(player.cash), font_size = 50, size_hint = (1, 1), pos_hint = {"x":0, "y":0}, pos = (150, 670))

        self.add_widget(cash)
        self.add_widget(layout)

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
        placeShipLayout = GridLayout(cols = 1, rows = 2,size = (200, 200), pos = (500,200))
        shipLabel = TextInput(font_size = 50, 
                      size_hint_y = None, 
                      height = 100)
        placeButton = Button(text ="Place Ship",
                        background_color =(255, 1, 1, 1),
                        size = (100, 100),
                        pos = (0,0),
                    )
        global currentPlayer
        placeButton.bind(on_press = lambda x: currentPlayer.placeShip(currentPlayer.shipList[0],int(shipLabel.text[1:shipLabel.text.index(" ")])-1,ord(shipLabel.text[0])-65,shipLabel.text[shipLabel.text.index(" ")+1:]))
        placeShipLayout.add_widget(placeButton)
        placeShipLayout.add_widget(shipLabel)
        self.add_widget(placeShipLayout)
    
    def makeBoard(self,player):
        global layout
        layout = GridLayout(cols = 12, rows = 12,size = (500, 500), pos = (0,0))
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
        self.add_widget(layout)
    
    def makeFiringBoard(self,player):
        global firingLayout
        firingLayout = GridLayout(cols = 12, rows = 12,size = (500, 500), pos = (700,0))
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
        self.add_widget(firingLayout)
    
    def takeInput(self,player):
        layout = GridLayout(cols = 1, rows = 2,size = (200, 200), pos = (500,0))
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
            btn.bind(on_press = lambda x: player1.shootMissileParam(player2,int(t.text[1:])-1,ord(t.text[0])-65))
        elif currentPlayer == player2:
            btn.bind(on_press = lambda x: player2.shootMissileParam(player1,int(t.text[1:])-1,ord(t.text[0])-65))
        btn.bind(on_release = lambda x: self.release())
        layout.add_widget(btn)
        layout.add_widget(t)
        self.add_widget(layout)
    
    def release(self):
        global currentPlayer
        global playerTurn
        global btn
        global firingLayout
        global showBackground
        if playerTurn == player1:
            btn.bind(on_press = lambda x: player2.shootMissileParam(player1,int(t.text[1:])-1,ord(t.text[0])-65))
            currentPlayer = player2
            layout.clear_widgets()
            firingLayout.clear_widgets()
            self.makeBoard(currentPlayer)
            self.makeFiringBoard(currentPlayer)
            self.backgroundImageButton()
            showBackground = True
        elif playerTurn == player2:
            btn.bind(on_press = lambda x: player1.shootMissileParam(player2,int(t.text[1:])-1,ord(t.text[0])-65))
            currentPlayer = player1
            layout.clear_widgets()
            firingLayout.clear_widgets()
            self.makeBoard(currentPlayer)
            self.makeFiringBoard(currentPlayer)
            self.backgroundImageButton()
            showBackground = True
    
    def update(self,ndt):
        global currentPlayer
        global showBackground
        global placePhase
        global playerTurn
        if showBackground == False and placePhase == True:
            layout.clear_widgets()
            self.makeBoard(currentPlayer)
        if placePhase == False and showBackground == False:
            layout.clear_widgets()
            firingLayout.clear_widgets()
            self.makeBoard(currentPlayer)
            self.makeFiringBoard(currentPlayer)
            global cash
            self.make_shop(currentPlayer)
            self.remove_widget(cash)
            if currentPlayer!= playerTurn:
                self.takeInput(currentPlayer)
            playerTurn = currentPlayer
        if player1.shipList == [] and player2.shipList != [] and currentPlayer == player1 and placePhase == True:
            currentPlayer = player2
        elif player2.shipList == [] and placePhase == True:
            currentPlayer = player1
            placePhase = False
            self.makeBoard(currentPlayer)
            self.makeFiringBoard(currentPlayer)
            self.remove_widget(placeShipLayout)
            self.takeInput(currentPlayer)
            
        
                    
        

root = BattleshipApp() 
root.run()



'''def main():
    for i in player1.board:
        print(i)
    player1.createShipList()
    player2.createShipList()
    print("Player 1 place your ships: ")
    player1.placeShip()
    print("Player 2 place your ships: ")
    player2.placeShip()
    while True:
        print("Player 1: ")
        player1.buyPowerUps()
        power1 = player1.usePowerUp()
        if power1 != False:
            player1.choosePowerUp(player2)
        else:
            print("Player 1 did not use a power up.")
            print("Player 1: ")
            player1.shootMissile(player2)
        if player1.checkWin():
            print("Player 1 wins!")
            break
        print("Player 2: ")
        player2.buyPowerUps()
        power2 = player2.usePowerUp()
        if power2 != False:
            player2.choosePowerUp(player1)
        else:
            print("Player 2 did not use a power up.")
            print("Player 2: ")
            player2.shootMissile(player1)
        if player2.checkWin():
            print("Player 2 wins!")
            break

main()'''