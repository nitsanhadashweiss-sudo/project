import sys
import consts
import screen
import soldier
import game_field
import time
import pygame


won=False
lost=False

def win():
    screen.draw_message(consts.WIN_MESSAGE)
    time.sleep(3)
    global won
    won= True


def lose():
    screen.draw_message(consts.LOSE_MESSAGE)
    time.sleep(3)
    global lost
    lost = True


game_field.create_field()

running = True
while running:
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    action=0
    if keys[pygame.K_UP]:
        action=1
    elif keys[pygame.K_DOWN]:
        action=3
    elif keys[pygame.K_LEFT]:
        action=2
    elif keys[pygame.K_RIGHT]:
        action=4

    if keys[pygame.K_KP_ENTER]:
        game_field.board_show()

    soldier.soldier_move(action)

if won or lost:
    running = False

pygame.quit()
sys.exit()


