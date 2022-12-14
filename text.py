import pygame
class Text():
    def __init__(self,text,rectpos,screen,colour,rect = "center",size = None):
        self.string = text
        self.pos = rectpos
        self.screen = screen
        self.colour = colour
        self.size = 16
        if size:
            self.size = size
        self.font = pygame.font.Font('assets/font.TTF',self.size)
        self.text = self.font.render(self.string,True,self.colour)
        if rect:
            self.textrect = self.text.get_rect(center = self.pos)
        else:
            self.textrect = self.text.get_rect(midleft = self.pos)
    def draw(self):
        self.screen.blit(self.text,self.textrect)