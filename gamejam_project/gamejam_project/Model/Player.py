import pygame
from Model.Point import Point

moveDownSprites = []
moveUpSprites = []
moveRightSprites = []
moveLeftSprites = []

for i in range(1, 6):
    moveDownSprites.append(pygame.image.load("img/player_move_down/player_move_down_" + str(i) + ".png"))
    moveDownSprites[i-1] = pygame.transform.scale(moveDownSprites[i-1], (42, 63))

for i in range(1, 6):
    moveUpSprites.append(pygame.image.load("img/player_move_up/player_move_up_" + str(i) + ".png"))
    moveUpSprites[i-1] = pygame.transform.scale(moveUpSprites[i-1], (42, 63))

for i in range(1, 6):
    moveRightSprites.append(pygame.image.load("img/player_move_right/player_move_right_" + str(i) + ".png"))
    moveRightSprites[i-1] = pygame.transform.scale(moveRightSprites[i-1], (42, 63))

for i in range(1, 6):
    moveLeftSprites.append(pygame.image.load("img/player_move_left/player_move_left_" + str(i) + ".png"))
    moveLeftSprites[i-1] = pygame.transform.scale(moveLeftSprites[i-1], (42, 63))

#PLAYER_IMG = moveDownSprites[0]

class Player:

    def __init__(self, name, moveSpeed, point: Point):
        self.name = name
        self.moveSpeed = moveSpeed
        self.point = point
        self.currentSprite = 0;
        self.player_img = moveDownSprites[0]

    def move(self):
        keys = pygame.key.get_pressed()
        self.point.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * self.moveSpeed
        self.point.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * self.moveSpeed
        self.animate()

    def animate(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]: # Animate down movement
            self.player_img = moveDownSprites[int(self.currentSprite)]
            self.currentSprite += 0.15
            if self.currentSprite >= len(moveDownSprites):
                self.currentSprite = 0
        elif keys[pygame.K_UP]:  # Animate up movement
            self.player_img = moveUpSprites[int(self.currentSprite)]
            self.currentSprite += 0.15
            if self.currentSprite >= len(moveUpSprites):
                self.currentSprite = 0
        elif keys[pygame.K_LEFT]:
            self.player_img = moveLeftSprites[int(self.currentSprite)]
            self.currentSprite += 0.15
            if self.currentSprite >= len(moveLeftSprites):
                self.currentSprite = 0
        elif keys[pygame.K_RIGHT]:
            self.player_img = moveRightSprites[int(self.currentSprite)]
            self.currentSprite += 0.15
            if self.currentSprite >= len(moveRightSprites):
                self.currentSprite = 0
        else:
            self.currentSprite = 0
            self.player_img = moveDownSprites[int(self.currentSprite)]

    def draw(self, window):
        window.blit(self.player_img, (self.point.x, self.point.y))