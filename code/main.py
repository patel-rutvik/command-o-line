import pygame
import sys
from menu_screen import menuScreen
from tutorial import tutorialScreen
from play_game import playGame

# Fonts are downloaded from:
# https://www.1001freefonts.com/retro-fonts-4.php

# setting up pygame
pygame.init()

# initializing display and clock
pygame.display.set_caption("Command-O-Line")
clock = pygame.time.Clock()
quit = False

# main game loop
def game_loop(quit):
    while not quit:
        # handling quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # We can add an "Are you sure you would like to quit" window later... 
                quit = True
        # default run state is the menu screen
        gameState = menuScreen(None)

        if gameState == "quit":
            quit = True
        elif gameState == "tutorial":
            # running tutorial screen
            quit = tutorialScreen()
        elif gameState == "play":
            # running play game
            quit = playGame()
        # updating display and establishing FPS
        pygame.display.update()
        clock.tick(60)

# calling game loop
game_loop(quit)
# quitting appropriately when done playing
pygame.quit()
sys.exit()
