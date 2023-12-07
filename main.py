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
font = pygame.font.SysFont("Arial", 30)
start_button = pygame.image.load("startGame2.png")
start_button = pygame.transform.scale(start_button, (300, 70))
gameBG = pygame.image.load("metalBG.jpg")
boardBG = pygame.image.load("Board.jpg")
gameBG = pygame.transform.scale(gameBG, (width, height))
boardBG = pygame.transform.scale(boardBG, (width/3, height/2 ))
player_board_text = font.render("Your Board", True, (225, 0, 0))
enemy_board_text = font.render("Enemy Board", True, (225, 0, 0))
base_font = pygame.font.Font(None, 32)
user_text = '' 
input_rect = pygame.Rect(600, 300, 140, 32) 


line_color = (225, 0, 0)


def main_menu():
    SCREEN.blit(BG, (0, 0))
    pygame.display.set_caption("Battleship")
    start_button_rect = start_button.get_rect(center = (1100, 660))
    SCREEN.blit(start_button, start_button_rect)
    while True:
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        pygame.display.update()
        main_clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(MENU_MOUSE_POS):
                    game()

        pygame.display.update()

def game():
    SCREEN.blit(gameBG, (0, 0))
    SCREEN.blit(boardBG, (100, 75))
    SCREEN.blit(boardBG, (750, 75))
    SCREEN.blit(player_board_text, (100, 30))
    SCREEN.blit(enemy_board_text, (750, 30))
    pygame.draw.rect(SCREEN, 'lightskyblue3', input_rect)
    user_text = '' 
    while True:
        pygame.display.update()
        main_clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN: 
  
                # Check for backspace 
                if event.key == pygame.K_BACKSPACE:  
                    user_text = ''
                    pygame.draw.rect(SCREEN, 'lightskyblue3', input_rect)
                else: 
                    user_text += event.unicode

        text_surface = base_font.render(user_text, True, (255, 255, 255))
        SCREEN.blit(text_surface, (input_rect.x+5, input_rect.y+5)) 
      
        input_rect.w = max(100, text_surface.get_width()+10)

        










        pygame.display.update()

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