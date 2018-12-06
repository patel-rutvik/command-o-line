import pygame
from util import displayText, button
import characters
import sys

# declaring our global variables
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
gameDisplay = pygame.display.set_mode((display_width, display_height))

# importing all the images needed
background = pygame.image.load('../images/game_background.jpg')
background = pygame.transform.scale(background, (2000, 1000))
arrow = pygame.image.load('../images/arrow.png')
arrow = pygame.transform.scale(arrow, (150, 100))
stand = pygame.image.load('../images/stand.png')
stand = pygame.transform.scale(stand, (500,500))
merchant = pygame.image.load('../images/merchant.png')
merchant = pygame.transform.scale(merchant, (125, 200))
bubble = pygame.image.load('../images/speech_bubble.png')
bubble = pygame.transform.scale(bubble, (400, 250))
heart = pygame.image.load('../images/heart.png')
heart = pygame.transform.scale(heart, (100, 100))
ammo_pic = pygame.image.load('../images/ammo_crate.png')
ammo_pic = pygame.transform.scale(ammo_pic, (100, 100))
half_heart = pygame.image.load('../images/half_heart.png')
half_heart = pygame.transform.scale(half_heart, (50, 50))
small_ammo = pygame.image.load('../images/ammo_crate.png')
small_ammo = pygame.transform.scale(small_ammo, (50, 50))

# creating all the sprites and their corresponding groups
playerGroup = pygame.sprite.Group()
player = characters.Player()
playerGroup.add(player)
enemyGroup = pygame.sprite.Group()
bulletGroup = pygame.sprite.Group()
ledgeGroup = pygame.sprite.Group()
enemyBulletGroup = pygame.sprite.Group()
pickupGroup = pygame.sprite.Group()
boss = characters.bossGuy()


# The play game function is the main driver function of this file.
# It takes in no parameters but it calls all the other functions in
# this file to run the game logic and run the level design. Finally,
# this function returns the current state if the user decides to quit.
def playGame():
    # initializing the levels
    faceRight()
    player.alive = True
    play = True
    levelCounter = 1
    temp_play = None
    player.health = 100
    player.ammo = 100
    # 3D list of enemies, including ground enemies and ledge enemies for each level
    enemies = [[[1, 2 ,2 ,3 ,3, 0], [0, 0, 1, 1, 1, 0]], [[1, 3, 3, 3, 4, 0], [0, 0, 1, 2, 2, 0]], [[1, 2, 3, 4, 4, 0], [0, 0, 1, 3, 4, 0]]]
    # the list of image addresses for the backgrounds
    backgrounds = ['../images/light_background.png', '../images/medium_background.png', '../images/city_background.png', '../images/misty_background.jpg', '../images/game_background.jpg', '../images/game_background.jpg']
    # the list of bool values to indicate whether or not to make a ledge
    # for that corresponding level
    ledges = [False, False, True, True, True, False]
    button_size = int((display_width / display_height) * 25)
    pressed = False
    difficulty = [None, None, None]

    while play:
        if difficulty[0] != None or difficulty[1] != None or difficulty[2] != None:
                pressed = True
        # checking if user has selected a difficulty or not
        if not pressed:

            keys = pygame.key.get_pressed()
            gameDisplay.blit(background, (0, 0))
            displayText("COMMAND-O-LINE", '../fonts/Antonio-Bold.ttf', 200, display_width / 2, (display_height / 5), white, 0)

            # creating difficulty selecting buttons
            difficulty[0] = button("Easy [e]", '../fonts/Antonio-Regular.ttf', button_size, white, green, 
                            hovergreen, display_width / 5 + 250, display_height - button_size, 50, True)
            difficulty[1] = button("Medium [m]", '../fonts/Antonio-Regular.ttf', button_size, white, blue,
                                 hoverblue, display_width / 2, display_height - button_size, 50, 
                                 True)
            difficulty[2] = button("Hard [h]", '../fonts/Antonio-Regular.ttf', button_size, white, red, hoverred,
                            (4*display_width) / 5 - 250, display_height - button_size, 50, True)
            
            # handling key press to select difficulty
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_e:
                        difficulty[0] = True
                    elif event.key == pygame.K_m:
                        difficulty[1] = True
                    elif event.key == pygame.K_h:
                        difficulty[2] = True
                        
                if event.type == pygame.QUIT:
                    return True
                    
            pygame.display.update()

        # if difficulty has been selected...
        elif pressed:
            menu_state = logic(background, False, levelCounter)

            # handling quit
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        play = False
                if event.type == pygame.QUIT:
                    return True

            if (player.rect.x > display_width):
                # make the level
                temp_play = levelMaker(difficulty, levelCounter, enemies, backgrounds, ledges)
                # after level is finished, increase the level count
                levelCounter += 1
                # reset screen and level
                resetLevel()
            if temp_play == False or menu_state:
                play = False


# This function simply empties all the sprite groups and 
# resets player position
def resetLevel():
    player.rect.x = 0
    bulletGroup.empty()
    ledgeGroup.empty()
    enemyBulletGroup.empty()
    pickupGroup.empty()


# This function takes in the following parameters...
# bkgd : background address of the background to be displayed
# playing: check if the user is in the playing state or not
# level_count: the current level the user is on
def logic(bkgd, playing, level_count):
    # THINGS THAT HAPPEN ALL THE TIME
    gameDisplay.blit(bkgd, (0, 0))
    back2menu = False
    makeStatbar()

    #THINGS THAT HAPPEN ONLY WHILE PLAYING
    if playing:
        pickupGroup.empty()
        levelStatbar(level_count)

        if (len(enemyGroup.sprites()) == 0):
            display_complete()

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

        if level_count == 6:
            boss.add(enemyGroup)
            if boss.health <= 0:
                enemyGroup.empty()

    #THINGS THAT HAPPEN WHEN NOT PLAYING
    else:
        display_merchant()
        back2menu = button("Main Menu (m)", '../fonts/Antonio-Regular.ttf', 40, white, red, hoverred, 1875, 970, 25, back2menu)
        startString = str('Level ' + str(level_count))
        displayText(startString, '../fonts/Antonio-Bold.ttf', 30, display_width - 75, characters.floor - 70, black, 15)
        gameDisplay.blit(arrow, (display_width - 150, characters.floor - 60))
        if level_count == 1:
            merchantDialogue("intro")

        elif level_count > 1 and level_count < 6:
            merchantDialogue("normal")

            makeSprites()

            getCollision()


        elif level_count == 6:
            youWon()

        elif level_count > 6 and boss.health <= 0:
            bossWin()
            back2menu = button("Main Menu (m)", '../fonts/Antonio-Regular.ttf', 40, white, red, hoverred, 1875, 970, 25, back2menu)
            
    updateDraw()

    pygame.display.update()

    if back2menu == False:
        return True



def level(num_enemy, level_num, background, isLedge, num_ledge_enemies):
    gameOver = False

    # creating enemies
    for i in range(num_enemy):
        enemy = characters.Enemy()
        enemyGroup.add(enemy)

    # creating ledge if required
    if isLedge:
        ledge = characters.Ledge()
        ledgeGroup.add(ledge)

    # creating ledge enemies
    for j in range(num_ledge_enemies):
        ledge_enemy = characters.ledgeEnemy()
        enemyGroup.add(ledge_enemy)

    # configuring level
    level_bkgd = pygame.image.load(background)
    level_bkgd = pygame.transform.scale(level_bkgd, (2000, 1000))
    player.rect.x = 0
    while True:
        # running game logic
        logic(level_bkgd, True, level_num)

        # handling quit
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    play = False
            if event.type == pygame.QUIT:
                sys.exit()

        # Check if the character is done the level
        if (player.rect.x >= display_width) and (len(enemyGroup.sprites()) == 0):
            break
        elif (player.rect.x >= (display_width - player.size)) and (len(enemyGroup.sprites()) > 0):
            player.rect.x = display_width - player.size
        if not player.alive:
            playerGroup.empty()
            enemyGroup.empty()
            break

    # check if player died
    if not player.alive:
        player.health = 0
        death_time = pygame.time.get_ticks()

        # game over screen
        while True:
            keys = pygame.key.get_pressed()
            displayText("GAME OVER", '../fonts/Antonio-Bold.ttf', 200, display_width / 2, display_height / 4, black, 50)
            pygame.display.update()
            present_time = pygame.time.get_ticks()
            if present_time - death_time >= 4500:
                return False


# This function takes in no parameters nor does it reutrn parameters
# This function is responsible for displaying the merchant to the screen.
def display_merchant():
    gameDisplay.blit(merchant, (3*display_width / 5 + 400, characters.floor - 50))
    gameDisplay.blit(stand, (display_width / 3 + 400, characters.floor - 300))
    gameDisplay.blit(bubble, ((3*display_width / 5) + 300, characters.floor - 290))


# This function takes in no parameters nor does it return parameters
# This function is reponsible for displaying the level complete text
# to the game screen
def display_complete():
    displayText("LEVEL COMPLETE", '../fonts/Antonio-Bold.ttf', 125, display_width / 2, display_height / 4, black, 50)
    displayText("Next stage", '../fonts/Antonio-Bold.ttf', 30, display_width - 75, characters.floor - 70, black, 15)
    gameDisplay.blit(arrow, (display_width - 150, characters.floor - 60))


# This function takes in no parameters nor does it return parameters.
# It simply creates and draws the stat bar at the top of the screen.
def makeStatbar():
    pygame.draw.rect(gameDisplay, black, ((0, 0), (display_width, display_height / 15)))
    healthString = str("Health: " + str(player.health) + "/100")
    ammoString = str("Ammo: " + str(player.ammo) + "/300")
    displayText(healthString, '../fonts/Antonio-Regular.ttf', 30, 100, 30, white, 25)
    displayText(ammoString , '../fonts/Antonio-Regular.ttf', 30, 500, 30, white, 25)


# This function works hand in hand with the previous function and updates the
# stat bar during the level with the enemy count and level number
def levelStatbar(level_count):
    enemyString = str('Enemies remaining: ' + str(len(enemyGroup.sprites())))
    levelString = str('Level: ' + str(level_count))
    displayText(enemyString, '../fonts/Antonio-Regular.ttf', 30, 1850, 30, white, 20)
    displayText(levelString, '../fonts/Antonio-Regular.ttf', 40, display_width / 2, 30, white, 20)


# This function checks if the player is facing the correct
# direction when the user begins playing
def faceRight():
    if len(playerGroup.sprites()) == 0:
            playerGroup.add(player)
            if player.facing == "left":
                player.flipIt()
                player.facing = "right"

# This function takes in the parameters...
# state: the state of the merchant, whether it is the intro
#        screen or every other level
# This function is responsible for displaying merchant dialogue
# in the transition state.
def merchantDialogue(state):
    if state == "intro":
            displayText("This is where you can restock!", '../fonts/Antonio-Regular.ttf', 25, (3*display_width/5) + 500, characters.floor - 235, black, 10)
            displayText("Come back later to take", '../fonts/Antonio-Regular.ttf', 25, (3*display_width/5) + 500, characters.floor - 185, black, 10)
            displayText("a look at my merchandise.", '../fonts/Antonio-Regular.ttf', 25, (3*display_width/5) + 500, characters.floor - 135, black, 10)
    elif state == "normal":
            displayText("Take a step into my shop!", '../fonts/Antonio-Regular.ttf', 25, (3*display_width/5) + 500, characters.floor - 235, black, 10)
            displayText("You can only pick one...", '../fonts/Antonio-Regular.ttf', 25, (3*display_width/5) + 500, characters.floor - 185, black, 10)
            displayText("Jump to select.", '../fonts/Antonio-Regular.ttf', 25, (3*display_width/5) + 500, characters.floor - 135, black, 10)


# This function takes in the parameters...
# difficulty: the difficulty of the game selected by the user
# level_count: the current level the user is on
# enemies: the 3d list of the enemies, ledge enemies, and boss
# backgrounds: the list of backgrounds which change every level
# ledges: the list of bool values which indicate whether or not
#         to draw the ledge for the corresponding index level
# This function then returns the current 'state' of the level
def levelMaker(difficulty, level_count, enemies, backgrounds, ledges):
    temp_play = None
    if difficulty[0]:
        temp_play = level(enemies[0][0][level_count-1], level_count, backgrounds[level_count-1], ledges[level_count-1], enemies[0][1][level_count-1])
    elif difficulty[1]:
        temp_play = level(enemies[1][0][level_count-1], level_count, backgrounds[level_count-1], ledges[level_count-1], enemies[1][1][level_count-1])
    elif difficulty[2]:
        temp_play = level(enemies[2][0][level_count-1], level_count, backgrounds[level_count-1], ledges[level_count-1], enemies[2][1][level_count-1])
    return temp_play


# This function simply makes the sprites at the beginning of
# each level as they are all cleared at the end of each
# transtiion state
def makeSprites():
    if pickupGroup.sprites() == []:
        health_pickup = characters.pickUp(heart, display_width / 2 - 700, characters.floor - 200, "health", player)
        ammo_pickup = characters.pickUp(ammo_pic, display_width / 2 - 400, characters.floor - 200, "ammo", player)
        both_pickup = characters.pickUp(half_heart, display_width / 2 - 110, characters.floor - 170, "both", player)
        pickupGroup.add(health_pickup, ammo_pickup, both_pickup)


# This function simply checks if the player has chosen to
# pickup any of the pickups or not
def getCollision():
    sprite = pygame.sprite.spritecollideany(player, pickupGroup)
    if sprite != None and len(pickupGroup.sprites()) == 3:
        sprite.collide = True
        pickupGroup.update()
        pygame.sprite.groupcollide(pickupGroup, playerGroup, True, False)


# This functino draws and updates all the sprites to the screen.
def updateDraw():
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


# This functino is responsible for displaying the end game text after
# the user defeats the boss
def bossWin():
    pickupGroup.empty()
    gameDisplay.blit(background, (0, 0))
    displayText("YOU BEAT GRAND MASTER", '../fonts/Antonio-Bold.ttf', 150, display_width / 2, display_height / 4, black, 50)
    if player.rect.x >= display_width - characters.char_size:
        player.rect.x = display_width - characters.char_size

# Thsi functin is responsible for emptying the pickups, updating merchat
# dialogue, and displaying the 'YOU WON' text to the screen.
def youWon():
    pickupGroup.empty()
    player.health = 100
    if player.ammo < 50:
        player.ammo = 50
    gameDisplay.blit(bubble, ((3*display_width / 5) + 300, characters.floor - 290))
    displayText("YOU WON", '../fonts/Antonio-Bold.ttf', 150, display_width / 2, display_height / 4, black, 50)
    displayText("Wow, you killed them all!", '../fonts/Antonio-Regular.ttf', 25, (3*display_width/5) + 500, characters.floor - 235, black, 10)
    displayText("I have nothing left to sell...", '../fonts/Antonio-Regular.ttf', 25, (3*display_width/5) + 500, characters.floor - 185, black, 10)
    displayText("I am not worthy...", '../fonts/Antonio-Regular.ttf', 25, (3*display_width/5) + 500, characters.floor - 135, black, 10)