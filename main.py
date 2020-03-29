# Pong2.2
# by @0N3IR0S
# 28.03.2020

import pygame
from Players import Player

# initialize  pygame
pygame.init()

# create screen
game_screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Pong2.0 by Me")
icon = pygame.image.load("pongIcon.png")
pygame.display.set_icon(icon)

lead_x_change = 0

# object setup Player
Player1 = Player("Player1", False, False, 275, 0)
Player2 = Player("Player2", False, False, 275, 0)

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

    game_screen.fill((0, 0, 0))
    pygame.draw.rect(game_screen, (255, 255, 255), [770, Player2.pos, 10, 50])
    pygame.draw.rect(game_screen, (255, 255, 255), [20, Player1.pos, 10, 50])
    pygame.display.update()

    clock.tick(30)

# quit
pygame.quit()