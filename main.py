# Pong2.2
# by @0N3IR0S
# 28.03.2020

import pygame
import winsound
from classes import Player
from classes import Ball
from classes import Options
from random import randint

# initialize pygame
pygame.init()

# create screen
game_screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Pong2.2 by @0N3IR0S")
icon = pygame.image.load("pongIcon.png")
pygame.display.set_icon(icon)

# setup classes
Player1 = Player(False, False, 275, 0)
Player2 = Player(False, False, 275, 0)
Ball1 = Ball(395, randint(0, 390), 10, 10)
Options1 = Options(True, False, False)
if randint(0, 1):
    Ball1.x_change *= -1
if randint(0, 1):
    Ball1.y_change *= -1

# FPS limitation
clock = pygame.time.Clock()


# draw score1 function
def draw_final_score1(score):
    if score == 0:
        pygame.draw.lines(game_screen, (255, 255, 255), True, [(325, 200), (355, 200), (355, 250), (325, 250)], 10)
    elif score == 1:
        pygame.draw.lines(game_screen, (255, 255, 255), False, [(355, 198), (355, 252)], 10)
    elif score == 2:
        pygame.draw.lines(game_screen, (255, 255, 255), False,
                          [(325, 200), (355, 200), (355, 225), (325, 225), (325, 250), (355, 250)], 10)
    elif score == 3:
        pygame.draw.lines(game_screen, (255, 255, 255), False,
                          [(325, 200), (355, 200), (355, 225), (325, 225), (355, 225), (355, 250), (325, 250)], 10)
    elif score == 4:
        pygame.draw.lines(game_screen, (255, 255, 255), False,
                          [(325, 200), (325, 225), (355, 225), (355, 200), (355, 250)], 10)
    elif score == 5:
        pygame.draw.lines(game_screen, (255, 255, 255), False,
                          [(355, 200), (325, 200), (325, 225), (355, 225), (355, 250), (325, 250)], 10)
    elif score == 6:
        pygame.draw.lines(game_screen, (255, 255, 255), False,
                          [(325, 200), (325, 250), (355, 250), (355, 225), (325, 225)], 10)
    elif score == 7:
        pygame.draw.lines(game_screen, (255, 255, 255), False, [(325, 200), (355, 200), (355, 250)], 10)
    elif score == 8:
        pygame.draw.lines(game_screen, (255, 255, 255), True,
                          [(325, 200), (355, 200), (355, 225), (325, 225), (355, 225), (355, 250), (325, 250)], 10)
    elif score == 9:
        pygame.draw.lines(game_screen, (255, 255, 255), False,
                          [(325, 200), (325, 225), (355, 225), (355, 200), (325, 200), (355, 200), (355, 250)], 10)
    elif score == 10:
        pygame.draw.lines(game_screen, (255, 255, 255), False, [(310, 198), (310, 252)], 10)
        pygame.draw.lines(game_screen, (255, 255, 255), True, [(330, 200), (360, 200), (360, 250), (330, 250)], 10)
    elif score == 11:
        pygame.draw.lines(game_screen, (255, 255, 255), False, [(310, 198), (310, 252)], 10)
        pygame.draw.lines(game_screen, (255, 255, 255), False, [(360, 198), (360, 252)], 10)


# draw score2 function
def draw_final_score2(score):
    if score == 0:
        pygame.draw.lines(game_screen, (255, 255, 255), True, [(445, 200), (475, 200), (475, 250), (445, 250)], 10)
    elif score == 1:
        pygame.draw.lines(game_screen, (255, 255, 255), False, [(475, 198), (475, 252)], 10)
    elif score == 2:
        pygame.draw.lines(game_screen, (255, 255, 255), False,
                          [(445, 200), (475, 200), (475, 225), (445, 225), (445, 250), (475, 250)], 10)
    elif score == 3:
        pygame.draw.lines(game_screen, (255, 255, 255), False,
                          [(445, 200), (475, 200), (475, 225), (445, 225), (475, 225), (475, 250), (445, 250)], 10)
    elif score == 4:
        pygame.draw.lines(game_screen, (255, 255, 255), False,
                          [(445, 200), (445, 225), (475, 225), (475, 200), (475, 250)], 10)
    elif score == 5:
        pygame.draw.lines(game_screen, (255, 255, 255), False,
                          [(475, 200), (445, 200), (445, 225), (475, 225), (475, 250), (445, 250)], 10)
    elif score == 6:
        pygame.draw.lines(game_screen, (255, 255, 255), False,
                          [(445, 200), (445, 250), (475, 250), (475, 225), (445, 225)], 10)
    elif score == 7:
        pygame.draw.lines(game_screen, (255, 255, 255), False, [(445, 200), (475, 200), (475, 250)], 10)
    elif score == 8:
        pygame.draw.lines(game_screen, (255, 255, 255), True,
                          [(445, 200), (475, 200), (475, 225), (445, 225), (475, 225), (475, 250), (445, 250)], 10)
    elif score == 9:
        pygame.draw.lines(game_screen, (255, 255, 255), False,
                          [(445, 200), (445, 225), (475, 225), (475, 200), (445, 200), (475, 200), (475, 250)], 10)
    elif score == 10:
        pygame.draw.lines(game_screen, (255, 255, 255), False, [(440, 198), (440, 252)], 10)
        pygame.draw.lines(game_screen, (255, 255, 255), True, [(460, 200), (490, 200), (490, 250), (460, 250)], 10)
    elif score == 11:
        pygame.draw.lines(game_screen, (255, 255, 255), False, [(440, 198), (440, 252)], 10)
        pygame.draw.lines(game_screen, (255, 255, 255), False, [(490, 198), (490, 252)], 10)


# draw score1 function
def draw_score1(score):
    if score == 0:
        pygame.draw.lines(game_screen, (255, 255, 255), True, [(325, 20), (355, 20), (355, 70), (325, 70)], 10)
    elif score == 1:
        pygame.draw.lines(game_screen, (255, 255, 255), False, [(355, 18), (355, 72)], 10)
    elif score == 2:
        pygame.draw.lines(game_screen, (255, 255, 255), False,
                          [(325, 20), (355, 20), (355, 45), (325, 45), (325, 70), (355, 70)], 10)
    elif score == 3:
        pygame.draw.lines(game_screen, (255, 255, 255), False,
                          [(325, 20), (355, 20), (355, 45), (325, 45), (355, 45), (355, 70), (325, 70)], 10)
    elif score == 4:
        pygame.draw.lines(game_screen, (255, 255, 255), False, [(325, 20), (325, 45), (355, 45), (355, 20), (355, 70)],
                          10)
    elif score == 5:
        pygame.draw.lines(game_screen, (255, 255, 255), False,
                          [(355, 20), (325, 20), (325, 45), (355, 45), (355, 70), (325, 70)], 10)
    elif score == 6:
        pygame.draw.lines(game_screen, (255, 255, 255), False, [(325, 20), (325, 70), (355, 70), (355, 45), (325, 45)],
                          10)
    elif score == 7:
        pygame.draw.lines(game_screen, (255, 255, 255), False, [(325, 20), (355, 20), (355, 70)], 10)
    elif score == 8:
        pygame.draw.lines(game_screen, (255, 255, 255), True,
                          [(325, 20), (355, 20), (355, 45), (325, 45), (355, 45), (355, 70), (325, 70)], 10)
    elif score == 9:
        pygame.draw.lines(game_screen, (255, 255, 255), False,
                          [(325, 20), (325, 45), (355, 45), (355, 20), (325, 20), (355, 20), (355, 70)], 10)
    elif score == 10:
        pygame.draw.lines(game_screen, (255, 255, 255), False, [(310, 18), (310, 72)], 10)
        pygame.draw.lines(game_screen, (255, 255, 255), True, [(330, 20), (360, 20), (360, 70), (330, 70)], 10)
    elif score == 11:
        pygame.draw.lines(game_screen, (255, 255, 255), False, [(310, 18), (310, 72)], 10)
        pygame.draw.lines(game_screen, (255, 255, 255), False, [(360, 18), (360, 72)], 10)


# draw score2 function
def draw_score2(score):
    if score == 0:
        pygame.draw.lines(game_screen, (255, 255, 255), True, [(445, 20), (475, 20), (475, 70), (445, 70)], 10)
    elif score == 1:
        pygame.draw.lines(game_screen, (255, 255, 255), False, [(475, 18), (475, 72)], 10)
    elif score == 2:
        pygame.draw.lines(game_screen, (255, 255, 255), False,
                          [(445, 20), (475, 20), (475, 45), (445, 45), (445, 70), (475, 70)], 10)
    elif score == 3:
        pygame.draw.lines(game_screen, (255, 255, 255), False,
                          [(445, 20), (475, 20), (475, 45), (445, 45), (475, 45), (475, 70), (445, 70)], 10)
    elif score == 4:
        pygame.draw.lines(game_screen, (255, 255, 255), False, [(445, 20), (445, 45), (475, 45), (475, 20), (475, 70)],
                          10)
    elif score == 5:
        pygame.draw.lines(game_screen, (255, 255, 255), False,
                          [(475, 20), (445, 20), (445, 45), (475, 45), (475, 70), (445, 70)], 10)
    elif score == 6:
        pygame.draw.lines(game_screen, (255, 255, 255), False, [(445, 20), (445, 70), (475, 70), (475, 45), (445, 45)],
                          10)
    elif score == 7:
        pygame.draw.lines(game_screen, (255, 255, 255), False, [(445, 20), (475, 20), (475, 70)], 10)
    elif score == 8:
        pygame.draw.lines(game_screen, (255, 255, 255), True,
                          [(445, 20), (475, 20), (475, 45), (445, 45), (475, 45), (475, 70), (445, 70)], 10)
    elif score == 9:
        pygame.draw.lines(game_screen, (255, 255, 255), False,
                          [(445, 20), (445, 45), (475, 45), (475, 20), (445, 20), (475, 20), (475, 70)], 10)
    elif score == 10:
        pygame.draw.lines(game_screen, (255, 255, 255), False, [(440, 18), (440, 72)], 10)
        pygame.draw.lines(game_screen, (255, 255, 255), True, [(460, 20), (490, 20), (490, 70), (460, 70)], 10)
    elif score == 11:
        pygame.draw.lines(game_screen, (255, 255, 255), False, [(440, 18), (440, 72)], 10)
        pygame.draw.lines(game_screen, (255, 255, 255), False, [(490, 18), (490, 72)], 10)


# draw loco function
def draw_logo():
    # P
    pygame.draw.rect(game_screen, (255, 255, 255), [130, 130, 40, 100])
    pygame.draw.rect(game_screen, (255, 255, 255), [170, 130, 40, 20])
    pygame.draw.rect(game_screen, (255, 255, 255), [170, 170, 40, 20])
    pygame.draw.rect(game_screen, (255, 255, 255), [190, 150, 40, 20])
    # O
    pygame.draw.rect(game_screen, (255, 255, 255), [290, 130, 60, 20])
    pygame.draw.rect(game_screen, (255, 255, 255), [290, 210, 60, 20])
    pygame.draw.rect(game_screen, (255, 255, 255), [270, 150, 40, 60])
    pygame.draw.rect(game_screen, (255, 255, 255), [330, 150, 40, 60])
    # N
    pygame.draw.rect(game_screen, (255, 255, 255), [410, 130, 40, 100])
    pygame.draw.rect(game_screen, (255, 255, 255), [490, 130, 40, 100])
    pygame.draw.rect(game_screen, (255, 255, 255), [450, 150, 20, 40])
    pygame.draw.rect(game_screen, (255, 255, 255), [470, 170, 20, 40])
    # G
    pygame.draw.rect(game_screen, (255, 255, 255), [570, 150, 40, 60])
    pygame.draw.rect(game_screen, (255, 255, 255), [590, 130, 80, 20])
    pygame.draw.rect(game_screen, (255, 255, 255), [590, 210, 60, 20])
    pygame.draw.rect(game_screen, (255, 255, 255), [630, 170, 40, 40])
    # Paddles
    pygame.draw.rect(game_screen, (255, 255, 255), [30, 275, 10, 50])
    pygame.draw.rect(game_screen, (255, 255, 255), [760, 275, 10, 50])


def draw_play():
    # background
    pygame.draw.rect(game_screen, (255, 255, 255), [312, 275, 176, 50])
    # P
    pygame.draw.rect(game_screen, (50, 50, 50), [322, 285, 12, 30])
    pygame.draw.rect(game_screen, (50, 50, 50), [334, 285, 12, 6])
    pygame.draw.rect(game_screen, (50, 50, 50), [334, 297, 12, 6])
    pygame.draw.rect(game_screen, (50, 50, 50), [340, 291, 12, 6])
    # L
    pygame.draw.rect(game_screen, (50, 50, 50), [364, 285, 12, 24])
    pygame.draw.rect(game_screen, (50, 50, 50), [364, 309, 24, 6])
    # A
    pygame.draw.rect(game_screen, (50, 50, 50), [400, 291, 12, 24])
    pygame.draw.rect(game_screen, (50, 50, 50), [418, 291, 12, 24])
    pygame.draw.rect(game_screen, (50, 50, 50), [406, 285, 18, 6])
    pygame.draw.rect(game_screen, (50, 50, 50), [412, 303, 6, 6])
    # Y
    pygame.draw.rect(game_screen, (50, 50, 50), [442, 285, 12, 6])
    pygame.draw.rect(game_screen, (50, 50, 50), [466, 285, 12, 6])
    pygame.draw.rect(game_screen, (50, 50, 50), [448, 291, 24, 6])
    pygame.draw.rect(game_screen, (50, 50, 50), [454, 297, 12, 18])


def key_pressed():
    if event.type == pygame.KEYDOWN:
        # Enter
        if event.key == pygame.K_RETURN:
            Options1.enter = True
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
        # Enter
        if event.key == pygame.K_RETURN:
            Options1.enter = False
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


def move_players():
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


# draw player paddles
def draw_paddle():
    pygame.draw.rect(game_screen, (255, 255, 255), [770, Player2.pos, 10, 50])
    pygame.draw.rect(game_screen, (255, 255, 255), [20, Player1.pos, 10, 50])


def draw_colon():
    pygame.draw.rect(game_screen, (255, 255, 255), [395, 210, 10, 10])
    pygame.draw.rect(game_screen, (255, 255, 255), [395, 230, 10, 10])


def move_ball():
    # move ball
    Ball1.pos_x += Ball1.x_change
    Ball1.pos_y += Ball1.y_change

    # check upper borders
    if Ball1.pos_y <= 0 or Ball1.pos_y >= 590:
        winsound.PlaySound("pong1Sound.wav", winsound.SND_ASYNC)
        Ball1.y_change *= -1

    # check side borders
    if Ball1.pos_x < 0:
        winsound.PlaySound("pong2Sound.wav", winsound.SND_ASYNC)
        Ball1.pos_x = 395
        Ball1.pos_y = randint(0, 390)
        if randint(0, 1):
            Ball1.y_change *= -1
        Player1.pos = 275
        Player2.pos = 275
        Player2.score += 1
    if Ball1.pos_x > 800:
        winsound.PlaySound("pong2Sound.wav", winsound.SND_ASYNC)
        Ball1.pos_x = 395
        Ball1.pos_y = randint(0, 390)
        if randint(0, 1):
            Ball1.y_change *= -1
        Player1.pos = 275
        Player2.pos = 275
        Player1.score += 1

    # check if hit paddles
    if Ball1.pos_x <= 30 and Player1.pos - 10 < Ball1.pos_y < Player1.pos + 50:
        winsound.PlaySound("pong1Sound.wav", winsound.SND_ASYNC)
        Ball1.x_change *= -1
        Ball1.pos_x = 30
    if Ball1.pos_x >= 760 and Player2.pos - 10 < Ball1.pos_y < Player2.pos + 50:
        winsound.PlaySound("pong1Sound.wav", winsound.SND_ASYNC)
        Ball1.x_change *= -1
        Ball1.pos_x = 760

    # draw ball
    pygame.draw.rect(game_screen, (255, 255, 255), [Ball1.pos_x, Ball1.pos_y, 10, 10])


def mode():
    # start game
    if Options1.enter:
        Options1.start_screen = False

    # restart game
    if Options1.finished and Options1.enter:
        Options1.finished = False
        Player1.score = 0
        Player2.score = 0

    # finish game
    if Player1.score == 11 or Player2.score == 11:
        Options1.finished = True


# main loop
game_exit = False
while not game_exit:
    for event in pygame.event.get():
        # Quit Program
        if event.type == pygame.QUIT:
            game_exit = True
        # Key pressed
        key_pressed()

    # game screen
    game_screen.fill((0, 0, 0))

    # mode
    mode()

    # start_screen
    if Options1.start_screen:
        # draw logo
        draw_logo()
        draw_paddle()
        draw_play()

    # Game started
    if Options1.start_screen == False and Options1.finished == False:
        # move players
        move_players()
        # draw paddles
        draw_paddle()
        # move ball
        move_ball()
        # draw score
        draw_score1(Player1.score)
        draw_score2(Player2.score)
        # draw middle line
        for i in range(-5, 600, 31):
            pygame.draw.rect(game_screen, (255, 255, 255), [395, i, 10, 20])

    # game finished
    if Options1.finished:
        # draw score
        draw_final_score1(Player1.score)
        draw_final_score2(Player2.score)
        draw_colon()
        draw_play()
        draw_paddle()

    # update display
    pygame.display.update()
    clock.tick(30)

# quit
pygame.quit()
