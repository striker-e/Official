import pygame
class PauseMenu():
    def __init__(self,screen,width,height): #Constructor, takes in the screen to draw, width and height for positioning info. Loads font.
        self.screen = screen
        self.font = pygame.font.Font('assets/font.TTF',16)
        self.width = width
        self.height = height
    def draw(self): #Draw function, fills screen black when paused and draws text over.
        self.screen.fill("black")
        text = self.font.render("To return to menu press return or To resume game press p", True, "white")
        textrect = text.get_rect()
        textrect.center = self.width/2,self.height/2 # Center text correctly.
        self.screen.blit(text,textrect)