# Main file
import random

import pygame

from Model.Bullet import Bullet
from Model.Enemy import Enemy
from Model.Player import Player
from Model.Point import Point
from Model.fruit import Fruit
from Model.GrandMa import GrandMa
from Model.Cycle import Cycle

pygame.init()
pygame.mixer.init()

# Window settings
WIN_WIDTH, WIN_HEIGHT = 1024, 768
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
CURSOR = pygame.image.load("img/cursor.png")
pygame.mouse.set_visible(False)  # hide the cursor

# cycle
cycle = Cycle(True, False)
time_cycle_before = pygame.time.get_ticks()
time_cycle = pygame.time.get_ticks()

# Images
grass_img = pygame.image.load("img/grass.png")

# First instances
player = Player("Gab", 3, Point(100, 100), [])
grandma = GrandMa("mamie", 100, Point(470, 334))
# Fruits
time_Before = pygame.time.get_ticks()
newFruitX = random.randint(0, 1004)
newFruitY = random.randint(0, 748)
fruits = [Fruit("fruit", 1, Point(newFruitX, newFruitY))]

# Balles

bullets = []

# Enemies

enemies = []

# nbFruits
nbBanana = 0
nbApple = 0
nbLemon = 0

# sound
music_theme = pygame.mixer.Sound("sound/theme.ogg")
music_theme.set_volume(0.5)
music_quest = pygame.mixer.Sound("sound/quest.ogg")
sound_1 = pygame.mixer.Sound("sound/briut1.ogg")
sound_kalash = pygame.mixer.Sound("sound/bruit_kalash.ogg")
sound_fruits = pygame.mixer.Sound("sound/bruit_fruit.ogg")
sound_grandma = pygame.mixer.Sound("sound/bruit_grandmere.mp3")
sound_end = pygame.mixer.Sound("sound/bruit_fin.mp3")
sound_enemy = pygame.mixer.Sound("sound/bruit_ennemi.mp3")
sound_night = pygame.mixer.Sound("sound/bruit_nuit.wav")
sound_day = pygame.mixer.Sound("sound/bruit_jour.wav")

darkness = 0

def animCycleAnouncement(imgName):
    night_img = pygame.image.load(imgName)
    pygame.image.save(WIN, 'img/temp.png')
    temp = pygame.image.load('img/temp.png')
    x = -1024
    while x < 1024:
        # Draw the world
        WIN.blit(temp, (0, 0))
        WIN.blit(night_img, (x, 0))
        pygame.display.update()
        x += 5


if __name__ == '__main__':

    clock = pygame.time.Clock()
    score = 0
    perdu = False
    compteur_cycle = 1
    restart = True
    waitUserResponse = True
    timer = 0
    running = True
    while running:
        while waitUserResponse:
            music_theme.play(loops=-1, maxtime=0, fade_ms=0)
            WIN.fill((0, 0, 0))
            if int(timer) % 2 == 1:
                font = pygame.font.Font('fonts/dogica.ttf', 10)
                text_play_again = font.render("Press ENTER to play", 1, (255, 255, 255))
                text_quit = font.render("Press DEL to exit", 1, (255, 255, 255))
                WIN.blit(text_play_again, (420, 350))
                WIN.blit(text_quit, (430, 380))
            timer += 0.005
            pygame.display.update()
            keys = pygame.key.get_pressed()
            pygame.display.flip()
            pygame.event.pump()
            if keys[pygame.K_RETURN]:
                waitUserResponse = False
                restart = True
                timer = 0
            if keys[pygame.K_BACKSPACE]:
                waitUserResponse = False
                restart = False
                running = False
        while restart:
            music_theme.stop()
            music_quest.play(loops=-1, maxtime=0, fade_ms=0)
            time_cycle_before = pygame.time.get_ticks()
            time_cycle = pygame.time.get_ticks()
            while not perdu:
                dt = clock.tick(60)
                time = pygame.time.get_ticks() - time_Before
                # Update player position
                player.move(dt)
                # NIGHT'S CYCLE ------------------------------------------------------------------------------------------------
                if cycle.getCycle() == "night":

                    Enemy.randomEnemySpawn(WIN, enemies, compteur_cycle)
                    time_cycle = pygame.time.get_ticks() - time_cycle_before
                    if time_cycle > 20000:
                        time_cycle_before = pygame.time.get_ticks()
                        cycle.cycleChange()
                        compteur_cycle = compteur_cycle + 1
                        sound_day.play()
                        animCycleAnouncement('img/day.png')

                    font = pygame.font.Font('fonts/dogica.ttf', 10)
                    text = font.render("nuit " + str(compteur_cycle), 1, (255, 255, 255))
                    WIN.blit(text, (10, 30))

                # DAY'S CYCLE --------------------------------------------------------------------------------------------------
                if cycle.getCycle() == "day":
                    # Create new fruits
                    if time > 2000:
                        fruits.append(Fruit("fruit", 1, Point(random.randint(0, 1004), random.randint(0, 748))))
                        time_Before = pygame.time.get_ticks()
                    time_cycle = pygame.time.get_ticks() - time_cycle_before
                    if time_cycle > 20000:
                        time_cycle_before = pygame.time.get_ticks()
                        cycle.cycleChange()
                        sound_night.play()
                        animCycleAnouncement('img/night.png')
                    font = pygame.font.Font('fonts/dogica.ttf', 10)
                    text = font.render("jour " + str(compteur_cycle), 1, (255, 255, 255))
                    WIN.blit(text, (10, 30))

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            bullets.append(Bullet(Point(player.point.x + 21, player.point.y + 31),
                                                  Point(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])))
                            sound_kalash.play()

                # Draw the window
                WIN.blit(grass_img, (0, 0))
                WIN.blit(text, (10, 30))
                for fruit in fruits:
                    fruit.drawFruit(WIN)

                # Draw reverse grandma if you shot her with bullet
                if not perdu:
                    grandma.drawGrandma(WIN, False)
                else:
                    grandma.drawGrandma(WIN, True)

                # Grandma's Life bar
                pygame.draw.rect(WIN, (255, 255, 255), pygame.Rect(450, 314, 100, 10))
                if not perdu:
                    if grandma.getLife() > 200:
                        grandma.setLife(200)
                    pygame.draw.rect(WIN, (0, 255, 0), pygame.Rect(450, 314, grandma.getLife() / 2, 10))
                else:
                    pygame.draw.rect(WIN, (255, 0, 0), pygame.Rect(450, 314, 100, 10))

                # draw enemies
                for enemy in enemies:
                    for bullet in bullets:
                        if enemy in enemies and enemy.inHitBoxBullet(bullet.point):
                            enemies.remove(enemy)
                            bullets.remove(bullet)
                            score += 1
                            sound_enemy.play()
                    if enemy in enemies and grandma.inHitBoxEnemy(enemy.point):
                        enemies.remove(enemy)
                        grandma.setLife(grandma.getLife() - 10)
                        sound_1.play()
                    enemy.draw(WIN)

                for bullet in bullets:
                    bullet.draw(WIN)
                    if bullet.lifetime <= 0:
                        bullets.pop(bullets.index(bullet))

                    if grandma.inHitBoxBullet(bullet.point):
                        grandma.drawGrandma(WIN, False)
                        bullets.remove(bullet)
                        grandma.setLife(grandma.getLife() - 10)
                        sound_1.play()

                if grandma.getLife() <= 0:
                    perdu = True
                    sound_end.play()

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
                            sound_fruits.play()
                        else:
                            fruit.drawFruit(WIN)
                    elif fruit.inHitBoxGrandma(grandma.point):
                        fruits.remove(fruit)

                # Feed the gandma
                if grandma.inHitBoxPlayer(player.point):
                    count = 0
                    if len(player.inventory) != 0:
                        sound_grandma.play()
                    for fruit in player.inventory:
                        count = count + fruit.getEnergy()
                        score = score + fruit.getEnergy()
                    player.inventory.clear()
                    grandma.setLife(grandma.getLife() + count)
                    nbBanana = 0
                    nbApple = 0
                    nbLemon = 0

                # Printing score and inventory
                font = pygame.font.Font('fonts/dogica.ttf', 10)
                text = font.render(
                    "score : " + str(score) + " | banana : " + str(nbBanana) + " | Apple : " + str(nbApple) + " | Lemon : "
                    + str(nbLemon), 1, (255, 255, 255))
                WIN.blit(text, (10, 10))

                if cycle.getCycle() == "night":
                    if darkness < 100:
                        darkness += 1
                    PURPLE = (255, 0, 255)
                    purple_image = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
                    purple_image.set_alpha(darkness)
                    WIN.blit(purple_image, (0, 0))
                else:  # cycle = day
                    if darkness > 0:
                        darkness -= 1
                        PURPLE = (255, 0, 255)
                        purple_image = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
                        purple_image.set_alpha(darkness)
                        WIN.blit(purple_image, (0, 0))

                coord = pygame.mouse.get_pos()
                WIN.blit(CURSOR, coord)
                pygame.display.flip()
                pygame.display.update()
                pygame.event.pump()

            while perdu:
                music_quest.stop()
                WIN.blit(grass_img, (0, 0))

                for fruit in fruits:
                    fruit.drawFruit(WIN)

                grandma.drawGrandma(WIN, True)

                pygame.draw.rect(WIN, (255, 0, 0), pygame.Rect(450, 314, 100, 10))

                font = pygame.font.Font('fonts/dogica.ttf', 100)
                text = font.render("GAME OVER", 1, (255, 255, 255))
                font = pygame.font.Font('fonts/dogica.ttf', 20)
                text_score = font.render("Score: " + str(score), 1, (255, 255, 255))
                font = pygame.font.Font('fonts/dogica.ttf', 10)
                text_play_again = font.render("Press r to play again", 1, (255, 255, 255))
                text_quit = font.render("Press e to menu", 1, (255, 255, 255))

                WIN.blit(text, (80, 150))
                WIN.blit(text_score, (420, 460))
                if int(timer) % 2 == 1:
                    WIN.blit(text_play_again, (400, 500))
                    WIN.blit(text_quit, (430, 520))
                timer += 0.05

                keys = pygame.key.get_pressed()
                if keys[pygame.K_r]:  # r pressed (for restart)
                    perdu = False
                    restart = True
                    grandma.setLife(100)
                    score = 0
                    compteur_cycle = 1
                    time_cycle_before = pygame.time.get_ticks()
                    time_cycle = pygame.time.get_ticks()
                    time_Before = pygame.time.get_ticks()
                    nbBanana = 0
                    nbApple = 0
                    nbLemon = 0
                    darkness = 0
                    player.inventory.clear()
                    enemies.clear()
                    fruits.clear()
                    bullets.clear()
                    cycle.day = True
                    cycle.night = False
                    player.setPoint(Point(100,100))

                if keys[pygame.K_e]:  # q pressed (for exit)
                    perdu = False
                    restart = False
                    waitUserResponse = True
                    grandma.setLife(100)
                    score = 0
                    compteur_cycle = 1
                    time_cycle_before = pygame.time.get_ticks()
                    time_cycle = pygame.time.get_ticks()
                    time_Before = pygame.time.get_ticks()
                    nbBanana = 0
                    nbApple = 0
                    nbLemon = 0
                    darkness = 0
                    player.inventory.clear()
                    enemies.clear()
                    fruits.clear()
                    bullets.clear()
                    cycle.day = True
                    cycle.night = False
                    player.setPoint(Point(100,100))

                pygame.display.update()
                pygame.event.pump()
