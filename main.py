import player
player1 = player.Player([],[],100,1,[])
player1.createCleanBoard()
player2 = player.Player([],[],100,2,[])
player2.createCleanBoard()


def main():
    for i in player1.board:
        print(i)
    player1.createShipList()
    player2.createShipList()
    player1.placeShip()
    player2.placeShip()
    while True:
        player1.buyPowerUps()
        power1 = player1.usePowerUp()
        if power1 != False:
            player1.choosePowerUp()
        else:
            player1.shootMissile(player2)
        if player1.checkWin():
            print("Player 1 wins!")
            break
        player2.buyPowerUps()
        player2.usePowerUp()
        player2.shootMissile(player1)
        if player2.checkWin():
            print("Player 2 wins!")
            break

main()