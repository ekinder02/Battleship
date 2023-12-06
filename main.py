import pygame
import player
player1 = player.Player([],[],100,1,[],[])
player1.createCleanBoard()
player2 = player.Player([],[],100,2,[],[])
player2.createCleanBoard()

pygame.init()
main_clock = pygame.time.Clock()
height = 720
width = 1280
SCREEN = pygame.display.set_mode((width, height))
BG = pygame.image.load("battleshipBG2.jpg")
BG = pygame.transform.scale(BG, (width, height))

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))
        pygame.display.update()
        main_clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass

main_menu()






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