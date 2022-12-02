import pygame
from text import Text
class PauseMenu():
    def __init__(self,screen,width,height): #Constructor, takes in the screen to draw, width and height for positioning info. Loads font.
        self.screen = screen
        self.font = pygame.font.Font('assets/font.TTF',16)
        self.width = width
        self.height = height
    def draw(self): #Draw function, fills screen black when paused and draws text over.
        self.screen.fill("black ")
        text = Text("To return to menu press tab or To resume game press p",(self.width/2,self.height/2),self.screen,"white",1)
        text.draw()
 