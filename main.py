import pygame
import player
player1 = player.Player([],[],100,1,[],[])
player1.createCleanBoard()
player2 = player.Player([],[],100,2,[],[])
player2.createCleanBoard()

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
        self.SelectionBar()
    
    def SelectionBar(self):
        layout = GridLayout(cols = 12, rows = 12,size = (500, 500), pos = (0,0))
        
        for i in range(144):
            layout.add_widget(Button(text ="",
                        color =(1, 1, 1, 1),
                        size = (100, 100),
                        pos = (0,0),
                    ))
        self.add_widget(layout)

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