import pygame
class Alien(pygame.sprite.Sprite):
    def __init__(self,colour,x,y):
        super().__init__()
        file_path = './assets/' + colour + '.png'
        self.base_image = pygame.image.load(file_path).convert_alpha()
        self.base_image = pygame.transform.scale(self.base_image, (20,20))
        self.image = self.base_image
        self.pos = pygame.math.Vector2(x,y)
        self.rect = self.image.get_rect(topleft = self.pos)
        self.mask = pygame.mask.from_surface(self.image)
    def update(self, direction):
        self.pos[0] += direction 
        self.rect.midtop = self.pos.x,self.pos.y
        

