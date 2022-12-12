import pygame, sys
from menu import Menu
from gamescreen import GameScreen
from player import Player
from alien import Alien
from laser import Laser, AlienLaser
from pausemenu import PauseMenu
from gameover import GameOver
from optionsmenu import OptionsMenu
from text import Text
import random
class Game:
    #Game Class Constructor,Creates Gamescreen with the initial resolution and positions it correctly, creates only one player object. Creates aliens once.
    def __init__(self,width,height,screen,option = False):
        self.option = option
        self.screen = screen
        self.width = width
        self.height = height
        self.gamescreen = GameScreen(displayscreen, self.width, self.height)
        self.gameover = GameOver(self.screen,self.width,self.height)
        self.pos = self.gamescreen.gamewindow.midbottom
        self.normalkeys = [pygame.K_RIGHT,pygame.K_LEFT,pygame.K_UP,pygame.K_DOWN,pygame.K_SPACE]
        if self.option:
            self.gamescreen = GameScreen(displayscreen,self.width,self.height,1)
            self.pos = self.gamescreen.gamewindow.midbottom
            keys = [pygame.K_d,pygame.K_a,pygame.K_w,pygame.K_s,pygame.K_SPACE]
            self.playersprite2 = Player((self.pos[0] + 100,self.pos[1]),"red",keys)
            self.player2 = pygame.sprite.GroupSingle(self.playersprite2)
            keyset2 = [pygame.K_RIGHT,pygame.K_LEFT,pygame.K_UP,pygame.K_DOWN,pygame.K_KP_ENTER]
            self.playersprite = Player(self.pos,"blue",keyset2)
            self.player = pygame.sprite.GroupSingle(self.playersprite)
        elif not self.option:
            self.playersprite = Player(self.pos,"blue",self.normalkeys)
            self.player = pygame.sprite.GroupSingle(self.playersprite)
        self.aliens = pygame.sprite.Group()
        if self.option:
            self.aliencreation(rows = 9,cols=30)
        elif not self.option:
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
                        self.gameover.val = False
                        self.gameend()
                    # elif alien.pos.y >= self.gamescreen.gamewindow.bottom:
                    #     self.gameend(False)
        if self.option:
            for laser in self.player2.sprite.lasers:
                if not self.gamescreen.gamewindow.contains(laser.rect):
                    laser.kill()
                if self.aliens:
                    for alien in self.aliens:
                        if alien.mask.overlap(laser.mask,laser.pos - alien.pos):
                            alien.kill()
                            laser.kill()
                            self.gamescreen.score += 20
                        elif pygame.sprite.spritecollide(alien,self.player,False):
                            self.player2.sprite.kill()
                            self.gameover.val = False
                            self.gameend()
                        # elif alien.pos.y >= self.gamescreen.gamewindow.bottom:
                        # self.gameend(False)
        if not self.aliens:
            self.gameover.val = 2
            self.gameend()
        for alienlaser in self.alien_lasers:
            if pygame.sprite.spritecollide(alienlaser,self.player,False):
                alienlaser.kill()
                self.player.sprite.kill()
                self.gameover.val = False
                self.gameend()
            elif self.option and pygame.sprite.spritecollide(alienlaser,self.player2,False):
                alienlaser.kill()
                self.player2.sprite.kill()
                self.gameover.val = True
                self.gameend()
    def gameend(self):
        self.gameover.draw(self.gamescreen.score)
        global gameoverstate 
        gameoverstate = True
        global running
        running = False
        global coopmode
        coopmode = False
        global value
    def run(self): #Run Object, player,alien each update using each of the sprite update and draw functions.
        if running:
            self.player.update(self.gamescreen.gamewindow.left,self.gamescreen.gamewindow.right)
            if self.option:
                self.player2.update(self.gamescreen.gamewindow.left,self.gamescreen.gamewindow.right)
            self.aliens.update(self.alien_direction)
            self.aliencheckpos(self.gamescreen.gamewindow.left,self.gamescreen.gamewindow.right)
            #self.alien_shoot()
            self.alien_lasers.update()
            displayscreen.fill("black")
            self.player.draw(displayscreen)
            self.player.sprite.lasers.draw(displayscreen)
            if self.option:
                self.player2.draw(displayscreen)
                self.player2.sprite.lasers.draw(displayscreen)
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
    ticks = 400
    mainmenu = Menu(width,height,screen) #Constructs objects for the main menu and the pause menu.
    pausemenu = PauseMenu(displayscreen,width,height)
    optionsmenu = OptionsMenu(displayscreen,width,height)
    pausestate = False
    running = False
    gameoverstate = False
    optionsstate = False
    firsttime = True
    coopmode = False
    clock = pygame.time.Clock()
    while True:
        if not running and not pausestate and not gameoverstate and not optionsstate: #Creates a new game if in main menu.
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
                if event.key == pygame.K_DOWN and not gameoverstate and not running and not optionsstate:
                    mainmenu.change(True)
                elif event.key == pygame.K_UP and not gameoverstate and not running and not optionsstate:
                    mainmenu.change(False)
                elif event.key == pygame.K_RETURN and not pausestate and not gameoverstate and not optionsstate:
                    match mainmenu.index:
                        case 0:
                            running = True
                            pygame.time.set_timer(alaser,400)
                        case 3:
                            optionsstate = True
                        case 1:
                            coopmode = True
                            running = True
                            game = Game(base_width,base_height,displayscreen,True)
                            pygame.time.set_timer(alaser,250)
                elif event.key == pygame.K_TAB and (pausestate or gameoverstate or optionsstate): #Pause Menu key checks
                    running = False
                    pausestate = False
                    gameoverstate = False
                    optionsstate = False
                    firsttime = True
                    coopmode = False
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
                elif gameoverstate:
                    if event.key == pygame.K_BACKSPACE:
                        game.gameover.username = game.gameover.username[0:-1]
                    elif event.key == pygame.K_RETURN:
                        if len(game.gameover.username):
                            game.gameover.savefunction(game.gamescreen.score)
                            gameoverstate = False
                    elif len(game.gameover.username) <= 2:
                        game.gameover.username += event.unicode
                elif optionsstate:
                    if event.key == pygame.K_DOWN:
                        optionsmenu.onestate = not optionsmenu.onestate
                    elif event.key == pygame.K_RETURN and optionsmenu.onestate:
                        game.gameover.deletehighscores()
                        optionsmenu.onestate = not optionsmenu.onestate
            elif event.type == alaser and running:
                game.alien_shoot()
        if gameoverstate:
            game.gameover.draw(game.gamescreen.score)
        elif optionsstate:
            optionsmenu.draw()
            list = game.gameover.topfive() #[score:username\n,score:username\n]
            yvalues = [height * 0.30,height * 0.40,height*0.50,height*0.60,height*0.70]
            highscore = Text("Highscores Below",(width * 0.80,height * 0.20),displayscreen,"red",1,24)
            highscore.draw()
            for i in range(len(list)):
                text = Text(list[i].split(":")[0] + " " + (list[i].split(":")[1]).split("\n")[0],(width * 0.80,yvalues[i]),displayscreen,"blue",1,32)
                text.draw()
        elif running and not pausestate: #Run game each frame.
            game.run()
        elif running:
            #Run server communication exchanges before game.onlinerun()
            game.onlinerun() #Pass something in to online run, such as player position and update it before drawing.
        screen.blit(pygame.transform.scale(displayscreen,(screen.get_width(),screen.get_height())),(0,0)) #Scales fakesceen correctly.
        if not running and not pausestate and not gameoverstate and not optionsstate:
            background = pygame.transform.scale(background, (width, height)) #Scales the background correctly.
            screen.blit(background, (0,0))
            mainmenu.draw() #Draws the menu.
        pygame.display.update() #Updates all display changes
        clock.tick(60) #Sets the FPS to 60