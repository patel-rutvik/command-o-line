import pygame
from util import displayText, button
import characters
import time

QUIT = False
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 200)
hoverblue = (0, 0, 255)
green = (100, 200, 100)
hovergreen = (100, 240, 100)
red = (200, 0, 0)
hoverred = (230, 0, 0)
yellow = (180, 180, 0)
hoveryellow = (200, 200, 0)
display_width, display_height = 2000, 1000
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width, display_height))


background = pygame.image.load('images/game_background.jpg')
background = pygame.transform.scale(background, (2000, 1000))
arrow = pygame.image.load('images/arrow.png')
arrow = pygame.transform.scale(arrow, (150, 100))
stand = pygame.image.load('images/stand.png')
stand = pygame.transform.scale(stand, (500,500))
merchant = pygame.image.load('images/merchant.png')
merchant = pygame.transform.scale(merchant, (125, 200))
bubble = pygame.image.load('images/speech_bubble.png')
bubble = pygame.transform.scale(bubble, (400, 250))
heart = pygame.image.load('images/heart.png')
heart = pygame.transform.scale(heart, (100, 100))
ammo_pic = pygame.image.load('images/ammo_crate.png')
ammo_pic = pygame.transform.scale(ammo_pic, (100, 100))
half_heart = pygame.image.load('images/half_heart.png')
half_heart = pygame.transform.scale(half_heart, (50, 50))
small_ammo = pygame.image.load('images/ammo_crate.png')
small_ammo = pygame.transform.scale(small_ammo, (50, 50))

playerGroup = pygame.sprite.Group()
player = characters.Player()
playerGroup.add(player)
enemyGroup = pygame.sprite.Group()
bulletGroup = pygame.sprite.Group()
ledgeGroup = pygame.sprite.Group()
enemyBulletGroup = pygame.sprite.Group()
pickupGroup = pygame.sprite.Group()



def playGame():
    play = True
    levelCounter = 1
    temp_play = None
    player.health = 100
    player.ammo = 50
    enemies = [[[1, 2 ,3 ,4 ,5], [0, 0, 1, 1, 1]], [[1, 2, 3, 5, 5], [0, 0, 1, 2, 2]], [[1, 2, 4, 5, 6], [0, 0, 1, 3, 5]]]
    button_size = int((display_width / display_height) * 25)
    pressed = False
    garbage = ""
    easy = None
    medium = None
    hard = None
    #time.sleep(0.2)

    while play:
        if easy != None or medium != None or hard != None:
            pressed = True
        if not pressed:
            keys = pygame.key.get_pressed()
            gameDisplay.blit(background, (0, 0))
            displayText("COMMAND-O-LINE", 'fonts/Antonio-Bold.ttf', 200, display_width / 2, (display_height / 5), white, 0)
            easy = button("Easy [e]", 'fonts/Antonio-Regular.ttf', button_size, white, green, 
                            hovergreen, display_width / 5 + 250, display_height - button_size, 50, True)
            medium = button("Medium [m]", 'fonts/Antonio-Regular.ttf', button_size, white, blue,
                                 hoverblue, display_width / 2, display_height - button_size, 50, 
                                 True)
            hard = button("Hard [h]", 'fonts/Antonio-Regular.ttf', button_size, white, red, hoverred,
                            (4*display_width) / 5 - 250, display_height - button_size, 50, True)
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_e:
                        easy = True
                    elif event.key == pygame.K_m:
                        medium = True
                    elif event.key == pygame.K_h:
                        hard = True
                        
                if event.type == pygame.QUIT:
                    return True
                    
            pygame.display.update()

        elif pressed:
            menu_state = logic(background, False, levelCounter)
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
                    enemyBulletGroup.empty()
                    pickupGroup.empty()
                    #if easy:
                    temp_play = level(1, levelCounter, 'images/light_background.png', False, 0)
                elif (levelCounter == 2):
                    temp_play = level(2, levelCounter, 'images/medium_background.png', False, 0)
                elif (levelCounter == 3):
                    temp_play = level(1, levelCounter, 'images/city_background.png', True, 1)
                elif (levelCounter == 4):
                    temp_play = level(1, levelCounter, 'images/misty_background.jpg', True, 1)
                elif (levelCounter == 5):
                    temp_play = level(1, levelCounter, 'images/game_background.jpg', True, 1)
                levelCounter += 1
                player.rect.x = 0
                bulletGroup.empty()
                ledgeGroup.empty()
                enemyBulletGroup.empty()
                pickupGroup.empty()
            if temp_play == False or menu_state == True:
                play = False


def logic(bkgd, playing, level_count):
    gameDisplay.blit(bkgd, (0, 0))
    back2menu = False
    if playing:
        if player.shot == True:
            bullet = characters.Bullet(player.rect.x, player.rect.y, player.facing, player.location)
            bulletGroup.add(bullet)
            player.canShoot = False
            player.ammo -= 1
        pygame.sprite.groupcollide(bulletGroup, ledgeGroup, True, False)
        hitList = pygame.sprite.groupcollide(bulletGroup, enemyGroup, True, False)
        for bull in hitList:
            for enmy in hitList[bull]:
                enmy.health -= bull.damage
        for enemy in enemyGroup.sprites():
            if enemy.shot == True:
                enemyBullet = characters.enemyBullet(player.rect.x, player.rect.y, enemy.facing, enemy.rect.x, enemy.rect.y)
                enemyBulletGroup.add(enemyBullet)
                enemy.shot = False
            if enemy.alive == False:
                enemy.remove(enemyGroup)
        for bullet in bulletGroup.sprites():
            if bullet.alive == False:
                bulletGroup.remove(bullet)
        if pygame.sprite.groupcollide(enemyBulletGroup, playerGroup, True, False):
            player.health -= 10

    else:
        gameDisplay.blit(merchant, (3*display_width / 5 + 400, characters.floor - 50))
        gameDisplay.blit(stand, (display_width / 3 + 400, characters.floor - 300))
        gameDisplay.blit(bubble, ((3*display_width / 5) + 300, characters.floor - 290))
        if level_count == 1:
            displayText("This is where you can restock!", 'fonts/Antonio-Regular.ttf', 25, (3*display_width/5) + 500, characters.floor - 235, black, 10)
            displayText("Come back later to take", 'fonts/Antonio-Regular.ttf', 25, (3*display_width/5) + 500, characters.floor - 185, black, 10)
            displayText("a look at my merchandise.", 'fonts/Antonio-Regular.ttf', 25, (3*display_width/5) + 500, characters.floor - 135, black, 10)
        elif level_count > 1 and level_count <= 5:
            displayText("Take a step into my shop!", 'fonts/Antonio-Regular.ttf', 25, (3*display_width/5) + 500, characters.floor - 235, black, 10)
            displayText("You can only pick one...", 'fonts/Antonio-Regular.ttf', 25, (3*display_width/5) + 500, characters.floor - 185, black, 10)
            displayText("Jump to select.", 'fonts/Antonio-Regular.ttf', 25, (3*display_width/5) + 500, characters.floor - 135, black, 10)

            if pickupGroup.sprites() == []:
                health_pickup = characters.pickUp(heart, display_width / 2 - 700, characters.floor - 200, "health", player)
                ammo_pickup = characters.pickUp(ammo_pic, display_width / 2 - 400, characters.floor - 200, "ammo", player)
                both_pickup = characters.pickUp(half_heart, display_width / 2 - 110, characters.floor - 170, "both", player)
                pickupGroup.add(health_pickup, ammo_pickup, both_pickup)

            sprite = pygame.sprite.spritecollideany(player, pickupGroup)
            if sprite != None and len(pickupGroup.sprites()) == 3:
                sprite.collide = True
                pickupGroup.update()
                pygame.sprite.groupcollide(pickupGroup, playerGroup, True, False)


        elif level_count == 6:
            pickupGroup.empty()
            gameDisplay.blit(bubble, ((3*display_width / 5) + 300, characters.floor - 290))
            displayText("Wow, you killed them all!", 'fonts/Antonio-Regular.ttf', 25, (3*display_width/5) + 500, characters.floor - 235, black, 10)
            displayText("I have nothing left to sell...", 'fonts/Antonio-Regular.ttf', 25, (3*display_width/5) + 500, characters.floor - 185, black, 10)
            displayText("I am not worthy.", 'fonts/Antonio-Regular.ttf', 25, (3*display_width/5) + 500, characters.floor - 135, black, 10)
            if player.rect.x >= display_width + characters.char_size:
                player.rect.x = display_width
        if level_count < 6:
            startString = str('Level ' + str(level_count))
            displayText(startString, 'fonts/Antonio-Bold.ttf', 30, display_width - 75, characters.floor - 70, black, 15)
            gameDisplay.blit(arrow, (display_width - 150, characters.floor - 60))

    #UPDATE
    pickupGroup.update()
    playerGroup.update()
    enemyGroup.update()
    bulletGroup.update()
    ledgeGroup.update()
    enemyBulletGroup.update()

    #DRAW
    pickupGroup.draw(gameDisplay)
    playerGroup.draw(gameDisplay)
    enemyGroup.draw(gameDisplay)
    bulletGroup.draw(gameDisplay)
    ledgeGroup.draw(gameDisplay)
    enemyBulletGroup.draw(gameDisplay)

    pygame.draw.rect(gameDisplay, black, ((0, 0), (display_width, display_height / 15)))
    healthString = str("Health: " + str(player.health) + "/100")
    ammoString = str("Ammo: " + str(player.ammo) + "/100")
    displayText(healthString, 'fonts/Antonio-Regular.ttf', 30, 100, 30, white, 25)
    displayText(ammoString , 'fonts/Antonio-Regular.ttf', 30, 500, 30, white, 25)

    if playing:
        pickupGroup.empty()
        if (len(enemyGroup.sprites()) == 0):
            displayText("LEVEL COMPLETE", 'fonts/Antonio-Bold.ttf', 75, display_width / 2, display_height / 4, black, 50)
            displayText("Next stage", 'fonts/Antonio-Bold.ttf', 30, display_width - 75, characters.floor - 70, black, 15)
            gameDisplay.blit(arrow, (display_width - 150, characters.floor - 60))
        enemyString = str('Enemies remaining: ' + str(len(enemyGroup.sprites())))
        levelString = str('Level: ' + str(level_count))
        displayText(enemyString, 'fonts/Antonio-Regular.ttf', 30, 1850, 30, white, 20)
        displayText(levelString, 'fonts/Antonio-Regular.ttf', 40, display_width / 2, 30, white, 20)
    else:
        back2menu = False
        back2menu = button("Main Menu (m)", 'fonts/Antonio-Regular.ttf', 40, white, red, hoverred, 1875, 970, 25, back2menu)


    pygame.display.update()

    if back2menu == False:
        return True



def level(num_enemy, level_num, background, isLedge, num_ledge_enemies):
    gameOver = False
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
        logic(level_bkgd, True, level_num)
        #pygame.display.update()
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
        if not player.alive:
            playerGroup.empty()
            enemyGroup.empty()
            break
    if not player.alive:
        death_time = pygame.time.get_ticks()
        while True:
            keys = pygame.key.get_pressed()
            displayText("GAME OVER", 'fonts/Antonio-Bold.ttf', 200, display_width / 2, display_height / 4, black, 50)
            pygame.display.update()
            present_time = pygame.time.get_ticks()
            if present_time - death_time >= 4500:
                return False
