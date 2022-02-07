# Main file
import pygame
import random
from Model.Fruit import Fruit
from Model.Point import Point
#from Model.Player import Player


pygame.init()

WIN_WIDTH, WIN_HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

#write this in the loop

#player = Player("Gab", 3, Point(100, 100))

x = random.randint(0, 780)
y = random.randint(0, 580)
fruit = Fruit("fruit", 1, Point(x, y))
fruit.drawfruit(WIN)
pygame.display.update()

time_Before = pygame.time.get_ticks()

if __name__ == '__main__':

    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        time = pygame.time.get_ticks() - time_Before
        print(time)
        if time > 2000:
            x = random.randint(0, 780)
            y = random.randint(0, 580)
            fruit = Fruit("fruit", 1, Point(x, y))
            fruit.drawfruit(WIN)
            pygame.display.update()
            time_Before = pygame.time.get_ticks()

        pygame.display.update()
