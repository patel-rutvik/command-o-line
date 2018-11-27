import pygame
import time
display_width, display_height = 2000, 1000


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("char-pikachu.png")
        self.image = pygame.transform.scale(self.image, (200,200))
        self.rect = self.image.get_rect()
        self.rect.y = 600
        #print(self.rect)


    def update(self):
        keys = pygame.key.get_pressed()
        #self.rect.x += 5
        if self.rect.x > display_width:
            self.rect.x = display_width-100
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    Player.moveLeft(self)
                if event.key == pygame.K_RIGHT:
                    Player.moveRight(self)
                if event.key == pygame.K_UP:
                    self.rect.y -= 200


    def moveRight(self):
        self.rect.x += 25


    def moveLeft(self):
        self.rect.x -= 25