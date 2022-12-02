import pygame
from pausemenu import PauseMenu
from text import Text
import os
class GameOver(PauseMenu):
    def __init__(self,screen,width,height):
        super().__init__(screen,width,height)
        self.username = '123'
        self.topfive = []
    def draw(self,score):
        self.screen.fill("black")
        scoreprint = Text(f"Game Over You Got a Score of {score}",(self.width/2,self.height/2),self.screen,"white",1)
        scoreprint.draw()
        returnmenu = Text("To Return To Menu Press Tab",(self.width/2,self.height * 0.75),self.screen,"red",1)
        returnmenu.draw()
        enterusername = Text("Enter Your Username TO Save Below Press Return To Save and Go To Mennu",(self.width * 0.50,self.height * 0.10),self.screen,"blue",1)
        enterusername.draw()
        usernamerect = pygame.Rect(self.width * 0.50 - 50,self.height* 0.10, 100,20)
        usernamerect.center = self.width/2,self.height * 0.20
        pygame.draw.rect(self.screen,"white",usernamerect,1)
        usernametext = Text(self.username,usernamerect.center,self.screen,"lightblue")
        usernametext.draw()
    def savefunction(self,score):
        self.filename = "highscore.txt"
        w = open(self.filename,"a+")
        lines = open(self.filename,'r').readlines()
        print(lines)
        text = f'{self.username} : {score}'
        for line in lines:
            if self.username in line:
                print("Found Identical")
                lineindex = lines[line]
                lines[lineindex] = text
                w.writelines(lines)
        w.write(text)
        w.close()

