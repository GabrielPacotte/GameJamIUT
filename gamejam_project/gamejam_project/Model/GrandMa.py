import pygame
import random
from Model.Point import Point


class GrandMa:

    def __init__(self, name, life, point: Point):
        self.name = name
        self.life = life
        self.point = point

    def getName(self) -> str:
        return self.name

    def getLife(self) -> str:
        return self.life

    def setenergy(self, valeur):
        self.life = valeur

    def getPoint(self) -> Point:
        return self.point

    def inHitBox(self, point: Point) -> bool:
        if self.getpoint().getx() <= point.getx() <= self.getpoint().getx() + 100 and self.getpoint().gety() <= point.gety() <= self.getpoint().gety() + 100:
            return True
        else:
            return False

    def drawGrandma(self, window):
        MONSTRE_IMG = pygame.image.load("img/grandma.png")
        MONSTRE_IMG = pygame.transform.scale(MONSTRE_IMG, (100, 100))
        window.blit(MONSTRE_IMG, (self.point.x, self.point.y))