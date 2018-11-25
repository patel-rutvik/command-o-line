import pygame
from util import displayText, button

black = (0, 0, 0)
white = (255, 255, 255)
green = (100, 200, 100)
red = (200, 0, 0)
display_width, display_height = 1500, 1000
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width, display_height))
#def importSprite():

def tutorialScreen():
    tutorial = True

    while tutorial:
        gameDisplay.fill(black)
        displayText("Tutorial", 'Antonio-Bold.ttf', 75, display_width / 2, 100, white, 0)
        displayText("You will be controlling _______.", 'Antonio-Regular.ttf', 30, display_width / 2, 200, white, 0)
        displayText("Press RIGHT on the keypad to move right. Press LEFT on the keypad to move left.", 'Antonio-Regular.ttf',
                     25, display_width / 2, 300, white, 0)
        displayText("Press UP on the keypad to JUMP.", 'Antonio-Regular.ttf', 25, display_width / 2, 340, white, 0)
        displayText("Press the SPACE BAR to shoot straight in front of you'", 'Antonio-Regular.ttf', 25, display_width / 2, 380, white, 0)
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    tutorial = False
                if event.type == pygame.QUIT:
                    return True ### Quit does not work...
                    break
        pygame.display.update()
        clock.tick(60)

