import pygame
white = (255, 255, 255)
green = (140, 240, 100)
red = (255, 0, 0)
display_width, display_height = 1500, 1000
gameDisplay = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()

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

def menuScreen():
    displayText("COMMAND-O-LINE", 'Antonio-Bold.ttf', 100, display_width / 2, display_height / 3, None, False, 0)
    displayText("Play game", 'Antonio-Regular.ttf', 50, display_width / 3, (2*display_height) / 3, green, True, 50)
    displayText("Quit game", 'Antonio-Regular.ttf', 50, (2*display_width) / 3, (2 * display_height) / 3, red, True, 50)
    pygame.display.update()
    clock.tick(60)
