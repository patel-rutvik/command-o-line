import pygame
from util import displayText, button
white = (255, 255, 255)
hovergreen = (140, 240, 100)
green = (140, 200, 100)
hoverred = (255, 0, 0)
red = (200, 0, 0)
blue = (0, 0, 200)
hoverblue = (0, 0, 255)
black = (0, 0, 0)
display_width, display_height = 1500, 1000
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width, display_height))

# https://www.1001freefonts.com/retro-fonts-4.php 


def menuScreen(state):
    gameDisplay.fill(black)
    displayText("COMMAND-O-LINE", 'Antonio-Bold.ttf', 115, display_width / 2, display_height / 3, white, 0)
    play_state = button("Play game", 'Antonio-Regular.ttf', 50, green, hovergreen, display_width / 3, (display_height) / 2, 50, "play")
    quit_state = button("Quit game", 'Antonio-Regular.ttf', 50, red, hoverred, display_width / 2, (2 * display_height) / 3, 50, "quit")
    tutorial_state = button("Tutorial", 'Antonio-Regular.ttf', 50, blue, hoverblue, (2*display_width) / 3, (display_height) / 2, 50, "tutorial")
    pygame.display.update()
    clock.tick(60)
    if play_state != state:
        return play_state
    elif quit_state != state:
        return quit_state
    elif tutorial_state != state:
        return tutorial_state
    #if state != button_state:
     #   return button_state

