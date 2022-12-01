import pygame
from pausemenu import PauseMenu
class GameOver(PauseMenu):
    def __init__(self,screen,width,height,score):
        super().__init__(screen,width,height)
        self.score = score
    def draw(self):
        self.screen.fill("black")
        text = self.font.render(f"Game Over You Got A Score Of {self.score}",True,"white")
        textrect = text.get_rect()
        textrect.center = self.width/2,self.height/2
        self.screen.blit(text,textrect)
        othertext = self.font.render(f"To Return To Menu Press Return",True,"red")
        othertextrect = othertext.get_rect()
        othertextrect.center = self.width/2, self.height * 0.75
        self.screen.blit(othertext,othertextrect)