import pygame
import random
pygame.init()

# Screen
screenwidth = 800
screenheight = 600

# Clock
start = 0
end = 0
clockfont = pygame.font.Font('Flashing.ttf', 30)

# Caption and icon
pygame.display.set_caption("River Crossing Competition Game")
icon = pygame.image.load('ship.png')

# Rounds
round1_cleared1 = -1
round2_cleared1 = -1
round1_cleared2 = -1
round2_cleared2 = -1
round3_cleared1 = -1
round3_cleared2 = -1

# Road
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

# Player1
player1 = 1
player1_active = True
player1img = pygame.image.load('triangle.png')
player1X = 370
player1Y = 600

# Player2
player2 = 1
player2_active = False
player2img = pygame.image.load('triangle2.png')
player2X = 370
player2Y = 0

# Tree
treeimg = []
treeX = []
treeY = [114, 228, 342, 456, 114, 228, 342, 456]
num_of_trees = 8

for i in range(num_of_trees):
    treeimg.append(pygame.image.load('tree.png'))
    treeX.append(random.randint(0, 729))

# Enemy
enemyimg = []
enemyX = []
enemyY = [50, 164, 278, 392, 506, 164, 392]
enemyX_change = []
num_of_enemies = 7

for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load('cruise.png'))
    enemyX.append(random.randint(0, 729))
    enemyX_change.append(0.3)

# Scoring
score1 = 0
score2 = 0
font = pygame.font.Font('Flashing.ttf', 30)
scoreX = 10
scoreY = 0

# Game Over Font
over = pygame.font.Font('Flashing.ttf', 64)
