import pygame
from Model.Point import Point

PLAYER_IMG = pygame.image.load("img/player.png")
PLAYER_IMG = pygame.transform.scale(PLAYER_IMG, (50, 70))

class Player:

    def __init__(self, name, moveSpeed, point: Point):
        self.name = name
        self.moveSpeed = moveSpeed
        self.point = point

    def move(self):
        keys = pygame.key.get_pressed()
        self.point.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * self.moveSpeed
        self.point.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * self.moveSpeed


    def draw(self, window):
        window.blit(PLAYER_IMG, (self.point.x, self.point.y))