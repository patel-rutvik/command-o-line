import pygame
white = (255, 255, 255)
hovergreen = (140, 240, 100)
green = (140, 200, 100)
hoverred = (255, 0, 0)
red = (200, 0, 0)
blue = (0, 0, 200)
hoverblue = (0, 0, 255)
display_width, display_height = 1500, 1000
gameDisplay = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
#mouse = pygame.mouse.get_pos()
# https://www.1001freefonts.com/retro-fonts-4.php 

def create_textobject(text, font):
    surface = font.render(text, True, white)
    return surface, surface.get_rect()

def displayText(text, font_type, fontsize, x, y, color, buff):
    text_width, text_height, textobject = textSize(text, font_type, fontsize)
    textSurface, textRectangle = create_textobject(text, textobject)
    textRectangle.center = (x, y)
    gameDisplay.blit(textSurface, textRectangle)


def textSize(text, font_type, fontsize):
    textobject = pygame.font.Font(font_type, fontsize)
    textWidth, textHeight = textobject.size(text)
    return textWidth, textHeight, textobject

def button(text, font_type, fontsize, color, hover_color, x, y, buff, clause):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    text_width, text_height, textobject = textSize(text, font_type, fontsize)
    state = "menu"
    if (x + (0.5 * text_width) + (0.5 * buff) > mouse[0] > x - (0.5 * text_width) - (0.5 * buff)) and (y + (0.5 * text_height) > mouse[1] > y - (0.5 * text_height)):
        pygame.draw.rect(gameDisplay, hover_color, ((x) - (text_width / 2) - (buff / 2), 
                        (y) - (text_height / 2), text_width + buff, text_height))
        if click[0] == 1:
            state = clause
    else:
        pygame.draw.rect(gameDisplay, color, ((x) - (text_width / 2) - (buff / 2), 
                        (y) - (text_height / 2), text_width + buff, text_height))
    textSurface, textRectangle = create_textobject(text, textobject)
    textRectangle.center = (x, y)
    gameDisplay.blit(textSurface, textRectangle)
    return state
    

def menuScreen():
    #play = False
    #tutorial = False
    #quitgame = False
    gameState = "menu"
    displayText("COMMAND-O-LINE", 'Antonio-Bold.ttf', 115, display_width / 2, display_height / 3, white, 0)
    gameState = button("Play game", 'Antonio-Regular.ttf', 50, green, hovergreen, display_width / 3, (display_height) / 2, 50, "play")
    gameState = button("How to play", 'Antonio-Regular.ttf', 50, blue, hoverblue, (2*display_width) / 3, (display_height) / 2, 50, "tutorial")
    gameState = button("Quit game", 'Antonio-Regular.ttf', 50, red, hoverred, display_width / 2, (2 * display_height) / 3, 50, "quit")
    pygame.display.update()
    clock.tick(60)
    return gameState

