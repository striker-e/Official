import pygame
import math
#add height as a constructor parameter
class Laser(pygame.sprite.Sprite):
    def __init__(self,angle,speed,spawnpoint):
        super().__init__()
        self.base_image = pygame.image.load('./assets/laser.png').convert_alpha()
        self.base_image = pygame.transform.rotate(self.base_image, 0)
        self.image = self.base_image
        self.rect = self.image.get_rect(center = spawnpoint)
        self.pos = pygame.Vector2(self.rect.center) #Storing pos as a vector which handles floating point, which will fix rounding errors and bugs
        self.vec = pygame.Vector2()
        self.angle = angle * -1
        self.vec.x = math.sin(((self.angle)/180)*math.pi) * speed
        self.vec.y = math.cos(((self.angle)/180)*math.pi) * speed
        oldcenter = self.rect.center
        self.image = pygame.transform.rotate(self.base_image, angle)
        self.rect = self.image.get_rect()
        self.rect.center = oldcenter
        #self.yconstraint = height
    #def destroy(self):
        #if self.rect.y <= -50 or self.rect.y >= self.yconstraint + 50:
            #self.kill()
    def update(self):
        self.pos.x += self.vec.x
        self.pos.y -= self.vec.y
        self.rect.center = self.pos.x,self.pos.y
        #self.destroy()
        
class AlienLaser(pygame.sprite.Sprite):
    def __init__(self,spawnpoint, height):
        super().__init__()
        self.image = pygame.image.load('./assets/laser.png').convert_alpha()
        self.rect = self.image.get_rect(center = spawnpoint)

    def update(self):
        self.rect.y += 5
        