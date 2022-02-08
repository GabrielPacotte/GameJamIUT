# Main file
import random

import pygame

from Model.Bullet import Bullet
from Model.Enemy import Enemy
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
player = Player("Gab", 3, Point(100, 100), [])
grandma = GrandMa("mamie", 100, Point(325, 225))
# Fruits
time_Before = pygame.time.get_ticks()

newFruitX = random.randint(0, 780)
newFruitY = random.randint(0, 580)
fruits = [Fruit("fruit", 1, Point(newFruitX, newFruitY))]

# Balles

bullets = []

# Enemies

enemies = [Enemy(1, 1, Enemy.SLIME, Point(0,0), Point(400, 300))]

#nbFruits
nbBanana = 0
nbApple = 0
nbLemon = 0

def drawGrass():
    for i in range(0, 475):
        x = i % 25
        y = (i - x) / 25
        WIN.blit(grass_img, (x * 32, y * 32))


if __name__ == '__main__':

    clock = pygame.time.Clock()
    score = 0
    perdu = False
    while True:
        clock.tick(60)
        time = pygame.time.get_ticks() - time_Before
        # Update player position
        player.move()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    bullets.append(Bullet(Point(player.point.x + 21, player.point.y + 31),
                                          Point(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])))
        # Create new fruits
        if time > 2000:
            fruits.append(Fruit("fruit", 1, Point(random.randint(0, 780), random.randint(0, 580))))
            time_Before = pygame.time.get_ticks()

        # Draw the window
        drawGrass()

        for fruit in fruits:
            fruit.drawFruit(WIN)

        # Draw reverse grandma if you shot her with bullet
        if not perdu:
            grandma.drawGrandma(WIN, False)
        else:
            grandma.drawGrandma(WIN, True)

        # Grandma's Life bar
        pygame.draw.rect(WIN, (255, 255, 255), pygame.Rect(325, 200, 100, 10))
        if not perdu:
            if grandma.getLife() > 200:
                grandma.setLife(200)
            pygame.draw.rect(WIN, (0, 255, 0), pygame.Rect(325, 200, grandma.getLife()/2, 10))
        else:
            pygame.draw.rect(WIN, (255, 0, 0), pygame.Rect(325, 200, 100, 10))

        # draw enemies
        for enemy in enemies:
            enemy.draw(WIN)

        for bullet in bullets:
            bullet.draw(WIN)
            if bullet.lifetime <= 0:
                bullets.pop(bullets.index(bullet))

            if grandma.inHitBoxBullet(bullet.point):
                grandma.drawGrandma(WIN, True)
                perdu = True

        player.draw(WIN)
        for fruit in fruits:
            if fruit.inHitBoxPlayer(player.point):
                if player.addFruit(fruit):
                    if fruit.name == "banana":
                        nbBanana = nbBanana + 1
                    elif fruit.name == "lemon":
                        nbLemon = nbLemon + 1
                    else:
                        nbApple = nbApple + 1
                    fruits.remove(fruit)
                else:
                    fruit.drawFruit(WIN)
            elif fruit.inHitBoxGrandma(grandma.point):
                fruits.remove(fruit)
            else:
                fruit.drawFruit(WIN)

        # Feed the gandma
        if grandma.inHitBoxPlayer(player.point):
            count = 0
            for fruit in player.inventory:
                count = count + fruit.getEnergy()
                score = score + fruit.getEnergy()
            player.inventory.clear()
            grandma.setLife(grandma.getLife() + count)
            nbBanana = 0
            nbApple = 0
            nbLemon = 0

        # Printing score and inventory
        font = pygame.font.Font(None, 24)
        text = font.render("score : " + str(score)+" | banana : "+str(nbBanana)+" | Apple : "+str(nbApple)+" | Lemon : "
                           + str(nbLemon), 1, (255, 255, 255))
        WIN.blit(text, (10, 10))

        coord = pygame.mouse.get_pos()
        WIN.blit(CURSOR, coord)
        pygame.display.update()
        pygame.event.pump()
