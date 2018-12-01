import pygame
from util import displayText, button
import characters

black = (0, 0, 0)
white = (255, 255, 255)
green = (100, 200, 100)
red = (200, 0, 0)
hoverred = (220, 0, 0)
yellow = (180, 180, 0)
hoveryellow = (200, 200, 0)
display_width, display_height = 2000, 1000
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width, display_height))

all_sprites = pygame.sprite.Group()
player = characters.Player()
all_sprites.add(player)

background = pygame.image.load('images/game_background.jpg')
background = pygame.transform.scale(background, (2000, 1000))
left_key = pygame.image.load('images/left_key.png')
left_key = pygame.transform.scale(left_key, (125, 125))
right_key = pygame.image.load('images/right_key.png')
right_key = pygame.transform.scale(right_key, (125, 125))
up_key = pygame.image.load('images/up_key.png')
up_key = pygame.transform.scale(up_key, (125, 125))
character = pygame.image.load('images/main_guy.png')
character = pygame.transform.scale(character, (150,150))

tutorialGroup = pygame.sprite.Group()
tutorialPlayer = characters.tutorialGuy()
tutorialGroup.add(tutorialPlayer)

def tutorialScreen():
    tutorial = True
    while tutorial:
        gameDisplay.blit(background, (0, 0))
        gameDisplay.blit(character, ((display_width / 2) + 185, 180))
        tutorialGroup.update()
        tutorialGroup.draw(gameDisplay)
        displayText("Tutorial", 'fonts/Antonio-Bold.ttf', 125, display_width / 2, 100, white, 0)
        displayText("You will be controlling             ", 'fonts/Antonio-Regular.ttf', 65, (display_width / 2), 275, white, 0)
        displayText("Roberto", 'fonts/Antonio-Bold.ttf', 30, (display_width / 2) + 250, 350, white, 0)
        displayText("Press       on the keypad to move right", 'fonts/Antonio-Regular.ttf', 50, (display_width / 3), 475, white, 0)
        displayText("Press       on the keypad to move left", 'fonts/Antonio-Regular.ttf', 50, (display_width / 3), 575, white, 0)
        displayText("Press       on the keypad to jump", 'fonts/Antonio-Regular.ttf', 50, (display_width / 3), 675, white, 0)
        displayText("Use the mouse to aim and shoot!", 'fonts/Antonio-Regular.ttf', 50, (display_width / 3), 775, white, 0)
        tempState = button("Main Menu (m)", 'fonts/Antonio-Regular.ttf', 40, white, red, hoverred, 1875, 970, 25, False)
        if tempState != None:
            tutorial = tempState
        gameDisplay.blit(right_key, ((display_width / 3) - 310, 385))
        gameDisplay.blit(left_key, ((display_width / 3) - 215, 480))
        gameDisplay.blit(up_key, ((display_width / 3) - 225, 635))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    tutorial = False
            if event.type == pygame.QUIT:
                return True ### Quit does not work...
        pygame.display.update()
        clock.tick(60)

