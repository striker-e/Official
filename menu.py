import pygame
class Menu:
    menuoptions = ["Solo Mode", "Coop", "Online","Options"]
    adjust = 30
    def __init__(self,width,height,screen):
        self.screen = screen
        self.width = width
        self.height = height
        self.colourstates = ["white","red"]
        self.index = 0
        self.one = 1
        self.two = 0
        self.three = 0
        self.four = 0
        self.font = pygame.font.Font('assets/font.TTF', 32)
    def draw(self):
        self.solomode = self.font.render(self.menuoptions[0],True,self.colourstates[self.one])
        self.solomoderect = self.solomode.get_rect()
        self.solomoderect.midleft = (50, 50)
        self.screen.blit(self.solomode, self.solomoderect)
        self.coopmode = self.font.render(self.menuoptions[1],True,self.colourstates[self.two])
        self.coopmoderect = self.coopmode.get_rect()
        self.coopmoderect.midleft = (50, 100)
        self.screen.blit(self.coopmode, self.coopmoderect)
        self.onlinemode = self.font.render(self.menuoptions[2],True, self.colourstates[self.three])
        self.onlinemoderect = self.onlinemode.get_rect()
        self.onlinemoderect.midleft = (50,150)
        self.screen.blit(self.onlinemode, self.onlinemoderect)
        self.option = self.font.render(self.menuoptions[3],True,self.colourstates[self.four])
        self.optionrect = self.option.get_rect()
        self.optionrect.midleft = (50, 200)
        self.screen.blit(self.option, self.optionrect)
    def manager(self):
        pass
    def change(self, value: bool):
        def assign():
            match self.index:
                    case 0:
                        self.one,self.two,self.three,self.four = 1,0,0,0
                    case 1:
                        self.one,self.two,self.three,self.four = 0,1,0,0
                    case 2:
                        self.one,self.two,self.three,self.four = 0,0,1,0
                    case 3:
                        self.one,self.two,self.three,self.four = 0,0,0,1    
        if value:
            if self.index != 3:
                self.index += 1
                assign()
            else:
                self.one,self.two,self.three,self.four = 0,0,0,1
        elif not value:
            if self.index != 0:
                self.index -= 1
                assign()
            else:
                self.one,self.two,self.three,self.four = 1,0,0,0
