import pygame
import math
import random
import time
from pygame import mixer
from time import sleep
from config import *

pygame.init()
pygame.mixer.init()

# Clock
clock = pygame.time.Clock()

# Creating screen
screen = pygame.display.set_mode((screenwidth, screenheight))

# Caption and Icon
pygame.display.set_icon(icon)

# Background Music
mixer.music.load('music.mp3')
mixer.music.play(-1)

# Road
surf = pygame.Surface((800, 30))
surf.fill((150, 75, 0))
rect = surf.get_rect()


def show_score1(x, y):
    score_value = font.render(
        "Score 1 is " + str(score1), True, (255, 255, 255))
    screen.blit(score_value, (x, y))


def show_score2(x, y):
    score_value = font.render(
        "Score 2 is " + str(score2), True, (255, 255, 255))
    screen.blit(score_value, (x, y))


def show_time():
    time_elapsed = font.render(
        "Time elapsed is " + str(end//1000), True, (255, 255, 255))
    screen.blit(time_elapsed, (610, 0))


def check_game_over():
    global player1_active, player2_active

    if player1 == -1 and player2 == -1:
        player1_active = False
        player2_active = False

        game_over()


def game_over():
    global running, player1_active, player2_active

    if score1 > score2:
        screen.fill((0, 0, 0))
        game = over.render("Player 1 Wins !!", True, (255, 255, 255))
        screen.blit(game, (200, 250))

    else:
        screen.fill((0, 0, 0))
        game = over.render("Player 2 Wins !!", True, (255, 255, 255))
        screen.blit(game, (200, 250))


def player(img, x, y):
    screen.blit(img, (x, y))


def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))


def tree(x, y, i):
    screen.blit(treeimg[i], (x, y))


def road():
    screen.blit(surf, (0, 0))
    screen.blit(surf, (0, 114))
    screen.blit(surf, (0, 228))
    screen.blit(surf, (0, 342))
    screen.blit(surf, (0, 456))
    screen.blit(surf, (0, 570))


def isCollision(enemyX, enemyY, playerX, playerY):
    distance = math.sqrt(math.pow(enemyX-playerX, 2) +
                         (math.pow(enemyY-playerY, 2)))
    if distance < 30:
        return True
    else:
        return False


def round(speed):
    global player1, player1_active, player1X, player1Y
    global player2, player2_active, player2X, player2Y
    global start, end
    global round1_cleared1, round1_cleared2, round2_cleared1, round2_cleared2
    global round3_cleared1, round3_cleared2
    global road1, road2, road3, road4, road5, road6
    global road1_flag
    global road2_flag, road3_flag, road4_flag, road5_flag, road6_flag

    # Enemy Movement and collision
    for i in range(num_of_enemies):

        enemyX[i] += enemyX_change[i]

        if enemyX[i] < 0:
            enemyX_change[i] = speed
        elif enemyX[i] > 750:
            enemyX_change[i] = -speed

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], player1X, player1Y)
        if collision:

            road1 = 0
            road2 = 0
            road3 = 0
            road4 = 0
            road5 = 0
            road6 = 0
            road1_flag = 0
            road2_flag = 0
            road3_flag = 0
            road4_flag = 0
            road5_flag = 0
            road6_flag = 0

            player1X = 370
            player1Y = 600

            player1 = -1
            player1_active = False
            player2_active = True

            round1_cleared1 = 1
            round2_cleared1 = 1

            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()

        collision = isCollision(enemyX[i], enemyY[i], player2X, player2Y)
        if collision:

            road1 = 0
            road2 = 0
            road3 = 0
            road4 = 0
            road5 = 0
            road6 = 0
            road1_flag = 0
            road2_flag = 0
            road3_flag = 0
            road4_flag = 0
            road5_flag = 0
            road6_flag = 0

            player2X = 370
            player2Y = 0

            player2 = -1
            player2_active = False
            player1_active = True

            round1_cleared2 = 1
            round2_cleared2 = 1

            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()

        enemy(enemyX[i], enemyY[i], i)

    if player != -1 and player1Y < 30 and speed == 0.3:
        round1_cleared1 = 1
        player1X = 370
        player1Y = 570

        if player2 != -1:
            player1_active = False
            player2_active = True

    if player2 != -1 and player2Y >= 570 and speed == 0.3:
        round1_cleared2 = 1
        player2X = 370
        player2Y = 0

        if player1 != -1:
            player1_active = True
            player2_active = False

    if player1 != -1 and player1Y < 30 and speed == 0.6:
        round2_cleared1 = 1
        player1X = 370
        player1Y = 570

        if player2 != -1:
            player1_active = False
            player2_active = True

    if player2 != -1 and player2Y >= 570 and speed == 0.6:
        round2_cleared2 = 1
        player2X = 370
        player2Y = 0

        if player1 != -1:
            player1_active = True
            player2_active = False

    if player1 != -1 and player1Y < 30 and speed == 1:
        round3_cleared1 = 1
        player1X = 370
        player1Y = 570

        if player2 != -1:
            player1_active = False
            player2_active = True

        game_over()

    if player2 != -1 and player2Y >= 570 and speed == 1:
        round3_cleared2 = 1
        player2X = 370
        player2Y = 0

        if player1 != -1:
            player1_active = True
            player2_active = False

        game_over()


def calculate_score1(y):
    global score1, score2, road1, road2, road3, road4, road5, road6, start, end
    global road1_flag
    global road2_flag, road3_flag, road4_flag, road5_flag, road6_flag
    global player1_active, player2_active

    # if y >= 570 and y <= 600:
    #     road1 = 1

    if player1_active:

        if y >= 456 and y <= 486:
            road2 = 1

        if y >= 342 and y <= 372:
            road3 = 1

        if y >= 228 and y <= 258:
            road4 = 1

        if y >= 114 and y <= 144:
            road5 = 1

        if y >= 0 and y <= 30:
            road6 = 1

        # if road1 == 1 and not(road1_flag):
        #     score1 += 5
        #     road1_flag = 1

        if road2 == 1 and not(road2_flag):
            score1 += 10
            road2_flag = 1

        if road3 == 1 and not(road3_flag):
            score1 += 30
            road3_flag = 1

        if road4 == 1 and not(road4_flag):
            score1 += 20
            road4_flag = 1

        if road5 == 1 and not(road5_flag):
            score1 += 30
            road5_flag = 1

        if road6 == 1 and not(road6_flag):
            score1 += 20
            road6_flag = 1
            print("reached")

        if road6_flag == 1:
            road1 = 0
            road2 = 0
            road3 = 0
            road4 = 0
            road5 = 0
            road6 = 0
            road1_flag = 0
            road2_flag = 0
            road3_flag = 0
            road4_flag = 0
            road5_flag = 0
            road6_flag = 0

            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()

            score1 -= (end//1000)

            if y < 1:
                player1_active = False
                player2_active = True


def calculate_score2(y):
    global score1, score2, road1, road2, road3, road4, road5, road6, start, end
    global road1_flag, road2_flag, road3_flag, road4_flag, road5_flag
    global road6_flag
    global player1_active, player2_active

    if player2_active:

        if y >= 570 and y <= 600:
            road5 = 1

        if y >= 456 and y <= 486:
            road4 = 1

        if y >= 342 and y <= 372:
            road3 = 1

        if y >= 228 and y <= 258:
            road2 = 1

        if y >= 114 and y <= 144:
            road1 = 1

        # if y >= 0 and y <= 30:
        #     road6 = 1

        if road1 == 1 and not(road1_flag):
            score2 += 10
            road1_flag = 1

        if road2 == 1 and not(road2_flag):
            score2 += 30
            road2_flag = 1

        if road3 == 1 and not(road3_flag):
            score2 += 20
            road3_flag = 1

        if road4 == 1 and not(road4_flag):
            score2 += 30
            road4_flag = 1

        if road5 == 1 and not(road5_flag):
            score2 += 20
            road5_flag = 1

        if road5_flag == 1:
            road1 = 0
            road2 = 0
            road3 = 0
            road4 = 0
            road5 = 0
            road6 = 0
            road1_flag = 0
            road2_flag = 0
            road3_flag = 0
            road4_flag = 0
            road5_flag = 0
            road6_flag = 0

            player1_active = False
            player2_active = True

            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            score2 -= (end//1000)

        # if road6 == 1 and not(road6_flag):
        #     score1 += 40
        #     road6_flag = 1


# Game loop
running = True
while running:
    screen.fill((50, 151, 255))
    road()
    # clock.tick(600)

    end = pygame.time.get_ticks() - start

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player1 Movement
    keys = pygame.key.get_pressed()

    if player1_active is True and player1 == 1:
        if keys[pygame.K_LEFT]:
            player1X -= 0.2
        elif keys[pygame.K_RIGHT]:
            player1X += 0.2
        if keys[pygame.K_DOWN]:
            player1Y += 0.2
        elif keys[pygame.K_UP]:
            player1Y -= 0.2

    # Player2 Movement
    keys = pygame.key.get_pressed()

    if player2_active is True and player2 == 1:
        if keys[pygame.K_a]:
            player2X -= 0.2
        elif keys[pygame.K_d]:
            player2X += 0.2
        if keys[pygame.K_s]:
            player2Y += 0.2
        elif keys[pygame.K_w]:
            player2Y -= 0.2

    # Quit
    if keys[pygame.K_ESCAPE]:
        running = False

    # Player1 Boundaries
    if player1X < 0:
        player1X = 0
    elif player1X > 730:
        player1X = 730
    if player1Y < 0:
        player1Y = 0
    elif player1Y > 570:
        player1Y = 570

    # player2 Boundaries
    if player2X < 0:
        player2X = 0
    elif player2X > 730:
        player2X = 730
    if player2Y < 0:
        player2Y = 0
    elif player2Y > 570:
        player2Y = 570

    # Tree placement and collsion
    for i in range(num_of_trees):
        # Collision
        collision = isCollision(treeX[i], treeY[i], player1X, player1Y)
        if collision:

            road1 = 0
            road2 = 0
            road3 = 0
            road4 = 0
            road5 = 0
            road6 = 0
            road1_flag = 0
            road2_flag = 0
            road3_flag = 0
            road4_flag = 0
            road5_flag = 0
            road6_flag = 0

            player1X = 370
            player1Y = 600

            player1 = -1
            player1_active = False
            player2_active = True

            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()

        collision = isCollision(treeX[i], treeY[i], player2X, player2Y)
        if collision:

            road1 = 0
            road2 = 0
            road3 = 0
            road4 = 0
            road5 = 0
            road6 = 0
            road1_flag = 0
            road2_flag = 0
            road3_flag = 0
            road4_flag = 0
            road5_flag = 0
            road6_flag = 0

            player2X = 370
            player2Y = 0

            player2 = -1
            player1_active = True
            player2_active = False

            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()

        tree(treeX[i], treeY[i], i)

    calculate_score1(player1Y)
    calculate_score2(player2Y)

    if round2_cleared1 == 1 and round2_cleared2 == 1:
        round(1)

    elif round1_cleared1 == 1 and round1_cleared2 == 1:
        round(0.6)

    else:
        round(0.3)

    player(player1img, player1X, player1Y)
    player(player2img, player2X, player2Y)
    show_score1(scoreX, scoreY)
    show_score2(10, 568)
    show_time()
    check_game_over()
    pygame.display.update()
