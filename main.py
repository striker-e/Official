import pygame, sys
from menu import Menu
from gamescreen import GameScreen
from player import Player
class Game:
    def __init__(self,screen,width,height):
        self.screen = screen
        self.width = width
        self.height = height
        self.gamescreen = GameScreen(self.screen, self.width, self.height)
        self.pos = self.gamescreen.gamewindow.midbottom
        self.player = Player(self.pos)
        self.player = pygame.sprite.GroupSingle(self.player)
    def run(self):
        self.gamescreen = GameScreen(self.screen, self.width, self.height)
        self.player.update()
        self.screen.fill("black")
        self.player.draw(self.screen)
        self.gamescreen.draw()
        
        

if __name__ == "__main__":
    pygame.init()
    width=1280
    height=720
    background = pygame.image.load('./assets/background.jpg')
    background = pygame.transform.scale(background, (width, height))
    screen = pygame.display.set_mode((width,height),pygame.RESIZABLE)
    pygame.display.set_caption("PROJ")
    pygame.font.init()
    mainmenu = Menu(width,height,screen)
    running = False
    clock = pygame.time.Clock()
    game = Game(screen,width,height)
    while True:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                new_width = max(800,event.size[0])
                new_height = max(600,event.size[1])
                screen = pygame.display.set_mode((new_width,new_height),pygame.RESIZABLE)
                print(game.player.sprite.rect.x/game.width, game.player.sprite.rect.y/game.height)
                p1,p2 = screen.get_width()/width,screen.get_height()/height
                game.player.sprite.position.x *= p1
                game.player.sprite.position.y *= p2
                print(game.player.sprite.rect.x/game.width, game.player.sprite.rect.y/game.height)
                width,height = screen.get_width(),screen.get_height()
                game.width, game.height = width,height
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    mainmenu.change(True)
                elif event.key == pygame.K_UP:
                    mainmenu.change(False)
                elif event.key == pygame.K_RETURN and mainmenu.index == 0:
                    running = True
                elif event.key == pygame.K_ESCAPE:
                    running = False
        if running:
            game.run()
        if running == False:
            background = pygame.transform.scale(background, (width, height))
            screen.blit(background, (0,0))
            mainmenu.draw()
        pygame.display.update()
        clock.tick(60)