# Pong2.2
# by @0N3IR0S
# 28.03.2020

import pygame
from classes import Player
from classes import Ball
from random import  randint

# initialize pygame
pygame.init()

# create screen
game_screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Pong2.0 by Me")
icon = pygame.image.load("pongIcon.png")
pygame.display.set_icon(icon)

lead_x_change = 0

# setup classes
Player1 = Player("Player1", False, False, 275, 0)
Player2 = Player("Player2", False, False, 275, 0)
Ball1 = Ball("Ball1", 395, randint(0, 390), 10, 10)
if randint(0, 1):
    Ball1.x_change *= -1
if randint(0, 1):
    Ball1.y_change *= -1

# FPS limitation
clock = pygame.time.Clock()

# main loop
game_exit = False
while not game_exit:
    for event in pygame.event.get():
        # Quit Program
        if event.type == pygame.QUIT:
            game_exit = True
        # Key pressed
        if event.type == pygame.KEYDOWN:
            # Player1
            if event.key == pygame.K_w:
                Player1.up = True
            if event.key == pygame.K_s:
                Player1.down = True
            # Player2
            if event.key == pygame.K_UP:
                Player2.up = True
            if event.key == pygame.K_DOWN:
                Player2.down = True
        # Key released
        if event.type == pygame.KEYUP:
            # Player1
            if event.key == pygame.K_w:
                Player1.up = False
            if event.key == pygame.K_s:
                Player1.down = False
            # Player2
            if event.key == pygame.K_UP:
                Player2.up = False
            if event.key == pygame.K_DOWN:
                Player2.down = False

    # move Player1
    if Player1.up:
        if Player1.pos <= 0:
            Player1.pos = 0
        else:
            Player1.pos -= 15
    else:
        Player1.pos = Player1.pos

    if Player1.down:
        if Player1.pos >= 550:
            Player1.pos = 550
        else:
            Player1.pos += 15
    else:
        Player1.pos = Player1.pos

    # move Player2
    if Player2.up:
        if Player2.pos <= 0:
            Player2.pos = 0
        else:
            Player2.pos -= 15
    else:
        Player2.pos = Player2.pos

    if Player2.down:
        if Player2.pos >= 550:
            Player2.pos = 550
        else:
            Player2.pos += 15
    else:
        Player2.pos = Player2.pos

    # move ball
    Ball1.pos_x += Ball1.x_change
    Ball1.pos_y += Ball1.y_change

    # check upper borders
    if Ball1.pos_y <= 0 or Ball1.pos_y >= 590:
        Ball1.y_change *= -1

    # check side borders
    if Ball1.pos_x < 0:
        Ball1.pos_x = 395
        Ball1.pos_y = randint(0, 390)
        Player1.pos = 275
        Player2.pos = 275
        if randint(0, 1):
            Ball1.y_change *= -1
    if Ball1.pos_x > 800:
        Ball1.pos_x = 395
        Ball1.pos_y = randint(0, 390)
        Player1.pos = 275
        Player2.pos = 275
        if randint(0, 1):
            Ball1.y_change *= -1

    # check if hit paddles
    if Ball1.pos_x <= 30 and Player1.pos - 10 < Ball1.pos_y < Player1.pos + 50:
        Ball1.x_change *= -1
        Ball1.pos_x = 30
    if Ball1.pos_x >= 760 and Player2.pos - 10 < Ball1.pos_y < Player2.pos + 50:
        Ball1.x_change *= -1
        Ball1.pos_x = 760

    # game screen
    game_screen.fill((0, 0, 0))
    # draw middle line
    for i in range(-5, 600, 31):
        pygame.draw.rect(game_screen, (255, 255, 255), [395, i, 10, 20])
    # draw player paddles
    pygame.draw.rect(game_screen, (255, 255, 255), [770, Player2.pos, 10, 50])
    pygame.draw.rect(game_screen, (255, 255, 255), [20, Player1.pos, 10, 50])
    # draw ball
    pygame.draw.rect(game_screen, (255, 255, 255), [Ball1.pos_x, Ball1.pos_y, 10, 10])
    # update display
    pygame.display.update()
    clock.tick(30)

# quit
pygame.quit()
