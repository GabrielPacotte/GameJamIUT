# Main file
import pygame
from Model.Player import Player
#from Model.Point import Point
from Model.Point import Point

pygame.init()

WIN_WIDTH, WIN_HEIGHT = 800, 600

WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

player = Player("Gab", 2, Point(100, 100))

if __name__ == '__main__':

    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        player.drawPlayer(WIN)
        player.point.x += 1
        pygame.display.update()
