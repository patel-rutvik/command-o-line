import pygame
from util import displayText, button
white = (255, 255, 255)
hovergreen = (140, 240, 100)
green = (140, 200, 100)
hoverred = (255, 0, 0)
red = (200, 0, 0)
blue = (0, 0, 200)
hoverblue = (0, 0, 255)
display_width, display_height = 1500, 1000
clock = pygame.time.Clock()

# https://www.1001freefonts.com/retro-fonts-4.php 


def menuScreen():
    gameState = "menu"
    displayText("COMMAND-O-LINE", 'Antonio-Bold.ttf', 115, display_width / 2, display_height / 3, white, 0)
    gameState = button("Play game", 'Antonio-Regular.ttf', 50, green, hovergreen, display_width / 3, (display_height) / 2, 50, "play")
    gameState = button("How to play", 'Antonio-Regular.ttf', 50, blue, hoverblue, (2*display_width) / 3, (display_height) / 2, 50, "tutorial")
    gameState = button("Quit game", 'Antonio-Regular.ttf', 50, red, hoverred, display_width / 2, (2 * display_height) / 3, 50, "quit")
    pygame.display.update()
    clock.tick(60)
    return gameState

