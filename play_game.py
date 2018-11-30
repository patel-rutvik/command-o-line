import pygame
from util import displayText, button
import characters

QUIT = False
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


playerGroup = pygame.sprite.Group()
player = characters.Player()
playerGroup.add(player)
enemyGroup = pygame.sprite.Group()
bulletGroup = pygame.sprite.Group()
keys = pygame.key.get_pressed()


def playGame():
    play = True

    while play:     
        logic(playerGroup, enemyGroup, bulletGroup)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    play = False
            if event.type == pygame.QUIT:
                return True
        if (player.rect.x > display_width):
            level_1()
            print("Nice")

def logic(playerGroup, enemyGroup, bulletGroup):
    gameDisplay.blit(background, (0, 0))
    print(bulletGroup.sprites())
        
    if player.shot == True:
        bullet = characters.Bullet(player.rect.x, player.rect.y, player.facing)
        bulletGroup.add(bullet)
    for enemy in enemyGroup:
        if pygame.sprite.spritecollideany(enemy, bulletGroup):
            pygame.sprite.groupcollide(bulletGroup, enemyGroup, True, False)
            enemy.health -= 10
    for enemy in enemyGroup.sprites():
        if enemy.alive == False:
            enemy.remove(enemyGroup)
    for bullet in bulletGroup.sprites():
        if bullet.alive == False:
            bulletGroup.remove(bullet)

    #UPDATE
    playerGroup.update()
    enemyGroup.update()
    bulletGroup.update()

    #DRAW
    playerGroup.draw(gameDisplay)
    enemyGroup.draw(gameDisplay)
    bulletGroup.draw(gameDisplay)

    pygame.display.update()



def level_1():
    enemy = characters.Enemy()
    enemyGroup.add(enemy)
    level_bkgd = pygame.image.load('medium_background.png')
    level_bkgd = pygame.transform.scale(level_bkgd, (2000, 1000))
    level_1 = True
    player.rect.x = 0
    while level_1:
        logic(playerGroup, enemyGroup, bulletGroup)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    play = False
            if event.type == pygame.QUIT:
                pygame.quit()
        if (player.rect.x > display_width):
            level_1 = False


