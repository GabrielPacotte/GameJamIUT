import pygame
from Model.Point import Point

PLAYER_IMG = pygame.image.load("img/player.png")
PLAYER_IMG = pygame.transform.scale(PLAYER_IMG, (50, 70))

class Player:

    def __init__(self, name, moveSpeed, point: Point):
        self.name = name
        self.moveSpeed = moveSpeed
        self.point = point



    def drawPlayer(self, window):
        window.blit(PLAYER_IMG, (self.point.x, self.point.y))