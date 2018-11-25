import pygame
display_width, display_height = 1500, 1000
gameDisplay = pygame.display.set_mode((display_width, display_height))
def create_textobject(text, font):
    surface = font.render(text, True, (255, 255, 255))
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
    state = ""
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
    if (state != ""):
        return state
