import pygame
from pausemenu import PauseMenu
from text import Text
class GameOver(PauseMenu):
    def __init__(self,screen,width,height):
        super().__init__(screen,width,height)
        self.username = '123'
    def draw(self,score):
        self.screen.fill("black")
        scoreprint = Text(f"Game Over You Got a Score of {score}",(self.width/2,self.height/2),self.screen,"white")
        scoreprint.draw()
        returnmenu = Text("To Return To Menu Press Return",(self.width/2,self.height * 0.75),self.screen,"red")
        returnmenu.draw()
        enterusername = Text("Enter Your Username TO Save Below",(self.width * 0.50,self.height * 0.10),self.screen,"blue")
        enterusername.draw()
        usernamerect = pygame.Rect(self.width * 0.50 - 50,self.height* 0.10, 100,20)
        usernamerect.center = self.width/2,self.height * 0.20
        pygame.draw.rect(self.screen,"white",usernamerect,1)
        usernametext = Text(self.username,usernamerect.center,self.screen,"lightblue")
        usernametext.draw()