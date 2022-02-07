import math

import pygame.draw

from Model import Point


class Bullet:
    def __init__(self, point: Point, mousePos: Point):
        self.point = point
        self.mousePos = mousePos
        self.lifetime = 50
        self.speed = 15
        self.angle = math.atan2(mousePos.y-point.y, mousePos.x-point.x)
        self.xVel = math.cos(self.angle) * self.speed
        self.yVel = math.sin(self.angle) * self.speed
        self.radius = 5

    def draw(self, window):
        self.point.x += int(self.xVel)
        self.point.y += int(self.yVel)

        pygame.draw.circle(window, (255,255,255), (self.point.x, self.point.y), self.radius)
        self.lifetime -= 1