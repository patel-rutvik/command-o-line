import pygame
import time
display_width, display_height = 1000, 500


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("char-pikachu.png")
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()
        self.rect.y = 300
        self.jumped = False

    def update(self):
        keys = pygame.key.get_pressed()
        if self.rect.x > display_width - 100:
            self.rect.x = display_width -  100
        if self.rect.y >= 300:
            self.rect.y = 300
            self.jumped = False
        if keys[pygame.K_LEFT]:
            Player.moveLeft(self)
        if keys[pygame.K_RIGHT]:
            Player.moveRight(self)
        if keys[pygame.K_UP] and self.jumped == False:
            Player.jump(self)
            if self.rect.y <= (300 - 150):
                self.jumped = True
        if (keys[pygame.K_UP] == False) or self.jumped == True:
            Player.gravity(self)
            


    def moveRight(self):
        self.rect.x += 4


    def moveLeft(self):
        self.rect.x -= 4

    def jump(self):
        self.rect.y -= 5
        
    def gravity(self):
        self.rect.y += 5









