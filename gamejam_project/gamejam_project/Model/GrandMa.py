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
        if self.getPoint().getx() <= point.getx() <= self.getPoint().getx() + 100 \
                and self.getPoint().gety() <= point.gety() <= self.getPoint().gety() + 100:
            return True
        else:
            return False

    def inHitBoxBullet(self, point: Point) -> bool:
        point2 = Point(point.getx()+10, point.gety())
        point3 = Point(point.getx(), point.gety()+10)
        point4 = Point(point.getx()+10, point.gety()+10)

        if self.inHitBox(point) or self.inHitBox(point2) or self.inHitBox(point3) or self.inHitBox(point4):
            return True
        else:
            return False

    def drawGrandma(self, window, bool):
        GRANDMA_IMG = pygame.image.load("img/grandma.png")
        GRANDMA_IMG = pygame.transform.scale(GRANDMA_IMG, (100, 100))
        if bool:
            GRANDMA_IMG = pygame.transform.flip(GRANDMA_IMG, True, True)

        window.blit(GRANDMA_IMG, (self.point.x, self.point.y))
