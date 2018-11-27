import pygame
display_width, display_height = 2000, 1000


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("char-pikachu.png")
        self.image = pygame.transform.scale(self.image, (200,200))
        self.rect = self.image.get_rect()
        print(self.rect)


    def update(self):
        self.rect.y = 600
        self.rect.x += 5
        if self.rect.x > display_width:
            self.rect.x = display_width-100