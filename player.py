import pygame
from gamescreen import GameScreen
class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.base_image = pygame.image.load('./assets/blue_ship.png')
        self.base_image = pygame.transform.scale(self.base_image, (30,30))
        self.image = self.base_image
        self.width = 1280
        self.height = 720
        self.speed = 5
        self.position = pygame.math.Vector2(pos)
        self.rect = self.base_image.get_rect(midbottom = self.position)
    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.position.x += self.speed
        elif keys[pygame.K_DOWN]:
            self.position.x -= self.speed
        elif keys[pygame.K_RIGHT]:
            pass
        elif keys[pygame.K_LEFT]:
            pass
    def restrictmovement(self):
        if self.rect.right >= self.xplusconstraint:
            self.rect.right = self.xplusconstraint
        elif self.rect.left <= self.xminusconstraint:
            self.rect.left = self.xminusconstraint
    def update(self):
        self.get_input()
        self.rect.midbottom = (self.position.x, self.position.y)