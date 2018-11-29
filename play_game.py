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
background = pygame.image.load('light_background.png')
background = pygame.transform.scale(background, (2000, 1000))


all_sprites = pygame.sprite.Group()
player = characters.Player()
all_sprites.add(player)
keys = pygame.key.get_pressed()


def playGame():
    play = True

    while play:
        gameDisplay.blit(background, (0, 0))
        
        if player.shot == True:
            bullet = characters.Bullet(player.rect.x, player.rect.y, player.facing)
            all_sprites.add(bullet)

        #UPDATE
        all_sprites.update()

        #DRAW
        all_sprites.draw(gameDisplay)

        if (player.rect.x > display_width):
            level_1()
            player.rect.x = 0

        #END PLAY
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    play = False
            if event.type == pygame.QUIT:
                return True
        pygame.display.update()

def level_1():
    goomba = characters.Enemy()
    all_sprites.add(goomba)
    level_bkgd = pygame.image.load('medium_background.png')
    level_bkgd = pygame.transform.scale(level_bkgd, (2000, 1000))
    level_1 = True
    # while level_1:........

