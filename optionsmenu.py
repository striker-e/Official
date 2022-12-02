import pygame
from text import Text
from gameover import GameOver
class OptionsMenu():
    def __init__(self,screen,width,height):
        self.screen = screen
        self.width = width
        self.height = height
    def draw(self):
        self.screen.fill("black")
        guidancetext = Text("Controls Shown Below",(self.width/3,self.height * 0.10),self.screen,"white")
        guidancetext.draw()
        # controlsimage = pygame.image.load('assets/controls.png')
        # controlsimagerect = controlsimage.get_rect(center = (self.width/3, self.height * 0.25))
        # self.screen.blit(controlsimage,controlsimagerect)

