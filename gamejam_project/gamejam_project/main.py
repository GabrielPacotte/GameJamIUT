# Main file
import random

import pygame
from Model.Player import Player
from Model.Point import Point
from Model.fruit import Fruit

pygame.init()

# Window settings
WIN_WIDTH, WIN_HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
CURSOR = pygame.image.load("img/cursor.png")
pygame.mouse.set_visible(False)  # hide the cursor

# First instances
player = Player("Gab", 3, Point(100, 100))

# Fruits
time_Before = pygame.time.get_ticks()

newFruitX = random.randint(0, 780)
newFruitY = random.randint(0, 580)
fruits = [Fruit("fruit", 1, Point(newFruitX, newFruitY))]

if __name__ == '__main__':

    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        time = pygame.time.get_ticks() - time_Before
        # Update objects position
        player.move()

        # Draw the window
        WIN.fill((0, 0, 0))

        player.draw(WIN)
        for fruit in fruits:
            fruit.drawFruit(WIN)
        coord = pygame.mouse.get_pos()
        WIN.blit(CURSOR, coord)
        pygame.display.update()
        pygame.event.pump()
