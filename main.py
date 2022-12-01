import pygame, sys
from menu import Menu
from gamescreen import GameScreen
from player import Player
from alien import Alien
from laser import Laser, AlienLaser
from pausemenu import PauseMenu
from gameover import GameOver
import random
class Game:
    #Game Class Constructor,Creates Gamescreen with the initial resolution and positions it correctly, creates only one player object. Creates aliens once.
    def __init__(self,width,height,screen):
        self.screen = screen
        self.width = width
        self.height = height
        self.gamescreen = GameScreen(displayscreen, self.width, self.height)
        self.pos = self.gamescreen.gamewindow.midbottom
        self.playersprite = Player(self.pos)
        self.player = pygame.sprite.GroupSingle(self.playersprite)
        self.aliens = pygame.sprite.Group()
        self.aliencreation(rows = 7, cols = 10)
        self.alien_direction = 1
        self.alien_lasers = pygame.sprite.Group()
        self.all_aliens = self.aliens.sprites()
    def aliencreation(self, cols, rows): #Creates aliens row by row, with spacing relative to gamescreen's left border.
        x_dist = 30
        y_dist = 30
        for row_index, row in enumerate(range(rows)):
            for col_index, col in enumerate(range(cols)):
                x = col_index * x_dist + self.gamescreen.gamewindow.left + 10
                y = row_index * y_dist + self.gamescreen.gamewindow.top + 10
                if row_index == 0: #Changes alien sprites depending on rows.
                    alien_sprite = Alien('yellow', x, y)
                elif 1 <= row_index <= 2: 
                    alien_sprite = Alien('green', x, y)
                elif 3 <= row_index <= 5:
                    alien_sprite = Alien('red', x, y)
                else:
                    alien_sprite = Alien('yellow', x ,y)
                self.aliens.add(alien_sprite)
    def aliencheckpos(self,leftconstraint,rightconstraint): #Check if touching gamescreen's border and move them down.
        for alien in self.all_aliens:
            if alien.rect.right >= rightconstraint:
                self.alien_direction = -1
                self.alien_move_down(0.5)
            elif alien.rect.left <= leftconstraint:
                self.alien_direction = 1
                self.alien_move_down(0.5)
    def alien_move_down(self, distance): #Moves aliens down.
        if self.aliens:
            for alien in self.aliens.sprites(): 
                alien.pos[1] += distance
    def alien_shoot(self): #Aliens shoot lasers
        if self.aliens.sprites():
            random_alien = random.choice(self.aliens.sprites())
            laser_sprite = AlienLaser(random_alien.rect.center, height)
            self.alien_lasers.add(laser_sprite)
    def collisiondetection(self):
        for laser in self.player.sprite.lasers:
            if not self.gamescreen.gamewindow.contains(laser.rect):
                laser.kill()
            if self.aliens:
                for alien in self.aliens:
                    if alien.mask.overlap(laser.mask,laser.pos - alien.pos):
                        alien.kill()
                        laser.kill()
                        self.gamescreen.score += 20
                    elif pygame.sprite.spritecollide(alien,self.player,False):
                        self.player.sprite.kill()
                        self.gameover()
                    elif alien.pos.y >= self.gamescreen.gamewindow.bottom:
                        self.gameover()
        if not self.aliens:
            self.gameover()
        for alienlaser in self.alien_lasers:
            if pygame.sprite.spritecollide(alienlaser,self.player,False):
                alienlaser.kill()
                self.player.sprite.kill()
                self.gameover()
    def gameover(self):
        gameover = GameOver(self.screen,self.width,self.height,self.gamescreen.score)
        gameover.draw()
        global gameoverstate 
        gameoverstate = True
        global running
        running = False
    def run(self): #Run Object, player,alien each update using each of the sprite update and draw functions.
        if running:
            self.player.update(self.gamescreen.gamewindow.left,self.gamescreen.gamewindow.right)
            self.aliens.update(self.alien_direction)
            self.aliencheckpos(self.gamescreen.gamewindow.left,self.gamescreen.gamewindow.right)
            #self.alien_shoot()
            self.alien_lasers.update()
            displayscreen.fill("black")
            self.player.draw(displayscreen)
            self.player.sprite.lasers.draw(displayscreen)
            self.gamescreen.draw()
            displayscreen.set_at((self.player.sprite.checker),"red") #For Testing Purposes
            self.aliens.draw(displayscreen)
            self.alien_lasers.draw(displayscreen)
            self.collisiondetection()
        else:
            return False
if __name__ == "__main__":
    pygame.init() # Pygame Initialisation and base variable's definitions.
    width=1280
    height=720
    base_width = 1280
    base_height = 720
    background = pygame.image.load('./assets/background.jpg') #Loading the background images.
    background = pygame.transform.scale(background, (width, height))
    screen = pygame.display.set_mode((width,height),pygame.RESIZABLE) #Making the main screen.
    displayscreen = screen.copy() #Make a fakescreen to draw all objects onto so can resize this whole screen when a resize occurs.
    pygame.display.set_caption("PROJ")
    pygame.font.init()
    alaser = pygame.USEREVENT + 1
    pygame.time.set_timer(alaser,400)
    mainmenu = Menu(width,height,screen) #Constructs objects for the main menu and the pause menu.
    pausemenu = PauseMenu(displayscreen,width,height)
    pausestate = False
    running = False
    gameoverstate = False
    clock = pygame.time.Clock()
    while True:
        if running == False and pausestate == False: #Creates a new game if in main menu.
            game = Game(base_width,base_height,displayscreen)
        keys = pygame.key.get_pressed() #Gets key's pressed each iteration.
        for event in pygame.event.get(): #Check events one by one
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE: #Upon resize, sets width and height but doesn't let window be smaller than 800 x 600 for better usability.
                new_width = max(800,event.size[0])
                new_height = max(600,event.size[1])
                screen = pygame.display.set_mode((new_width,new_height),pygame.RESIZABLE)
                width,height = screen.get_width(),screen.get_height()
                game.width, game.height = width,height
                # changed this as would make gamescreen be scaled twice.
            elif event.type == pygame.KEYDOWN: #Key Checks
                if event.key == pygame.K_k:
                    mainmenu.change(True)
                elif event.key == pygame.K_i:
                    mainmenu.change(False)
                elif event.key == pygame.K_RETURN and mainmenu.index == 0 and not pausestate and not gameoverstate:
                    running = True
                elif event.key == pygame.K_RETURN and (pausestate or gameoverstate): #Pause Menu key checks
                    running = False
                    pausestate = False
                    gameoverstate = False
                elif event.key == pygame.K_p and pausestate:
                    running = True
                    pausestate = False
                elif event.key == pygame.K_ESCAPE:
                    running = False
                elif running and event.key == pygame.K_p: #Draw pause menu.
                    pausestate = True
                    running = False
                    if pausestate:
                        pausemenu.draw()
            elif event.type == alaser:
                game.alien_shoot()
        if running and not pausestate: #Run game each frame.
            game.run()
        screen.blit(pygame.transform.scale(displayscreen,(screen.get_width(),screen.get_height())),(0,0)) #Scales fakesceen correctly.
        if not running and not pausestate and not gameoverstate:
            background = pygame.transform.scale(background, (width, height)) #Scales the background correctly.
            screen.blit(background, (0,0))
            mainmenu.draw() #Draws the menu.
        pygame.display.update() #Updates all display changes
        clock.tick(60) #Sets the FPS to 60