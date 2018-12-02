import pygame
import time
import math
import random
ORANGE = (255, 165, 0)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
display_width, display_height = 2000, 1000
char_size = int(display_width / 10)
floor = int(display_height - (2 * char_size))
ceiling = int((4*floor) / 9) 
gameDisplay = pygame.display.set_mode((display_width, display_height))

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/main_guy.png")
        self.image = pygame.transform.scale(self.image, (char_size, char_size))
        self.rect = self.image.get_rect()
        self.size = char_size
        self.rect.y = floor
        self.facing = "right"
        self.shot = False
        self.canShoot = True
        self.health = 100
        self.ammo = 100

    def update(self):
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.y >= floor:
            self.rect.y = floor
            self.jumped = False
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.facing == "right":
                Player.flipIt(self)
                self.facing = "left"
            Player.moveLeft(self)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.facing == "left":
                Player.flipIt(self)
                self.facing = "right"
            Player.moveRight(self)
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.jumped == False:
            Player.jump(self)
            if self.rect.y <= (floor - ceiling):
                self.jumped = True
        if ((keys[pygame.K_UP] == False and not keys[pygame.K_w]) and self.rect.y < floor):
            self.jumped = True
        if self.jumped == True:
            Player.gravity(self)

        if click[0] and self.canShoot == True and self.ammo > 0:
            self.location = mouse
            self.shot = True
        if self.canShoot == False:
            self.shot = False
        if click[0] == False:
            self.canShoot = True

    def flipIt(self):
        self.image = pygame.transform.flip(self.image, True, False)


    def moveRight(self):
        self.rect.x += (display_width / 100)


    def moveLeft(self):
        self.rect.x -= (display_width / 100) 

    def jump(self):
        self.rect.y -= (display_height / 100) * 4
        
    def gravity(self):
        self.rect.y += (display_height / 100) * 4




class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/bad_guy.png")
        self.image = pygame.transform.scale(self.image, (char_size, char_size))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.y = floor
        self.rect.x = random.randint(1200, display_width + (4*char_size))
        self.health = 100
        self.alive = True

    def update(self):
        self.rect.x -= 9
        if self.rect.x == 0 - char_size:
            self.rect.x = display_width
        if self.health <= 0:
            self.alive = False
        Enemy.healthBar(self)


    def healthBar(self):
        tempInt = char_size / 100
        pygame.draw.rect(gameDisplay, RED, ((self.rect.x, self.rect.y - 10, char_size, 15)))
        pygame.draw.rect(gameDisplay, GREEN, ((self.rect.x, self.rect.y - 10, (char_size - tempInt*(100 - self.health)) , 15)))

class Bullet(pygame.sprite.Sprite):

    def __init__(self, player_x, player_y, facing, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((2,2))
        self.image = pygame.transform.scale(self.image, (int(char_size/20), int(char_size/20)))
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
        self.location = location
        self.originX = self.rect.x
        self.originY = self.rect.y
        self.speed = 45

    def update(self):
        Xspeed, Yspeed = Bullet.calc(self)
        if self.originX < self.location[0] and self.originY > self.location[1]:
            self.rect.x += Xspeed
            self.rect.y += Yspeed
        elif self.originX > self.location[0] and self.originY > self.location[1]:
            self.rect.x -= Xspeed
            self.rect.y -= Yspeed
        elif self.originX > self.location[0] and self.originY < self.location[1]:
            self.rect.x -= Xspeed
            self.rect.y -= Yspeed
        else:
            self.rect.x += Xspeed
            self.rect.y += Yspeed

        if self.rect.x > display_width or self.rect.x < 0 or self.rect.y < 0 or self.rect.y > display_height:
            self.alive = False

    def calc(self):
        deltaX = self.location[0] - self.originX + 0.0001
        deltaY = self.location[1] - self.originY
        theta = math.atan(deltaY/deltaX)
        Xspeed = self.speed * math.cos(theta)
        Yspeed = self.speed * math.sin(theta)
        return Xspeed, Yspeed

class menugoodGuy(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/main_guy.png")
        self.image = pygame.transform.scale(self.image, (char_size, char_size))
        self.rect = self.image.get_rect()
        self.rect.y = floor
        self.rect.x = 0

    def update(self):
        self.rect.x += 7
        if self.rect.x > display_width:
            self.rect.x = 0 - char_size


class menubadGuy(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/bad_guy.png")
        self.image = pygame.transform.scale(self.image, (char_size, char_size))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.y = floor
        self.rect.x = random.randint(0, display_width)

    def update(self):
        self.rect.x -= random.randint(0, 25)
        if self.rect.x < 0 - char_size:
            self.rect.x = display_width + char_size

class tutorialGuy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/main_guy.png")
        self.image = pygame.transform.scale(self.image, (char_size, char_size))
        self.rect = self.image.get_rect()
        self.rect.y = floor
        self.facing = "right"
        self.shot = False
        self.canShoot = True
        self.rect.x = 1200

    def update(self):
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.rect.x <= 1200 - char_size:
            self.rect.x = display_width + char_size
        if self.rect.x >= display_width + char_size:
            self.rect.x = 1200 - char_size
        if self.rect.y >= floor:
            self.rect.y = floor
            self.jumped = False
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.facing == "right":
                Player.flipIt(self)
                self.facing = "left"
            Player.moveLeft(self)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.facing == "left":
                Player.flipIt(self)
                self.facing = "right"
            Player.moveRight(self)
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.jumped == False:
            Player.jump(self)
            if self.rect.y <= (floor - ceiling):
                self.jumped = True
        if ((keys[pygame.K_UP] == False and not keys[pygame.K_w]) and self.rect.y < floor):
            self.jumped = True
        if self.jumped == True:
            Player.gravity(self)

        if click[0] and self.canShoot == True:
            self.location = mouse
            self.shot = True
        if self.canShoot == False:
            self.shot = False
        if click[0] == False:
            self.canShoot = True

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
        
class ledgeEnemy(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/bad_guy.png")
        self.image = pygame.transform.scale(self.image, (char_size, char_size))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.y = floor - 500
        self.rect.x = random.randint(1500 - char_size, display_width + (4*char_size))
        self.health = 100
        self.alive = True
        self.ledge_reached = False

    def update(self):
        if self.ledge_reached == False:
            self.rect.x -= 9
        if self.rect.x <= 1500:
            self.ledge_reached = True
            self.rect.x = 1500
        if self.health <= 0:
            self.alive = False
        ledgeEnemy.healthBar(self)

    def healthBar(self):
        tempInt = char_size / 100
        pygame.draw.rect(gameDisplay, RED, ((self.rect.x, self.rect.y - 10, char_size, 15)))
        pygame.draw.rect(gameDisplay, GREEN, ((self.rect.x, self.rect.y - 10, (char_size - tempInt*(100 - self.health)) , 15)))

class Ledge(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((2,2))
        self.image = pygame.transform.scale(self.image, (500, 50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.y = floor - 300
        self.rect.x = display_width - 500


    
