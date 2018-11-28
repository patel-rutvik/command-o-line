import pygame
from util import displayText, button
import characters

black = (0, 0, 0)
white = (255, 255, 255)
green = (100, 200, 100)
red = (200, 0, 0)
yellow = (180, 180, 0)
hoveryellow = (200, 200, 0)
display_width, display_height = 2000, 1000
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width, display_height))
background = pygame.image.load('game_background.jpg')
background = pygame.transform.scale(background, (2000, 1000))

all_sprites = pygame.sprite.Group()
player = characters.Player()
all_sprites.add(player)
goomba = characters.Enemy()
all_sprites.add(goomba)
keys = pygame.key.get_pressed()


def playGame():
    play = True

    while play:
        gameDisplay.fill(black)
        gameDisplay.blit(background, (0, 0))

        #UPDATE
        player.update()

        #DRAW
        all_sprites.draw(gameDisplay)


        #END PLAY
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    play = False
            if event.type == pygame.QUIT:
                #play = False
                return True ### Quit does not work...
        pygame.display.update()