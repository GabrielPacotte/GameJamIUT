import pygame
import random
from Model.Point import Point


class Fruit:

    def __init__(self, name, energy, point: Point):
        self.name = name
        self.energy = energy
        self.point = point
        x = random.randint(0, 10)
        if x <= 5:
            self.FRUITS_IMG = pygame.image.load("img/fruits/citron.png")
            self.FRUITS_IMG = pygame.transform.scale(self.FRUITS_IMG, (20, 20))
            self.setEnergy(1)
        if 5 < x <= 8:
            self.FRUITS_IMG = pygame.image.load("img/fruits/pomme.png")
            self.FRUITS_IMG = pygame.transform.scale(self.FRUITS_IMG, (20, 20))
            self.setEnergy(2)
        if x > 8:
            self.FRUITS_IMG = pygame.image.load("img/fruits/banane.png")
            self.FRUITS_IMG = pygame.transform.scale(self.FRUITS_IMG, (20, 20))
            self.setEnergy(3)

    def getname(self) -> str:
        return self.name

    def getEnergy(self) -> str:
        return self.energy

    def setEnergy(self, valeur):
        self.energy = valeur

    def getPoint(self) -> Point:
        return self.point

    def inHitBox(self, point: Point) -> bool:
        if self.getpoint().getx() <= point.getx() <= self.getpoint().getx() + 20 and self.getpoint().gety() <= point.gety() <= self.getpoint().gety() + 20:
            return True
        else:
            return False

    def drawFruit(self, window):
        window.blit(self.FRUITS_IMG, (self.point.x, self.point.y))



