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
ledgeGroup = pygame.sprite.Group()
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
                bulletGroup.empty()
                level(1, levelCounter, 'images/light_background.png', False, 0)
            elif (levelCounter == 2):
                level(2, levelCounter, 'images/medium_background.png', True, 1)
            elif (levelCounter == 3):
                level(2, levelCounter, 'images/city_background.png', True, 2)
            elif (levelCounter == 4):
                level(3, levelCounter, 'images/misty_background.jpg', True, 3)
            levelCounter += 1
            player.rect.x = 0
            bulletGroup.empty()
            ledgeGroup.empty()
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
    back2menu = button("Main Menu (m)", 'fonts/Antonio-Regular.ttf', 40, white, red, hoverred, 1875, 970, 25, back2menu)

    #UPDATE
    playerGroup.update()
    enemyGroup.update()
    bulletGroup.update()
    ledgeGroup.update()

    #DRAW
    playerGroup.draw(gameDisplay)
    enemyGroup.draw(gameDisplay)
    bulletGroup.draw(gameDisplay)
    ledgeGroup.draw(gameDisplay)

    pygame.display.update()

    if back2menu == False:
        return True



def level(num_enemy, level_num, background, isLedge, num_ledge_enemies):
    for i in range(num_enemy):
        enemy = characters.Enemy()
        enemyGroup.add(enemy)
    if isLedge:
        ledge = characters.Ledge()
        ledgeGroup.add(ledge)
    for j in range(num_ledge_enemies):
        ledge_enemy = characters.ledgeEnemy()
        enemyGroup.add(ledge_enemy)
    level_bkgd = pygame.image.load(background)
    level_bkgd = pygame.transform.scale(level_bkgd, (2000, 1000))
    player.rect.x = 0
    while True:
        logic(level_bkgd)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    play = False
            if event.type == pygame.QUIT:
                pygame.quit()
        if (player.rect.x >= display_width) and (len(enemyGroup.sprites()) == 0):
            break
        elif (player.rect.x >= (display_width - player.size)) and (len(enemyGroup.sprites()) > 0):
            player.rect.x = display_width - player.size
