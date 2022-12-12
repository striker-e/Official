import pygame
from text import Text
from gameover import GameOver
class OptionsMenu():
    def __init__(self,screen,width,height):
        self.screen = screen
        self.width = width
        self.height = height
        self.onestate = False
    def draw(self):
        if not self.onestate:
            colour = "white"
        elif self.onestate:
            colour = "red"
        self.screen.fill("black")
        guidancetext = Text("Controls Shown Below",(self.width/3,self.height * 0.10),self.screen,"white")
        guidancetext.draw()
        deletehighscores = Text("Delete Highscores",(self.width/2,self.height * 0.8),self.screen,colour)
        deletehighscores.draw()
        # controlsimage = pygame.image.load('assets/controls.png')
        # controlsimagerect = controlsimage.get_rect(center = (self.width/3, self.height * 0.25))
        # self.screen.blit(controlsimage,controlsimagerect)

