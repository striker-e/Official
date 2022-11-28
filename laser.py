import pygame
#add height as a constructor parameter
class Laser(pygame.sprite.Sprite):
    def __init__(self,angle,speed,spawnpoint):
        super().__init__()
        self.base_image = pygame.image.load('./assets/laser.png').convert_alpha()
        self.base_image = pygame.transform.rotate(self.base_image, 0)
        self.image = self.base_image
        self.rect = self.image.get_rect(center = spawnpoint)
        self.vec = pygame.Vector2()
        self.vec.from_polar((speed,angle + 90))
        oldcenter = self.rect.center
        self.image = pygame.transform.rotate(self.base_image, angle)
        self.rect = self.image.get_rect()
        self.rect.center = oldcenter
        #self.yconstraint = height
    #def destroy(self):
        #if self.rect.y <= -50 or self.rect.y >= self.yconstraint + 50:
            #self.kill()
    def update(self):
        self.rect.x += self.vec[0]
        self.rect.y -= self.vec[1]
        #self.destroy()
        
class AlienLaser(pygame.sprite.Sprite):
    def __init__(self,spawnpoint, height):
        super().__init__()
        self.image = pygame.image.load('./assets/laser.png').convert_alpha()
        self.rect = self.image.get_rect(center = spawnpoint)

    def update(self):
        self.rect.y += 5
        