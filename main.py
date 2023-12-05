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
    print("Player 1 place your ships: ")
    player1.placeShip()
    print("Player 2 place your ships: ")
    player2.placeShip()
    while True:
        print("Player 1: ")
        player1.buyPowerUps()
        power1 = player1.usePowerUp()
        if power1 != False:
            player1.choosePowerUp()
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
            player2.choosePowerUp()
        else:
            print("Player 2 did not use a power up.")
            print("Player 2: ")
            player2.shootMissile(player1)
        if player2.checkWin():
            print("Player 2 wins!")
            break

main()