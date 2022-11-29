import pygame
from gamescreen import GameScreen
from laser import Laser
import math
class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.base_image = pygame.image.load('./assets/blue_ship.png')
        self.base_image = pygame.transform.scale(self.base_image, (30,30))
        self.image = self.base_image
        self.width = 1280
        self.height = 720
        self.speed = 5
        self.ready = True
        self.lasertime = 0
        self.dir= 0 
        self.cooldown = 600
        self.laserangle = 0
        self.lasers = pygame.sprite.Group()
        self.position = pygame.math.Vector2(pos)
        self.rect = self.base_image.get_rect(midbottom = self.position)
    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.position.x += self.speed
        elif keys[pygame.K_DOWN]:
            self.position.x -= self.speed
        elif keys[pygame.K_RIGHT]:
            self.turnright()
        elif keys[pygame.K_LEFT]:
            self.turnleft()
        elif keys[pygame.K_SPACE] and self.ready:
            self.shoot()
            self.ready = False
            self.lasertime = pygame.time.get_ticks()
    def charge(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.lasertime >= self.cooldown:
                self.ready = True
    def turnleft(self):
        oldcenter = self.rect.center
        if self.dir <= 90:
            self.dir += 1
        self.image = pygame.transform.rotate(self.base_image, self.dir)
        self.rect = self.image.get_rect()
        self.rect.center = oldcenter
        self.position = pygame.Vector2(self.rect.midbottom)
        self.laserangle = self.dir
    def turnright(self):
        oldcenter = self.rect.center
        if self.dir >= -90:
            self.dir -= 1
        self.image = pygame.transform.rotate(self.base_image, self.dir)
        self.rect = self.image.get_rect()
        self.rect.center = oldcenter
        self.position = pygame.Vector2(self.rect.midbottom)
        self.laserangle = self.dir
    def alignment(self):
        center = pygame.Vector2()
        radius = (self.base_image.get_height() - 5)/2
        center.x,center.y = self.rect.center
        self.spawnpoint = (center.x + (math.cos(((self.dir*-1) -90)/180 * math.pi) * radius),center.y + (math.sin(((self.dir*-1) -90)/180 * math.pi) * radius))
        self.checker = int(self.spawnpoint[0]),int(self.spawnpoint[1])
    def shoot(self):
        self.lasers.add(Laser(self.laserangle,3,self.spawnpoint))
        self.lasers.update()
        print("Dog")
    def restrictmovement(self,leftconstraint,rightconstraint):
        if self.rect.right > rightconstraint:
            self.rect.right = rightconstraint
            self.position = pygame.Vector2(self.rect.midbottom)
        elif self.rect.left < leftconstraint:
            self.rect.left = leftconstraint
            self.position = pygame.Vector2(self.rect.midbottom)
    def update(self,leftconstraint,rightconstraint):
        self.get_input()
        self.alignment()
        self.rect.midbottom = (self.position.x, self.position.y)
        self.restrictmovement(leftconstraint,rightconstraint)
        self.charge()
        self.lasers.update()