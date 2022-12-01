import pygame
class GameScreen:
    def __init__(self,screen,width,height):
        self.screen = screen
        self.width = width
        self.height = height
        self.score = 0  
        self.font = pygame.font.Font('assets/font.TTF', 32)
        self.left = self.width * 0.33
        self.top = self.height * 0.30
        self.gamewindowwidth = self.width * 0.35
        self.gamewindowheight = self.height * 0.60
        self.gamewindow = pygame.Rect(self.left,self.top,self.gamewindowwidth,self.gamewindowheight)
        self.rect = self.gamewindow
        self.mask = pygame.mask.Mask(self.gamewindow.size, True)
    def draw(self):
        self.gamewindow = pygame.Rect(self.left,self.top,self.gamewindowwidth,self.gamewindowheight)
        self.gamewindow = pygame.draw.rect(self.screen,"white",self.gamewindow,2)
        scoredisplay = self.font.render(f"Score {self.score}",True,"white")
        scorerect = scoredisplay.get_rect()
        scorerect.midleft = (20,50)
        self.screen.blit(scoredisplay,scorerect)  
