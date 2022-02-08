import math
import random

import pygame

from Model.Point import Point

# Sprites
slime_sprites = []
for i in range(1, 3):
    slime_sprites.append(pygame.image.load('img/slime/slime_move_' + str(i) + '.png'))
    slime_sprites[i - 1] = pygame.transform.scale(slime_sprites[i - 1], (48, 32))  # 24 16


class Enemy:
    SLIME = 1
    timer = 20
    @staticmethod
    def randomEnemySpawn(window, enemiesList):
        Enemy.timer -= 0.1
        if Enemy.timer <= 0:
            x = -48
            y = -32
            side = random.randint(0,4)
            if side >= 3: # Spawn on top
                x = random.randint(0, 1024)
            elif side >= 2: # spawn on bottom
                x = random.randint(0, 1024)
                y = 710
            elif side >= 1: # spawn on left
                y = random.randint(0, 678)
            else: # spawn on right
                x = 1072
                y = random.randint(0, 678)
            Enemy.timer = random.random() * 20
            enemiesList.append(Enemy(1, random.random() * 3, Enemy.SLIME, Point(x, y), Point(512, 384), 10))



    def __init__(self, hp, moveSpeed, type, point: Point, target: Point, damages):
        self.hp = hp
        self.moveSpeed = moveSpeed
        if type == Enemy.SLIME:
            self.sprites = slime_sprites
        self.point = point
        self.target = target
        self.angle = math.atan2(target.y - point.y, target.x - point.x)
        self.xVel = math.cos(self.angle) * self.moveSpeed
        self.yVel = math.sin(self.angle) * self.moveSpeed
        self.currentSprite = self.sprites[0]
        self.spriteCounter = 0
        self.damages = damages

    def getDamages(self) -> int:
        return self.damages

    def setDamages(self, damages):
        self.damages = damages

    def draw(self, window):
        self.animate()
        self.point.x += self.xVel
        self.point.y += self.yVel
        window.blit(self.currentSprite, (self.point.x, self.point.y))

    def inHitBox(self, point: Point) -> bool:
        if self.point.getx() <= point.getx() <= self.point.getx() + 48 \
                and self.point.gety() <= point.gety() <= self.point.gety() + 32:
            return True
        else:
            return False

    def inHitBoxBullet(self, point: Point) -> bool:
        point2 = Point(point.getx() + 10, point.gety())
        point3 = Point(point.getx(), point.gety() + 10)
        point4 = Point(point.getx() + 10, point.gety() + 10)

        if self.inHitBox(point) or self.inHitBox(point2) or self.inHitBox(point3) or self.inHitBox(point4):
            return True
        else:
            return False

    def animate(self):
        self.currentSprite = self.sprites[int(self.spriteCounter)]
        self.spriteCounter += 0.1
        if self.spriteCounter >= len(self.sprites):
            self.spriteCounter = 0
