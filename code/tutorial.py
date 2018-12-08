import pygame
from util import displayText, button
import characters

# declaring our global variables
black = (0, 0, 0)
white = (255, 255, 255)
green = (100, 200, 100)
red = (200, 0, 0)
hoverred = (220, 0, 0)
yellow = (180, 180, 0)
hoveryellow = (200, 200, 0)
display_width, display_height = 2000, 1000

# initializing pygame modules
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width, display_height))

# creating sprite groups
all_sprites = pygame.sprite.Group()
player = characters.Player()
all_sprites.add(player)
tutorialGroup = pygame.sprite.Group()
tutorialPlayer = characters.tutorialGuy()
tutorialGroup.add(tutorialPlayer)
bulletGroup = pygame.sprite.Group()

# importing and rescaling images
background = pygame.image.load('../images/game_background.jpg')
background = pygame.transform.scale(background, (2000, 1000))
# arrow keys found from:
# https://www.google.ca/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwiW2srr2ozfAhWZ14MKHScGAB8Qj
# Rx6BAgBEAU&url=https%3A%2F%2Ffr.m.wikipedia.org%2Fwiki%2FFichier%3ACursor-key-arrangements-according-to
# -isoiec-9995-5.png&psig=AOvVaw2cPzXvj-MVtkDN-L8rudkL&ust=1544237414005703
left_key = pygame.image.load('../images/left_key.png')
left_key = pygame.transform.scale(left_key, (125, 125))
right_key = pygame.image.load('../images/right_key.png')
right_key = pygame.transform.scale(right_key, (125, 125))
up_key = pygame.image.load('../images/up_key.png')
up_key = pygame.transform.scale(up_key, (125, 125))

character = pygame.image.load('../images/main_guy.png')
character = pygame.transform.scale(character, (150,150))



def tutorialScreen():
    # The tutorial screen function takes in no parameters, nor does it return
    # anything. It is generally in charge of the visuals and establishing a
    # moveable character to allow the user to become familiar with the controls
    # of the game.
    tutorial = True
    while tutorial:
        # displaying baackground and characters
        gameDisplay.blit(background, (0, 0))
        gameDisplay.blit(character, ((display_width / 2) + 185, 180))
        if tutorialPlayer.shot == True:
            bullet = characters.Bullet(tutorialPlayer.rect.x, tutorialPlayer.rect.y, tutorialPlayer.facing, tutorialPlayer.location)
            bulletGroup.add(bullet)
            tutorialPlayer.canShoot = False
        updateDraw()
        tutorialText()
        tempState = button("Main Menu (m)", '../fonts/Antonio-Regular.ttf', 40, white, red, hoverred, 1875, 970, 25, False)
        if tempState != None:
            tutorial = tempState
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    tutorial = False
            if event.type == pygame.QUIT:
                return True ### Quit does not work...
        pygame.display.update()
        clock.tick(60)


def updateDraw():
    # This function does not take in or return any parameters.
    # It is simply in charge of updating and drawing sprites.
    tutorialGroup.update()
    bulletGroup.update()
    bulletGroup.draw(gameDisplay)
    tutorialGroup.draw(gameDisplay)


def tutorialText():
    # This function does not take in or return any parameters.
    # It is simply in charge of updating the screen and draw the
    # text needed to convey the tutorial instructions.
    displayText("Tutorial", '../fonts/Antonio-Bold.ttf', 125, display_width / 2, 100, white, 0)
    displayText("You will be controlling             ", '../fonts/Antonio-Regular.ttf', 65, (display_width / 2), 275, white, 0)
    displayText("Roberto", '../fonts/Antonio-Bold.ttf', 30, (display_width / 2) + 250, 350, white, 0)
    displayText("Press       on the keypad to move right", '../fonts/Antonio-Regular.ttf', 50, (display_width / 3), 475, white, 0)
    displayText("Press       on the keypad to move left", '../fonts/Antonio-Regular.ttf', 50, (display_width / 3), 575, white, 0)
    displayText("Press       on the keypad to jump", '../fonts/Antonio-Regular.ttf', 50, (display_width / 3), 675, white, 0)
    displayText("Use the mouse to aim and shoot!", '../fonts/Antonio-Regular.ttf', 50, (display_width / 3), 775, white, 0)
    gameDisplay.blit(right_key, ((display_width / 3) - 310, 385))
    gameDisplay.blit(left_key, ((display_width / 3) - 215, 480))
    gameDisplay.blit(up_key, ((display_width / 3) - 225, 635))