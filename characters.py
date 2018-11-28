import pygame
import time
display_width, display_height = 2000, 1000
char_size = int(display_width / 10)
floor = int(display_height - (2 * char_size))
ceiling = int((2*floor) / 5) 

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("char-pikachu.png")
        self.image = pygame.transform.scale(self.image, (char_size, char_size))
        self.rect = self.image.get_rect()
        self.rect.y = floor

    def update(self):
        keys = pygame.key.get_pressed()
        if self.rect.x > display_width - char_size:
            self.rect.x = display_width -  char_size
        if self.rect.y >= floor:
            self.rect.y = floor
            self.jumped = False
        if keys[pygame.K_LEFT]:
            Player.moveLeft(self)
        if keys[pygame.K_RIGHT]:
            Player.moveRight(self)
        if keys[pygame.K_UP] and self.jumped == False:
            Player.jump(self)
            if self.rect.y <= (floor - ceiling):
                self.jumped = True
        if (keys[pygame.K_UP] == False and self.rect.y < floor):
            self.jumped = True
        if self.jumped == True:
            Player.gravity(self)

    def moveRight(self):
        self.rect.x += (display_width / 200)


    def moveLeft(self):
        self.rect.x -= (display_width / 200)

    def jump(self):
        self.rect.y -= (display_height / 100) * 3
        
    def gravity(self):
        self.rect.y += (display_height / 100) * 3



class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("goomba.png")
        self.image = pygame.transform.scale(self.image, (char_size, char_size))
        self.rect = self.image.get_rect()
        self.rect.y = floor
        self.rect.x = display_width - char_size

    def update(self):
        self.rect.x -= 10
        if self.rect.x == 0 - char_size:
            self.rect.x = display_width