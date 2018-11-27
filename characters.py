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

        #print(self.rect)

    def update(self):
        keys = pygame.key.get_pressed()
        #self.rect.x += 5
        if self.rect.x > display_width - 100:
            self.rect.x = display_width -  100
        if self.rect.y > 300:
            self.rect.y = 300
        #hold = False
        #while not hold:
        #for event in pygame.event.get():
         #   if event.type == pygame.KEYDOWN:
          #      if event.key == pygame.K_LEFT:
           #         Player.moveLeft(self)
            #    if event.key == pygame.K_RIGHT:
             #       rhold = True
              #      Player.moveRight(self)
               #     while rhold:
                #        if event.type == pygame.KEYUP:
                 #           if event.key == pygame.K_RIGHT:
                  #              rhold = False
                   #     Player.moveRight(self)
               # if event.key == pygame.K_UP:
                #    self.rect.y -= 100
               # if event.key == pygame.K_DOWN:
                #    self.rect.y += 100
        if keys[pygame.K_LEFT]:
            Player.moveLeft(self)
        if keys[pygame.K_RIGHT]:
            Player.moveRight(self)
        if keys[pygame.K_UP]:
            Player.jump(self)

        


    def moveRight(self):
        self.rect.x += 10


    def moveLeft(self):
        self.rect.x -= 10

    def jump(self):
        while (self.rect.y >= (300 - 60)):
            self.rect.y -= 5
        while (self.rect.y < 300):
            self.gravity()
        
    def gravity(self):
        self.rect.y += 5









