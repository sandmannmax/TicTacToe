import pygame, game

pygame.init()
gameDisplay = pygame.display.set_mode((400,400))
pygame.display.set_caption('TicTacToe')
clock = pygame.time.Clock()
table = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
dict1 = {1:(13,13),2:(146,13),3:(277,13),4:(13,146),5:(146,146),6:(277,146),7:(13,277),8:(146,277),9:(277,277)}

tableImg = pygame.image.load('table-tictactoe.png')
oImg = pygame.image.load('circle-tictactoe.png')
xImg = pygame.image.load('x-tictactoe.png')

gameDisplay.blit(tableImg,(0,0))

close = False
count = 0

while not close:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close = True
        if pygame.mouse.get_pressed()[0] == 1:
            if game.getPosXY(pygame.mouse.get_pos()) != 0:
                if game.getPosHelp(game.getPosXY(pygame.mouse.get_pos()), table) == -1:
                    tabel = game.insert(game.getPosXY(pygame.mouse.get_pos()), str((count%2)+1), table)
                    if (count%2)+1 == 1:
                        gameDisplay.blit(oImg,dict1[game.getPosXY(pygame.mouse.get_pos())])
                    elif (count%2)+1 == 2:
                        gameDisplay.blit(xImg,dict1[game.getPosXY(pygame.mouse.get_pos())])
                    count += 1
        if game.test(table) == 1 or game.test(table) == 2:
            close = True
        pygame.display.update()
        clock.tick(30)

pygame.quit()
quit()
