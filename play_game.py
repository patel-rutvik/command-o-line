import pygame
from util import displayText, button
import characters

QUIT = False
black = (0, 0, 0)
white = (255, 255, 255)
green = (100, 200, 100)
red = (200, 0, 0)
hoverred = (230, 0, 0)
yellow = (180, 180, 0)
hoveryellow = (200, 200, 0)
display_width, display_height = 2000, 1000
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width, display_height))
background = pygame.image.load('images/game_background.jpg')
background = pygame.transform.scale(background, (2000, 1000))


playerGroup = pygame.sprite.Group()
player = characters.Player()
playerGroup.add(player)
enemyGroup = pygame.sprite.Group()
bulletGroup = pygame.sprite.Group()
keys = pygame.key.get_pressed()


def playGame():
    play = True
    levelCounter = 1
    #transition = True
    while play:     
        menu_state = logic(background)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    play = False
            if event.type == pygame.QUIT:
                return True
        # IF the level counter > 1 then add pick ups
        if (player.rect.x > display_width):
            if (levelCounter == 1):
                level_1()
            elif (levelCounter == 2):
                level_2()
            levelCounter += 1
            player.rect.x = 0
        if menu_state == True:
            play = False


def logic(bkgd):
    gameDisplay.blit(bkgd, (0, 0))
        
    if player.shot == True:
        bullet = characters.Bullet(player.rect.x, player.rect.y, player.facing, player.location)
        bulletGroup.add(bullet)
        player.canShoot = False
    hitList = pygame.sprite.groupcollide(bulletGroup, enemyGroup, True, False)
    for bull in hitList:
        for enmy in hitList[bull]:
            enmy.health -= bull.damage
    for enemy in enemyGroup.sprites():
        if enemy.alive == False:
            enemy.remove(enemyGroup)
    for bullet in bulletGroup.sprites():
        if bullet.alive == False:
            bulletGroup.remove(bullet)
    back2menu = False
    back2menu = button("Main Menu (m)", 'Antonio-Regular.ttf', 40, white, red, hoverred, 1875, 970, 25, back2menu)

    #UPDATE
    playerGroup.update()
    enemyGroup.update()
    bulletGroup.update()

    #DRAW
    playerGroup.draw(gameDisplay)
    enemyGroup.draw(gameDisplay)
    bulletGroup.draw(gameDisplay)

    pygame.display.update()

    if back2menu == False:
        return True



def level_1():
    enemy = characters.Enemy()
    enemyGroup.add(enemy)
    level_bkgd = pygame.image.load('images/light_background.png')
    level_bkgd = pygame.transform.scale(level_bkgd, (2000, 1000))
    level_1 = True
    player.rect.x = 0
    while level_1:
        logic(level_bkgd)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    play = False
            if event.type == pygame.QUIT:
                pygame.quit()
        if (player.rect.x > display_width):
            level_1 = False


def level_2():
    pass
