# Main file
import pygame
from Model.Point import Point
from Model.Monstre import Monstre


pygame.init()

WIN_WIDTH, WIN_HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

#write this in the loop

#player = Player("Gab", 3, Point(100, 100))
monster = Monstre("monstre", 100, Point(325, 225))

if __name__ == '__main__':

    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        monster.drawMonstre(WIN)
        pygame.display.update()
