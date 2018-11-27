import pygame
from util import displayText, button

black = (0, 0, 0)
white = (255, 255, 255)
green = (100, 200, 100)
red = (200, 0, 0)
yellow = (180, 180, 0)
hoveryellow = (200, 200, 0)
display_width, display_height = 2000, 1000
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width, display_height))


def playGame():
    play = True

    while play:
        gameDisplay.fill(black)
        displayText("Kaden You Are Gay", 'Antonio-Bold.ttf', 75, display_width / 2, 100, white, 0)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    play = False
                    #return True
            if event.type == pygame.QUIT:
                play = False
                return True ### Quit does not work...
        pygame.display.update()