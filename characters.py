import pygame
import time
ORANGE = (255, 165, 0)
display_width, display_height = 2000, 1000
char_size = int(display_width / 10)
floor = int(display_height - (2 * char_size))
ceiling = int((2*floor) / 5) 

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("main_guy.png")
        self.image = pygame.transform.scale(self.image, (char_size, char_size))
        self.rect = self.image.get_rect()
        self.rect.y = floor
        self.facing = "right"
        self.shot = False

    def update(self):
        keys = pygame.key.get_pressed()
        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.y >= floor:
            self.rect.y = floor
            self.jumped = False
        if keys[pygame.K_LEFT]:
            if self.facing == "right":
                Player.flipIt(self)
                self.facing = "left"
            Player.moveLeft(self)
        if keys[pygame.K_RIGHT]:
            if self.facing == "left":
                Player.flipIt(self)
                self.facing = "right"
            Player.moveRight(self)
        if keys[pygame.K_UP] and self.jumped == False:
            Player.jump(self)
            if self.rect.y <= (floor - ceiling):
                self.jumped = True
        if (keys[pygame.K_UP] == False and self.rect.y < floor):
            self.jumped = True
        if self.jumped == True:
            Player.gravity(self)

        if keys[pygame.K_SPACE] and self.shot == False:
            self.shot = True
        if keys[pygame.K_SPACE] == False:
            self.shot = False


    def flipIt(self):
        self.image = pygame.transform.flip(self.image, True, False)


    def moveRight(self):
        self.rect.x += (display_width / 100)


    def moveLeft(self):
        self.rect.x -= (display_width / 100) 

    def jump(self):
        self.rect.y -= (display_height / 100) * 3
        
    def gravity(self):
        self.rect.y += (display_height / 100) * 3




class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("bad_guy.png")
        self.image = pygame.transform.scale(self.image, (char_size, char_size))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.y = floor
        self.rect.x = display_width - char_size
        self.health = 100
        self.alive = True

    def update(self):
        self.rect.x -= 9
        if self.rect.x == 0 - char_size:
            self.rect.x = display_width
        if self.health <= 0:
            self.alive = False

class Bullet(pygame.sprite.Sprite):

    def __init__(self, player_x, player_y, facing):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((2,2))
        self.image = pygame.transform.scale(self.image, (int(char_size/10), int(char_size/20)))
        self.image.fill(ORANGE)
        self.rect = self.image.get_rect()
        self.rect.y = player_y + (char_size/3)
        if facing == "right":
            self.rect.x = player_x + (8*char_size/9)
        if facing == "left":
            self.rect.x = player_x
        self.facing = facing
        self.damage = 10
        self.alive = True

    def update(self):
        if self.facing == "right":
            self.rect.x += 30
        else:
            self.rect.x -= 30
        if self.rect.x > display_width or self.rect.x < 0:
            self.alive = False

