import pygame

# establishing global variables
display_width, display_height = 2000, 1000
gameDisplay = pygame.display.set_mode((display_width, display_height))


# This function takes in the following...
# text: text to be displayed
# font: font selected to configure the text
# color: color of the text on screen
# This function then creates and renders the text
# surface and that is what is returned.
def create_textobject(text, font, color):
    surface = font.render(text, True, (color))
    return surface, surface.get_rect()


# This function takes in the following...
# text: text to be displayed
# font_type: font chosen
# fontsize: size of the text
# x: x coordinate of the text object
# y: y coordinate of the text object
# color: color of the text chosen
# buff: number of pixels to 'buffer' the text rect created
# The function does not return anything, but its sole purpose
# is to display text to the screen.
def displayText(text, font_type, fontsize, x, y, color, buff):
    text_width, text_height, textobject = textSize(text, font_type, fontsize)
    textSurface, textRectangle = create_textobject(text, textobject, color)
    textRectangle.center = (x, y)
    gameDisplay.blit(textSurface, textRectangle)


# This function takes in the following... 
# text: text to be displayed
# font_type: font chosen
# fontsize: size of the text
# The function then calculates and returns the text width, height, and
# creates the text object
def textSize(text, font_type, fontsize):
    textobject = pygame.font.Font(font_type, fontsize)
    textWidth, textHeight = textobject.size(text)
    return textWidth, textHeight, textobject


# This function takes in the following...
# text: text to be displayed
# font_type: font chosen
# fontsize: size of the text
# fontcolor: color of the text
# x: x coordinate of the text object
# y: y coordinate of the text object
# color: color of the button chosen
# hover_color: color of the button when hovering over it
# buff: number of pixels to 'buffer' the text rect created
# clause: the clause to be changed when the button is pressed
# This function creates and displays a button on the screen which is then used
# to change the status of the finite state machine.
def button(text, font_type, fontsize, fontcolor, color, hover_color, x, y, buff, clause):
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
    textSurface, textRectangle = create_textobject(text, textobject, fontcolor)
    textRectangle.center = (x, y)
    gameDisplay.blit(textSurface, textRectangle)
    if (state != ""):
        return state

