import pygame
from Model.Point import Point
from Model.fruit import Fruit

# ------------------------------------------------------------------------
# LOAD ALL SPRITES FOR ANIMATIONS
# ------------------------------------------------------------------------

moveDownSprites = []
moveUpSprites = []
moveRightSprites = []
moveLeftSprites = []

for i in range(1, 6):
    moveDownSprites.append(pygame.image.load("img/player_move_down/player_move_down_" + str(i) + ".png"))
    moveDownSprites[i - 1] = pygame.transform.scale(moveDownSprites[i - 1], (42, 63))

for i in range(1, 6):
    moveUpSprites.append(pygame.image.load("img/player_move_up/player_move_up_" + str(i) + ".png"))
    moveUpSprites[i - 1] = pygame.transform.scale(moveUpSprites[i - 1], (42, 63))

for i in range(1, 6):
    moveRightSprites.append(pygame.image.load("img/player_move_right/player_move_right_" + str(i) + ".png"))
    moveRightSprites[i - 1] = pygame.transform.scale(moveRightSprites[i - 1], (42, 63))

for i in range(1, 6):
    moveLeftSprites.append(pygame.image.load("img/player_move_left/player_move_left_" + str(i) + ".png"))
    moveLeftSprites[i - 1] = pygame.transform.scale(moveLeftSprites[i - 1], (42, 63))


# ------------------------------------------------------------------------
# CLASS PLAYER
# ------------------------------------------------------------------------

class Player:

    def __init__(self, name, moveSpeed, point: Point, inventory):
        self.name = name
        self.moveSpeed = moveSpeed
        self.point = point
        self.currentSprite = 0
        self.player_img = moveDownSprites[0]
        self.inventory = []

    # Used to move the player thanks to arrow keys
    def move(self):
        keys = pygame.key.get_pressed()
        xMovement = (keys[pygame.K_d] - keys[pygame.K_q]) * self.moveSpeed
        yMovement = (keys[pygame.K_s] - keys[pygame.K_z]) * self.moveSpeed
        if xMovement**2 + yMovement**2 > self.moveSpeed**2:  # Because the player move faster diagonally
            xMovement /= 1.5
            yMovement /= 1.5
        self.point.x += xMovement
        self.point.y += yMovement
        # Constraints on horizontal axis
        if self.point.x >= 1024:
            self.point.x = -42
        elif self.point.x <= -42:
            self.point.x = 1024
        # Constraints on vertical axis
        if self.point.y >= 825:
            self.point.y = -63
        elif self.point.y <= -63:
            self.point.y = 825
        self.animate()

    # Used to animate the player
    def animate(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:  # Animate down movement
            self.player_img = moveDownSprites[int(self.currentSprite)]
            self.currentSprite += 0.2
            if self.currentSprite >= len(moveDownSprites):
                self.currentSprite = 0
        elif keys[pygame.K_z]:  # Animate up movement
            self.player_img = moveUpSprites[int(self.currentSprite)]
            self.currentSprite += 0.2
            if self.currentSprite >= len(moveUpSprites):
                self.currentSprite = 0
        elif keys[pygame.K_q]:  # Animate movement on left
            self.player_img = moveLeftSprites[int(self.currentSprite)]
            self.currentSprite += 0.2
            if self.currentSprite >= len(moveLeftSprites):
                self.currentSprite = 0
        elif keys[pygame.K_d]:  # Animate movement on right
            self.player_img = moveRightSprites[int(self.currentSprite)]
            self.currentSprite += 0.2
            if self.currentSprite >= len(moveRightSprites):
                self.currentSprite = 0
        else:  # Else stay idle
            self.currentSprite = 0
            self.player_img = moveDownSprites[int(self.currentSprite)]

    def addFruit(self, fruit: Fruit) -> bool:
        if len(self.inventory) == 3:
            return False
        else:
            self.inventory.append(fruit)
            return True

    # Used to draw the current image of the player at the right location of the screen
    def draw(self, window):
        window.blit(self.player_img, (self.point.x, self.point.y))
