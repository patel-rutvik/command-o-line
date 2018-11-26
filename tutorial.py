import pygame
from util import displayText, button

black = (0, 0, 0)
white = (255, 255, 255)
green = (100, 200, 100)
red = (200, 0, 0)
yellow = (180, 180, 0)
hoveryellow = (200, 200, 0)
display_width, display_height = 1500, 1000
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width, display_height))
left_key = pygame.image.load('left_key.png')
right_key = pygame.image.load('right_key.png')
right_key = pygame.transform.scale(right_key, (100,100))
up_key = pygame.image.load('up_key.png')
up_key = pygame.transform.scale(up_key, (50,50))


def tutorialScreen():
    tutorial = True

    while tutorial:
        gameDisplay.fill(black)
        displayText("Tutorial", 'Antonio-Bold.ttf', 75, display_width / 2, 100, white, 0)
        displayText("You will be controlling Pikachu.", 'Antonio-Regular.ttf', 30, display_width / 2, 200, white, 0)
        displayText("Press        on the keypad to move right. Press LEFT on the keypad to move left.", 'Antonio-Regular.ttf',
                     25, display_width / 2, 300, white, 0)
        displayText("Press UP on the keypad to JUMP.", 'Antonio-Regular.ttf', 25, display_width / 2, 340, white, 0)
        displayText("Press the SPACE BAR to shoot straight in front of you", 'Antonio-Regular.ttf', 25, display_width / 2, 380, white, 0)
        tempState = button("Main Menu (ENTER)", 'Antonio-Regular.ttf', 40, yellow, hoveryellow, 1350, 960, 25, False)
        if tempState != None:
            tutorial = tempState
        gameDisplay.blit(right_key, (385,225))
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    tutorial = False
                if event.type == pygame.QUIT:
                    return True ### Quit does not work...
        pygame.display.update()
        clock.tick(60)

