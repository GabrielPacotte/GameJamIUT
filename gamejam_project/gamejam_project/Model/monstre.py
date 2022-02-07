import pygame
import random
from Model.Point import Point


class Monstre:

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
        if self.getpoint().getx() <= point.getx() <= self.getpoint().getx() + 150 and self.getpoint().gety() <= point.gety() <= self.getpoint().gety() + 150:
            return True
        else:
            return False

    def drawfruit(self, window):
        x = random.randint(0, 10)
        if x <= 5:
            FRUITS_IMG = pygame.image.load("img/citron.png")
            FRUITS_IMG = pygame.transform.scale(FRUITS_IMG, (20, 20))
            self.setenergy(1)
        if 5 < x <= 8:
            FRUITS_IMG = pygame.image.load("img/pomme.png")
            FRUITS_IMG = pygame.transform.scale(FRUITS_IMG, (20, 20))
            self.setenergy(2)
        if x > 8:
            FRUITS_IMG = pygame.image.load("img/banane.png")
            FRUITS_IMG = pygame.transform.scale(FRUITS_IMG, (20, 20))
            self.setenergy(3)

        window.blit(FRUITS_IMG, (self.point.x, self.point.y))



