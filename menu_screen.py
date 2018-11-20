import pygame
white = (255, 255, 255)
display_width, display_height = 1500, 1000
gameDisplay = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()

def create_textobject(text, font):
    surface = font.render(text, True, white)
    return surface, surface.get_rect()

def displayText(text, fontsize, width, height):
    textobject = pygame.font.Font('Antonio-Bold.ttf', fontsize)
    textSurface, textRectangle = create_textobject(text, textobject)
    textRectangle.center = ((width), (height))
    gameDisplay.blit(textSurface, textRectangle)

def menuScreen():
    displayText("COMMAND-O-LINE", 100, display_width / 2, display_height / 3)
    displayText("Play game", 50, display_width / 2, (2*display_height) / 3)
    pygame.display.update()
    clock.tick(60)
    