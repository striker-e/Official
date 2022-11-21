import pygame
from player import Player
from gamescreen import GameScreen
class Game:
    def __init__(self,screen,width,height):
        self.screen = screen
        self.width = width
        self.height = height
        self.gamescreen = GameScreen(self.screen, self.width, self.height)
    def run(self):
        self.gamescreen.draw()
        self.pos = self.gamescreen.gamewindow.midbottom
        self.player = Player(self.pos)
        self.player = pygame.sprite.GroupSingle(self.player)
        self.player.draw(self.screen)