import pygame
import time
import math
import random
from util import displayText

# Creating all global vairables
ORANGE = (255, 165, 0)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
PURPLE = (200, 0, 200)
display_width, display_height = 2000, 1000
char_size = int(display_width / 10)
floor = int(display_height - (2 * char_size))
ceiling = int((5*floor) / 9) 
gameDisplay = pygame.display.set_mode((display_width, display_height))

small_ammo = pygame.image.load('../images/ammo_crate.png')
small_ammo = pygame.transform.scale(small_ammo, (50, 50))


# The player class is an object for the main playable character
class Player(pygame.sprite.Sprite):

    # Initializing the sprite with the following components
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # This gets the image for the object
        self.image = pygame.image.load("../images/main_guy.png")
        # This scales the object to the size we want
        self.image = pygame.transform.scale(self.image, (char_size, char_size))
        # This gets the x and y components of the sprite
        self.rect = self.image.get_rect()
        # This sets the size of the character
        self.size = char_size
        # This initializes the player on the floor
        self.rect.y = floor
        # This sets the player facing to the right
        self.facing = "right"
        # This shows that the player has not shot yet
        self.shot = False
        # The sprite has the ability to shoot
        self.canShoot = True
        # The health of the player
        self.health = 100
        # The ammo of the player
        self.ammo = 100
        # The state of the player
        self.alive = True


    def update(self):
        # Getting input from the mouse and keyboard
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # Making sure the character can't walk off the screen
        if self.rect.x <= 0:
            self.rect.x = 0
        # Making sure the character doesn't fall through the floor
        if self.rect.y >= floor:
            self.rect.y = floor
            self.jumped = False
        # Using the keyboard inputs to move the character appropriately
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            # This checks if the player needs to flip or not
            if self.facing == "right":
                # The flip function being called
                Player.flipIt(self)
                # Redefining the current facing direction
                self.facing = "left"
            Player.moveLeft(self)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.facing == "left":
                Player.flipIt(self)
                self.facing = "right"
            Player.moveRight(self)
        # Checking if the player can jump and hasn't jumped already
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.jumped == False:
            Player.jump(self)
            if self.rect.y <= (floor - ceiling):
                self.jumped = True
        # If the player let go of the jump key but hasn't reached the floor yet
        if ((keys[pygame.K_UP] == False and not keys[pygame.K_w]) and self.rect.y < floor):
            self.jumped = True
        # If the player has jumped, gravity is applied to the character
        if self.jumped == True:
            Player.gravity(self)
        # Using the mouse clicks to fire the gun
        # If the mouse is clicked and the player has ammo and can shoot
        if click[0] and self.canShoot == True and self.ammo > 0:
            # The location of the mouse is saved
            self.location = mouse
            # The player has shot
            self.shot = True
        # If the player cannot shoot the player stops shooting
        if self.canShoot == False:
            self.shot = False
        # If the player stops pressing the mouse he can shoot again
        if click[0] == False:
            self.canShoot = True
        # Checking if the player is alive
        Player.alive(self)


    # This function flips the characters sprite
    def flipIt(self):
        self.image = pygame.transform.flip(self.image, True, False)


    # The following 4 functions move the character
    def moveRight(self):
        self.rect.x += (display_width / 100)


    def moveLeft(self):
        self.rect.x -= (display_width / 100) 


    def jump(self):
        self.rect.y -= (display_height / 100) * 4
        

    def gravity(self):
        self.rect.y += (display_height / 100) * 4


    # Checks if the character has died
    def alive(self):
        if self.health <= 0:
            self.alive = False


# This is a class for the enemies walking along the ground
class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Loads the enemy sprite
        self.image = pygame.image.load("../images/bad_guy.png")
        self.image = pygame.transform.scale(self.image, (char_size, char_size))
        # Has the enemy start facing left
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        # This enemy starts on the floor
        self.rect.y = floor
        # Randomizes the starting location of the enemy off the screen
        self.rect.x = random.randint(display_width, display_width + (6*char_size))
        # This enemy has 100 health points
        self.health = 100
        self.alive = True
        self.shot = False
        # This gets the current time
        self.lastFire = pygame.time.get_ticks()
        # This sets the cooldown period between shots
        self.cooldown = 3000
        self.facing = "left"
        # THe enemy has a speed of -9
        self.speed = -9
        # This variable says if the enemy is on the screen
        self.onScreen = False


    def update(self):
        # This moves the enemy
        self.rect.x += self.speed
        # This checks if the enemy is on the screen
        if self.rect.x > 0 and self.rect.x < display_width - char_size:
            self.onScreen = True
        # This checks if the enemy has reached either side of the screen is actually on the screen
        if (self.rect.x < 0 or self.rect.x > display_width - char_size) and self.onScreen:
            # The enemy's speed is reversed
            self.speed = self.speed *-1
            # The enemy then flips its facing direction
            if self.facing == "left":
                Enemy.flip(self)
                self.facing = "right"
            elif self.facing == "right":
                Enemy.flip(self)
                self.facing = "left"
        # Checking if the enemy is alive
        if self.health <= 0:
            self.alive = False
        # Calling the health bar function
        Enemy.healthBar(self)
        # The enemy can only fire if it is on the screen
        if self.onScreen:
            Enemy.shoot(self)


    # A function that displays the enemy's health as a bar
    def healthBar(self):
        # A ratio is created between the make health and size of the character
        tempInt = char_size / 100
        # A red bar is displayed above the enemy that is hidden by th green bar
        pygame.draw.rect(gameDisplay, RED, ((self.rect.x, self.rect.y - 10, char_size, 15)))
        # A green bar overlaps the red and each time its shot the bar shrinks
        pygame.draw.rect(gameDisplay, GREEN, ((self.rect.x, self.rect.y - 10, (char_size - tempInt*(100 - self.health)) , 15)))


    # A function that controls when the enemy can fire
    def shoot(self):
        # This gets the present time
        presentTime = pygame.time.get_ticks()
        # This checks if the time between shots has reached the cooldown time
        if (presentTime - self.lastFire) >= self.cooldown:
            # The lastFire time is reset to the present time
            self.lastFire = presentTime
            # The gun shoots
            self.shot = True


    # A function that flips the sprite
    def flip(self):
        self.image = pygame.transform.flip(self.image, True, False)


# The bullet class creates all bullets fired from the player
class Bullet(pygame.sprite.Sprite):

    # Unlike the player and enemy classes, this class requires some parameters
    def __init__(self, player_x, player_y, facing, location):
        pygame.sprite.Sprite.__init__(self)
        # A small rectangle is used as the sprite
        self.image = pygame.Surface((2,2))
        self.image = pygame.transform.scale(self.image, (int(char_size/20), int(char_size/20)))
        # The colour of the rectangle is orange
        self.image.fill(ORANGE)
        self.rect = self.image.get_rect()
        # The y coordinate of the guns barrel is set as the staring location
        self.originY = player_y + (char_size/3)
        # Determining the starting location based on the way the character is facing
        if facing == "right":
            self.originX = player_x + (8*char_size/9)
        if facing == "left":
            self.originX = player_x
        self.facing = facing
        # The damage the bullet does
        self.damage = 10
        # Sets the bullet's status to "alive"
        self.alive = True
        # The location of the mouse when the bullet was fired
        self.location = location
        # Setting the starting location of the bullet
        self.rect.x = self.originX
        self.rect.y = self.originY
        # Setting the speed of the bullet
        self.speed = 45


    def update(self):
        # This calls the calc function
        Xspeed, Yspeed = Bullet.calc(self)
        # These if statements help make sure the the velocities are correct in all 4 quadrants
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
        # Check if the bullet has gone off screen
        if self.rect.x > display_width or self.rect.x < 0 or self.rect.y < 0 or self.rect.y > display_height:
            self.alive = False


    # This function calculates the velocities of the bullet in both the x and y directions
    # This is based on the player's and mouse positions
    def calc(self):
        # This uses pythangorean theorem to determine the speed in both directions
        # A small value of 0.0001 is added to the delataX so that there is no dividing by 0 error
        deltaX = self.location[0] - self.originX + 0.0001
        deltaY = self.location[1] - self.originY
        theta = math.atan(deltaY/deltaX)
        Xspeed = self.speed * math.cos(theta)
        Yspeed = self.speed * math.sin(theta)
        return Xspeed, Yspeed


# The class for all the enemy bullets
# This is similar to that of the Bullet class
class enemyBullet(pygame.sprite.Sprite):

    def __init__(self, player_x, player_y, facing, enemy_x, enemy_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((2,2))
        # These bullets are bigger than the player's
        self.image = pygame.transform.scale(self.image, (int(char_size/15), int(char_size/15)))
        # The colour of these bullets are purple
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        # The bullet has a different staring location for the sprite
        self.originY = enemy_y + (char_size/3)
        if facing == "right":
            self.originX = enemy_x + (8*char_size/9)
        if facing == "left":
            self.originX = enemy_x
        self.facing = facing
        self.damage = 10
        self.alive = True
        self.player_x = player_x
        self.player_y = player_y
        self.rect.x = self.originX
        self.rect.y = self.originY
        self.speed = 45


    def update(self):
        # Calling the calc function
        Xspeed, Yspeed = enemyBullet.calc(self)
        # Making sure the bullet travels in the right direction
        if (self.player_x < self.originX):
            self.rect.x -= Xspeed
            self.rect.y -= Yspeed
        elif(self.player_x > self.originX):
            self.rect.x += Xspeed
            self.rect.y += Yspeed
        # Check if the bullet is off the screen
        if self.rect.x > display_width or self.rect.x < 0 or self.rect.y < 0 or self.rect.y > display_height:
            self.alive = False


    # This function calculates the velocities of the bullet based on the player's and enemy's location
    def calc(self):
        deltaX = self.player_x - self.originX + char_size/2 + 0.0001
        deltaY = self.player_y + (char_size/2) - self.originY
        theta = math.atan(deltaY/deltaX)
        Xspeed = self.speed * math.cos(theta)
        Yspeed = self.speed * math.sin(theta)
        return Xspeed, Yspeed


# A class for the player on the menu screen
# This character does not fire and instead just moves along the ground
class menugoodGuy(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("../images/main_guy.png")
        self.image = pygame.transform.scale(self.image, (char_size, char_size))
        self.rect = self.image.get_rect()
        self.rect.y = floor
        self.rect.x = 0


    # Controls the movement and makes sure he stays on screen
    def update(self):
        # This guy has a set movement speed
        self.rect.x += 7
        # If he goes off the screen he comes back on from the other side
        if self.rect.x > display_width:
            self.rect.x = 0 - char_size


# A class for the enemies on the menu screen
# This class is simliar to the player menu guy because they only move in a set direction
class menubadGuy(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("../images/bad_guy.png")
        self.image = pygame.transform.scale(self.image, (char_size, char_size))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.y = floor
        # The enemy has a random staring location in the x direction
        self.rect.x = random.randint(0, display_width)


    # Controls the movement and makes sure he stays on screen
    def update(self):
        self.rect.x -= random.randint(0, 25)
        if self.rect.x < 0 - char_size:
            self.rect.x = display_width + char_size


# A class for the player that appears on the tutorial screen
class tutorialGuy(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("../images/main_guy.png")
        self.image = pygame.transform.scale(self.image, (char_size, char_size))
        self.rect = self.image.get_rect()
        self.rect.y = floor
        self.facing = "right"
        self.shot = False
        self.canShoot = True
        # This character stars at a different x position
        self.rect.x = 1200


    # All the same functionality as he normal player however the area of movement is reduced
    def update(self):
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # Limited area for movement
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
        

# The class for the enemies on the ledges
# Same as the ground enemy except for its movement and initial position
class ledgeEnemy(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("../images/bad_guy.png")
        self.image = pygame.transform.scale(self.image, (char_size, char_size))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        # Starts higher off the ground
        self.rect.y = floor - 500
        self.rect.x = random.randint(display_width, display_width + (7*char_size))
        self.health = 100
        self.alive = True
        self.ledge_reached = False
        self.shot = False
        self.lastFire = pygame.time.get_ticks()
        self.cooldown = 3000
        self.facing = "left"
        self.onScreen = False
        self.speed = -9


    def update(self):
        # The enemy can only move to the edge of the ledge and then reverses direction
        self.rect.x += self.speed
        if self.rect.x > 0 and self.rect.x < display_width - char_size:
            self.onScreen = True
        if (self.rect.x < 1500 or self.rect.x > display_width - char_size) and self.onScreen:
            self.shot = False
            self.speed = self.speed *-1

        if self.health <= 0:
            self.alive = False
        ledgeEnemy.healthBar(self)
        if self.onScreen:
            ledgeEnemy.shoot(self)


    def healthBar(self):
        tempInt = char_size / 100
        pygame.draw.rect(gameDisplay, RED, ((self.rect.x, self.rect.y - 10, char_size, 15)))
        pygame.draw.rect(gameDisplay, GREEN, ((self.rect.x, self.rect.y - 10, (char_size - tempInt*(100 - self.health)) , 15)))


    def shoot(self):
        presentTime = pygame.time.get_ticks()
        if (presentTime - self.lastFire) >= self.cooldown and self.rect.x < display_width:
            self.lastFire = presentTime
            self.shot = True


# The class for the ledges that appear in some levels
class Ledge(pygame.sprite.Sprite):

    # This is a solid black rectangle that absorbs bullets from the player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((2,2))
        self.image = pygame.transform.scale(self.image, (500, 50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        # This object is created off the ground and to the right of the screen
        self.rect.y = floor - 300
        self.rect.x = display_width - 500


# This is the class for the pick items that appear in the transistion "merchant" scenes
class pickUp(pygame.sprite.Sprite):

    # This object requires parameters
    def __init__(self, image, x, y, pickType, player):
        pygame.sprite.Sprite.__init__(self)
        # Depending on the type an image is used
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.type = pickType
        # The collision with the player is set to false
        self.collide = False
        # This gets the attributes of the player
        self.player = player


    def update(self):
        # The pickup displays different text depending on what it is
        if self.type == "health":
            displayText("Big Health", '../fonts/Antonio-Regular.ttf', 25, display_width / 2 - 650, floor - 230, BLACK, 10)
        elif self.type == "ammo":
            displayText("Big Ammo", '../fonts/Antonio-Regular.ttf', 25, display_width / 2 - 350, floor - 230, BLACK, 10)
        elif self.type == "both":
            # The small ammo picture is displayed seperately
            gameDisplay.blit(small_ammo, (display_width / 2 - 50, floor - 170))
            displayText("Small Health", '../fonts/Antonio-Regular.ttf', 25, display_width / 2 - 50, floor - 240, BLACK, 10)
            displayText("Small Ammo", '../fonts/Antonio-Regular.ttf', 25, display_width / 2 - 50, floor - 200, BLACK, 10)


        # Check if the player touches the pickup and then give the player the bonuses
        if self.collide:
            if (self.type == "health"):
                self.player.health += 50
                self.collide = False
            elif (self.type == "ammo"):
                self.player.ammo += 50
                self.collide = False
            elif (self.type == "both"):
                self.player.health += 25
                self.player.ammo += 25
            # Make sure the player can only have a certain maximum of health and ammo
            if self.player.health >= 100:
                self.player.health = 100
            if self.player.ammo >= 300:
                self.player.ammo = 300


# The class for the secret boss enemy.
# This is the same as the other enemies however it has a different sprite image, size, speed, and health.
class bossGuy(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Using the same merchant sprite
        self.image = pygame.image.load('../images/merchant.png')
        self.image = pygame.transform.scale(self.image, (400, 640))
        self.rect = self.image.get_rect()
        self.rect.y = floor - 400
        self.rect.x = random.randint(display_width, display_width + (6*char_size))
        # Higher health than normal
        self.health = 500
        self.alive = True
        self.shot = False
        self.lastFire = pygame.time.get_ticks()
        # Shorter cooldown between shots than normal
        self.cooldown = 1000
        self.facing = "left"
        # Slower speed than normal
        self.speed = -3
        self.onScreen = False

 
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > 0 and self.rect.x < display_width - char_size:
            self.onScreen = True
        if (self.rect.x < 0 or self.rect.x > display_width - char_size) and self.onScreen:
            self.shot = False
            self.speed = self.speed *-1
            if self.facing == "left":
                Enemy.flip(self)
                self.facing = "right"
            elif self.facing == "right":
                Enemy.flip(self)
                self.facing = "left"
        if self.health <= 0:
            self.alive = False
        bossGuy.healthBar(self)
        if self.onScreen:
            bossGuy.shoot(self)


    def healthBar(self):
        # Health bar had to be adjusted for the higher health
        tempInt = 400 / 500
        pygame.draw.rect(gameDisplay, RED, ((self.rect.x, self.rect.y - 10, 400, 15)))
        pygame.draw.rect(gameDisplay, GREEN, ((self.rect.x, self.rect.y - 10, (400 - tempInt*(500 - self.health)) , 15)))


    def shoot(self):
        presentTime = pygame.time.get_ticks()
        if (presentTime - self.lastFire) >= self.cooldown:
            self.lastFire = presentTime
            self.shot = True


    def flip(self):
        self.image = pygame.transform.flip(self.image, True, False)
