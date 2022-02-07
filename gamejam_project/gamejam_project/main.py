# Main file
import random

import pygame

from Model.Bullet import Bullet
from Model.Player import Player
from Model.Point import Point
from Model.fruit import Fruit
from Model.GrandMa import GrandMa
pygame.init()

# Window settings
WIN_WIDTH, WIN_HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
CURSOR = pygame.image.load("img/cursor.png")
pygame.mouse.set_visible(False)  # hide the cursor

# Images
grass_img = pygame.image.load("img/bg_grass.png")

# First instances
player = Player("Gab", 3, Point(100, 100))
grandma = GrandMa("mamie", 100, Point(325,225))
# Fruits
time_Before = pygame.time.get_ticks()

newFruitX = random.randint(0, 780)
newFruitY = random.randint(0, 580)
fruits = [Fruit("fruit", 1, Point(newFruitX, newFruitY))]

# Balles

bullets = [];

def drawGrass():
    for i in range(0, 475):
        x = i % 25
        y = (i - x) / 25
        WIN.blit(grass_img, (x * 32, y * 32))


if __name__ == '__main__':

    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        time = pygame.time.get_ticks() - time_Before
        # Update player position
        player.move()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    bullets.append(Bullet(Point(player.point.x+21, player.point.y+31), Point(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])))
        # Create new fruits
        if time > 2000:
            fruits.append(Fruit("fruit", 1, Point(random.randint(0, 780), random.randint(0, 580))))
            time_Before = pygame.time.get_ticks()

        # Draw the window
        drawGrass()

        for fruit in fruits:
            fruit.drawFruit(WIN)

        for bullet in bullets:
            bullet.draw(WIN)
            if(bullet.lifetime <= 0):
                bullets.pop(bullets.index(bullet))
        player.draw(WIN)
        grandma.drawGrandma(WIN)
        for fruit in fruits:
            if fruit.inHitBoxPlayer(player.point) or fruit.inHitBoxGrandma(grandma.point):
                fruits.remove(fruit)
            else:
                fruit.drawFruit(WIN)
        coord = pygame.mouse.get_pos()
        WIN.blit(CURSOR, coord)
        pygame.display.update()
        pygame.event.pump()
