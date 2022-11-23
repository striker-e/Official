import pygame, sys
from menu import Menu
from gamescreen import GameScreen
from player import Player
from alien import Alien
from laser import Laser, AlienLaser
import random
p1 = 1
p2 = 1
class Game:
    def __init__(self,screen,width,height,p1,p2):
        self.p1 = p1
        self.p2 = p2
        self.screen = screen
        self.width = width
        self.height = height
        self.gamescreen = GameScreen(self.screen, self.width, self.height)
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
        x_dist,y_dist = x_dist * self.p1, y_dist * self.p2
        for row_index, row in enumerate(range(rows)):
            for col_index, col in enumerate(range(cols)):
                x = col_index * x_dist + self.gamescreen.gamewindow.left
                y = row_index * y_dist + self.gamescreen.gamewindow.top
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
                self.alien_move_down(0.6)
            elif alien.rect.left <= leftconstraint:
                self.alien_direction = 1
                self.alien_move_down(0.6)
    def alien_move_down(self, distance):
        if self.aliens:
            for alien in self.aliens.sprites(): 
                alien.rect.y += distance
    def alien_shoot(self):
        if self.aliens.sprites():
            random_alien = random.choice(self.aliens.sprites())
            laser_sprite = AlienLaser(random_alien.rect.center, height)
            self.alien_lasers.add(laser_sprite)
    def run(self):
        self.gamescreen = GameScreen(self.screen, self.width, self.height)
        self.player.update(self.gamescreen.gamewindow.left,self.gamescreen.gamewindow.right)
        self.aliens.update(self.alien_direction)
        self.aliencheckpos(self.gamescreen.gamewindow.left,self.gamescreen.gamewindow.right)
        self.alien_lasers.update()
        self.screen.fill("black")
        self.player.draw(self.screen)
        self.aliens.draw(screen)
        self.alien_lasers.draw(screen)
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
    while True:
        if running == False:
            para = p1
            para2 = p2
            game = Game(screen,width,height,para,para2)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                new_width = max(800,event.size[0])
                new_height = max(600,event.size[1])
                screen = pygame.display.set_mode((new_width,new_height),pygame.RESIZABLE)
                p1 = screen.get_width()/width
                p2 = screen.get_height()/height
                game.player.sprite.position.x *= p1
                game.player.sprite.position.y *= p2
                for alien in game.all_aliens:
                    alien.pos[0] *= p1
                    alien.pos[1] *= p2
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