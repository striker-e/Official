import pygame
class Text():
    def __init__(self,text,rectpos,screen,colour):
        self.string = text
        self.pos = rectpos
        self.screen = screen
        self.colour = colour
        self.font = pygame.font.Font('assets/font.TTF',16)
        self.text = self.font.render(self.string,True,self.colour)
        self.textrect = self.text.get_rect(center = self.pos)
    def draw(self):
        self.screen.blit(self.text,self.textrect)