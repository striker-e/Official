import pygame
from pausemenu import PauseMenu
from text import Text
import os
class GameOver(PauseMenu):
    def __init__(self,screen,width,height):
        super().__init__(screen,width,height)
        self.username = '123'
        self.val = 1
    def draw(self,score):
        self.screen.fill("black")
        if self.val == True:
            whogothit = Text("Player 2 or RED Got Hit",(self.width/2,self.height * 0.30),self.screen,"white",1)
            whogothit.draw()
        elif self.val== 2:
            whogothit = Text("You won",(self.width/2,self.height * 0.30),self.screen,"white",1)
            whogothit.draw()
        elif self.val == False:
            whogothit = Text("Player 1 or BLUE Got Hit",(self.width/2,self.height * 0.30),self.screen,"white",1)
            whogothit.draw()
        scoreprint = Text(f"Game Over You Got a Score of {score}",(self.width/2,self.height/2),self.screen,"white",1)
        scoreprint.draw()
        returnmenu = Text("To Return To Menu Press Tab",(self.width/2,self.height * 0.75),self.screen,"red",1)
        returnmenu.draw()
        enterusername = Text("Enter Your Username TO Save Below Press Return To Save and Go To Menu",(self.width * 0.50,self.height * 0.10),self.screen,"white",1)
        enterusername.draw()
        usernamerect = pygame.Rect(self.width * 0.50 - 50,self.height* 0.10, 100,20)
        usernamerect.center = self.width/2,self.height * 0.20
        pygame.draw.rect(self.screen,"white",usernamerect,1)
        usernametext = Text(self.username,usernamerect.center,self.screen,"lightblue")
        usernametext.draw()
    def savefunction(self,score):
        self.filename = "highscore.txt"
        w = open(self.filename,"a+")
        writescore = str(score)
        w.write(writescore+ ":" +self.username + "\n")
        w.close()
    def topfive(self):
        r = open("highscore.txt","r")
        lines = r.readlines()
        sortedlines = sorted(lines,key=lambda x:int(x.split(":")[0]),reverse=True)
        sortedlines = sortedlines[:5]
        return sortedlines
        """ 
            This code makes use of lambda functions which is the same as 
            def simplefunction(val):
                score,value = val.split(":")
                return int(score)
            sortedlines = sorted(lines, key=simplefunction, reverse=True)
            key takes previous argument and applies function on each element 
            like map(), and key just lets sorted() know how to sort the iterable.
            In this case it sorts it based on the first element after splitting each element.
        """
    def deletehighscores(self):
        open("highscore.txt","w").close()