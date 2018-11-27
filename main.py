import pygame
import sys
from menu_screen import menuScreen
from tutorial import tutorialScreen
from play_game import playGame
# https://pythonprogramming.net/pygame-python-3-part-1-intro/

# setting up pygame
pygame.init()

pygame.display.set_caption("Command-o-Line")
clock = pygame.time.Clock()
quit = False

def game_loop(quit):
    while not quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # We can add an "Are you sure you would like to quit" window later... 
                quit = True
        gameState = menuScreen(None)
        print("State of game: ", gameState, '\n')
        if gameState == "quit":
            quit = True
        elif gameState == "tutorial":
            quit = tutorialScreen()
        elif gameState == "play":
            quit = playGame()
        pygame.display.update()
        clock.tick(60)

game_loop(quit)

pygame.quit()
sys.exit()
