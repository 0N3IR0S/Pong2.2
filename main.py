# Pong2.2
# by @0N3IR0S
# 28.03.2020

import pygame

# initialize  pygame
pygame.init()

# create screen
game_screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Pong2.0 by Me")
icon = pygame.image.load("pongIcon.png")
pygame.display.set_icon(icon)

lead_x = 300
lead_y = 300
lead_x_change = 0

# FPS limitation
clock = pygame.time.Clock()

# main loop
game_exit = False
while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -10
                print("Hello")
            if event.key == pygame.K_RIGHT:
                lead_x_change = 10

    lead_x += lead_x_change
    game_screen.fill((0, 0, 0))
    pygame.draw.rect(game_screen, (255, 255, 255), [lead_x, lead_y, 10, 10])
    pygame.display.update()

    clock.tick(30)

# quit
pygame.quit()