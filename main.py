import pygame, sys
from menu import Menu
from gamescreen import GameScreen
from player import Player
from alien import Alien
from laser import Laser, AlienLaser
from pausemenu import PauseMenu
import random
class Game:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.gamescreen = GameScreen(displayscreen, self.width, self.height)
        self.pos = self.gamescreen.gamewindow.midbottom
        self.player = Player(self.pos)
        self.player = pygame.sprite.GroupSingle(self.player)
        self.aliens = pygame.sprite.Group()
        self.aliencreation(rows = 7, cols = 10)
        self.alien_direction = 1
        self.alien_lasers = pygame.sprite.Group()
        self.all_aliens = self.aliens.sprites()
    def aliencreation(self, cols, rows):
        x_dist = 30
        y_dist = 30
        for row_index, row in enumerate(range(rows)):
            for col_index, col in enumerate(range(cols)):
                x = col_index * x_dist + self.gamescreen.gamewindow.left + 10
                y = row_index * y_dist + self.gamescreen.gamewindow.top + 10
                if row_index == 0:
                    alien_sprite = Alien('yellow', x, y)
                elif 1 <= row_index <= 2: 
                    alien_sprite = Alien('green', x, y)
                elif 3 <= row_index <= 5:
                    alien_sprite = Alien('red', x, y)
                else:
                    alien_sprite = Alien('yellow', x ,y)
                self.aliens.add(alien_sprite)
    def aliencheckpos(self,leftconstraint,rightconstraint):
        for alien in self.all_aliens:
            if alien.rect.right >= rightconstraint:
                self.alien_direction = -1
                self.alien_move_down(0.5)
                print(alien.rect.x,alien.rect.y)
            elif alien.rect.left <= leftconstraint:
                self.alien_direction = 1
                self.alien_move_down(0.5)
                print(alien.rect.x,alien.rect.y)
    def alien_move_down(self, distance):
        if self.aliens:
            for alien in self.aliens.sprites(): 
                alien.pos[1] += distance
    def alien_shoot(self):
        if self.aliens.sprites():
            random_alien = random.choice(self.aliens.sprites())
            laser_sprite = AlienLaser(random_alien.rect.center, height)
            self.alien_lasers.add(laser_sprite)
    def run(self):
        self.gamescreen = GameScreen(displayscreen, self.width, self.height)
        self.player.sprite.update(self.gamescreen.gamewindow.left,self.gamescreen.gamewindow.right)
        self.aliens.update(self.alien_direction)
        self.aliencheckpos(self.gamescreen.gamewindow.left,self.gamescreen.gamewindow.right)
        #self.alien_shoot()
        self.alien_lasers.update()
        self.player.sprite.lasers.draw(displayscreen)
        displayscreen.fill("black")
        self.player.draw(displayscreen)
        self.aliens.draw(displayscreen)
        self.alien_lasers.draw(displayscreen)
        self.gamescreen.draw()
if __name__ == "__main__":
    pygame.init()
    width=1280
    height=720
    base_width = 1280
    base_height = 720
    background = pygame.image.load('./assets/background.jpg')
    background = pygame.transform.scale(background, (width, height))
    screen = pygame.display.set_mode((width,height),pygame.RESIZABLE)
    displayscreen = screen.copy()
    pygame.display.set_caption("PROJ")
    pygame.font.init()
    mainmenu = Menu(width,height,screen)
    pausemenu = PauseMenu(displayscreen,width,height)
    pausestate = False
    running = False
    clock = pygame.time.Clock()
    while True:
        if running == False and pausestate == False:
            game = Game(base_width,base_height)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                new_width = max(800,event.size[0])
                new_height = max(600,event.size[1])
                screen = pygame.display.set_mode((new_width,new_height),pygame.RESIZABLE)
                width,height = screen.get_width(),screen.get_height()
                #game.width, game.height = width,height
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_k:
                    mainmenu.change(True)
                elif event.key == pygame.K_i:
                    mainmenu.change(False)
                elif event.key == pygame.K_RETURN and mainmenu.index == 0 and pausestate == False:
                    running = True
                elif event.key == pygame.K_RETURN and pausestate == True:
                    running = False
                    pausestate = False
                elif event.key == pygame.K_BACKSPACE and pausestate == True:
                    running = True
                    pausestate = False
                elif event.key == pygame.K_ESCAPE:
                    running = False
                elif running and event.key == pygame.K_p:
                    pausestate = True
                    running = False
                    if pausestate:
                        pausemenu.draw()
        if running and pausestate == False:
            game.run()
        screen.blit(pygame.transform.scale(displayscreen,(screen.get_width(),screen.get_height())),(0,0))
        if running == False and pausestate == False:
            background = pygame.transform.scale(background, (width, height))
            screen.blit(background, (0,0))
            mainmenu.draw()
        pygame.display.update()
        clock.tick(60)