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
    def restrictmovement(self,leftconstraint,rightconstraint):
        if self.rect.right >= rightconstraint:
            self.rect.right = rightconstraint
        elif self.rect.left <= leftconstraint:
            self.rect.left = leftconstraint
    def update(self,leftconstraint,rightconstraint):
        self.get_input()
        self.restrictmovement(leftconstraint,rightconstraint)
        self.rect.midbottom = (self.position.x, self.position.y)