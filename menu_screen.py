import pygame
white = (255, 255, 255)
hovergreen = (140, 240, 100)
green = (140, 200, 100)
hoverred = (255, 0, 0)
red = (200, 0, 0)
display_width, display_height = 1500, 1000
gameDisplay = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
#mouse = pygame.mouse.get_pos()
# https://www.1001freefonts.com/retro-fonts-4.php 

def create_textobject(text, font):
    surface = font.render(text, True, white)
    return surface, surface.get_rect()

def displayText(text, font_type, fontsize, x, y, color, rect, buff):
    text_width, text_height, textobject = textSize(text, font_type, fontsize)
    if rect:
        pygame.draw.rect(gameDisplay, color, ((x) - (text_width / 2) - (buff / 2), 
                        (y) - (text_height / 2), text_width + buff, text_height))
    textSurface, textRectangle = create_textobject(text, textobject)
    textRectangle.center = (x, y)
    gameDisplay.blit(textSurface, textRectangle)


def textSize(text, font_type, fontsize):
    textobject = pygame.font.Font(font_type, fontsize)
    textWidth, textHeight = textobject.size(text)
    return textWidth, textHeight, textobject

def button(text, font_type, fontsize, color, hover_color, x, y, buff):
    mouse = pygame.mouse.get_pos()
    text_width, text_height, textobject = textSize(text, font_type, fontsize)
    if (x + (0.5 * text_width) + (0.5 * buff) > mouse[0] > x - (0.5 * text_width) - (0.5 * buff)) and (y + (0.5 * text_height) > mouse[1] > y - (0.5 * text_height)):
        pygame.draw.rect(gameDisplay, hover_color, ((x) - (text_width / 2) - (buff / 2), 
                        (y) - (text_height / 2), text_width + buff, text_height))
    else:
        pygame.draw.rect(gameDisplay, color, ((x) - (text_width / 2) - (buff / 2), 
                        (y) - (text_height / 2), text_width + buff, text_height))
    textSurface, textRectangle = create_textobject(text, textobject)
    textRectangle.center = (x, y)
    gameDisplay.blit(textSurface, textRectangle)
    

def menuScreen():
    displayText("COMMAND-O-LINE", 'Antonio-Bold.ttf', 100, display_width / 2, display_height / 3, white, False, 0)
    button("Play game", 'Antonio-Regular.ttf', 50, green, hovergreen, display_width / 3, (2*display_height) / 3, 50)
    #displayText("Play game", 'Antonio-Regular.ttf', 50, display_width / 3, (2*display_height) / 3, green, True, 50)
    #displayText("Quit game", 'Antonio-Regular.ttf', 50, (2*display_width) / 3, (2 * display_height) / 3, red, True, 50)
    button("Quit game", 'Antonio-Regular.ttf', 50, red, hoverred, (2*display_width) / 3, (2 * display_height) / 3, 50)
    pygame.display.update()
    clock.tick(60)


