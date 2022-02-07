# Main file
import pygame
from Model.Player import Player
#from Model.Point import Point
from Model.Point import Point

pygame.init()

WIN_WIDTH, WIN_HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

player = Player("Gab", 3, Point(100, 100))

if __name__ == '__main__':

    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        player.move()

        WIN.fill((255, 255, 255))
        player.draw(WIN)
        #player.point.x += 1
        pygame.display.update()
        pygame.event.pump()
