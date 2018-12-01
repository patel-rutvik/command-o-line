import pygame
from util import displayText, button
import characters
white = (255, 255, 255)
hovergreen = (140, 240, 100)
green = (140, 200, 100)
hoverred = (255, 0, 0)
red = (200, 0, 0)
blue = (0, 0, 200)
hoverblue = (0, 0, 255)
black = (0, 0, 0)
display_width, display_height = 2000, 1000
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width, display_height))
background = pygame.image.load('images/game_background.jpg')
background = pygame.transform.scale(background, (2000, 1000))
button_size = int((display_width / display_height) * 25)
# https://www.1001freefonts.com/retro-fonts-4.php 

bad_guys = 3
menuGroup = pygame.sprite.Group()
menu_mainPlayer = characters.menugoodGuy()
menuGroup.add(menu_mainPlayer)
for i in range(bad_guys):
    menu_badPlayer = characters.menubadGuy()
    menuGroup.add(menu_badPlayer)


def menuScreen(state):
    gameDisplay.blit(background, (0, 0))
    displayText("COMMAND-O-LINE", 'fonts/Antonio-Bold.ttf', 200, display_width / 2, (display_height / 5),
                 white, 0)
    play_state = button("Play game", 'fonts/Antonio-Regular.ttf', button_size, white, green, 
                        hovergreen, display_width / 5, display_height - button_size, 50, "play")
    tutorial_state = button("Tutorial", 'fonts/Antonio-Regular.ttf', button_size, white, blue,
                             hoverblue, display_width / 2, display_height - button_size, 50, 
                             "tutorial")
    quit_state = button("Quit game", 'fonts/Antonio-Regular.ttf', button_size, white, red, hoverred,
                        (4*display_width) / 5, display_height - button_size, 50, "quit")
                    
    menuGroup.update()
    menuGroup.draw(gameDisplay)
    if play_state != state:
        return play_state
    elif quit_state != state:
        return quit_state
    elif tutorial_state != state:
        return tutorial_state
    #if state != button_state:
     #   return button_state

