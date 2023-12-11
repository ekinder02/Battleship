
import player
player1 = player.Player([],[],100,1,[],[])
player1.createCleanBoard()
player1.createShipList()
player2 = player.Player([],[],100,2,[],[])
player2.createCleanBoard()

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
        self.takeInput(player1)
        self.makeFiringBoard(player1)
        self.placeShip(player1)
        global playerTurn
        playerTurn = 1
    
    def placeShip(self,player):
        layout = GridLayout(cols = 1, rows = 2,size = (200, 200), pos = (500,200))
        shipLabel = TextInput(font_size = 50, 
                      size_hint_y = None, 
                      height = 100)
        placeButton = Button(text ="Place Ship",
                        background_color =(255, 1, 1, 1),
                        size = (100, 100),
                        pos = (0,0),
                    )
        placeButton.bind(on_press = lambda x: player.placeShip(player.shipList[0],int(shipLabel.text[1:shipLabel.text.index(" ")])-1,ord(shipLabel.text[0])-65,shipLabel.text[shipLabel.text.index(" ")+1:]))
        layout.add_widget(placeButton)
        layout.add_widget(shipLabel)
        self.add_widget(layout)
    
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
        
        btn.bind(on_press = lambda x: player.shootMissileParam(player2,int(t.text[1:])-1,ord(t.text[0])-65))
        btn.bind(on_release = lambda x: self.release())
        layout.add_widget(btn)
        layout.add_widget(t)
        self.add_widget(layout)
    
    def release(self):
        global playerTurn
        global btn
        global firingLayout
        print("playerTurn: ",playerTurn)
        if playerTurn == 1:
            layout.clear_widgets()
            firingLayout.clear_widgets()
            self.makeBoard(player2)
            self.makeFiringBoard(player2)
            btn.bind(on_press = lambda x: player2.shootMissileParam(player1,int(t.text[1:])-1,ord(t.text[0])-65))
            playerTurn = 2
        elif playerTurn == 2:
            layout.clear_widgets()
            firingLayout.clear_widgets()
            self.makeBoard(player1)
            self.makeFiringBoard(player1)
            btn.bind(on_press = lambda x: player1.shootMissileParam(player2,int(t.text[1:])-1,ord(t.text[0])-65))
            playerTurn = 1
    
    # def update(self,ndt):
        
                    
        

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