import pygame
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
display_width, display_height = 1500, 1000
gameDisplay = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()

# https://www.1001freefonts.com/retro-fonts-4.php 

def create_textobject(text, font):
    surface = font.render(text, True, white)
    return surface, surface.get_rect()

def displayText(text, fontsize, width, height, rect):
    if rect:
        text_width, text_height = textSize(text, fontsize)
        pygame.draw.rect(gameDisplay, green, ((display_width / 3) - (text_width / 2), ((2*display_height) / 3) - (text_height / 2), text_width, text_height))
    textobject = pygame.font.Font('Antonio-Bold.ttf', fontsize)
    textSurface, textRectangle = create_textobject(text, textobject)
    textRectangle.center = ((width), (height))
    gameDisplay.blit(textSurface, textRectangle)


def textSize(text, fontsize):
    textobject = pygame.font.Font('Antonio-Bold.ttf', fontsize)
    textWidth, textHeight = textobject.size(text)
    return textWidth, textHeight

def menuScreen():
    displayText("COMMAND-O-LINE", 100, display_width / 2, display_height / 3, False)
    displayText("Play game", 50, display_width / 3, (2*display_height) / 3, True)
    pygame.display.update()
    clock.tick(60)
