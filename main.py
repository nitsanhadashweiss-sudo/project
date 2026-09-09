import sys
import consts
import screen
import soldier
import game_field
import time
import pygame


won=False
lost=False


game_field.create_field()
see_mines=False


running = True
while running:
    action=0
    game_field.create_field()
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                action = 1
            elif event.key == pygame.K_LEFT:
                action = 2
            elif event.key == pygame.K_DOWN:
                action = 3
            elif event.key == pygame.K_RIGHT:
                action = 4
            elif event.key == pygame.K_RETURN:  # ENTER   BUT FOR 1 SECOND!
                see_mines = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN:  # HIDES MINES BACK
                see_mines = False

        if action != 0:
            soldier.soldier_move(action)
            game_result=soldier.game_state()
            if game_result:
                screen.draw_game(game_field.field, soldier.corner, see_mines)

    if soldier.flag() or soldier.mine():
        running = False

screen.draw_game(game_field.field, soldier.corner, see_mines)

screen.draw_message(soldier.message)
time.sleep(3)

pygame.quit()
sys.exit()


