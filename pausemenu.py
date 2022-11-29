import pygame
class PauseMenu():
    def __init__(self,screen,width,height):
        self.screen = screen
        self.font = pygame.font.Font('assets/font.TTF',16)
        self.width = width
        self.height = height
    def draw(self):
        self.screen.fill("black")
        text = self.font.render("To return to menu press return or To resume game press backspace", True, "white")
        textrect = text.get_rect()
        textrect.center = self.width/2,self.height/2
        self.screen.blit(text,textrect)
    def keychecker(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            print("case2")
            return 2
        elif keys[pygame.K_BACKSPACE]:
            print("case 1")
            return 1
        else:
            print("case 3")
            return 3