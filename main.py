import sys
import consts
import screen
import soldier
import game_field
import time
import pygame

running=True
see_mines=False
game_field.create_field()

while running:
    action=1

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                action=1
            elif event.key==pygame.K_LEFT:
                action=2
            elif event.key == pygame.K_DOWN:
                action = 3
            elif event.key == pygame.K_RIGHT:
                action = 4
            elif event.key == pygame.K_RETURN: #ENTER   BUT FOR 1 SECOND!
                see_mines = True
                # time.sleep(1)
                # see_mines= False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN:  # HIDES MINES BACK
                see_mines = False

        if action!= 0:
            soldier.soldier_move(action)

            game_result = soldier.game_state()

            if game_result:
                screen.draw_game(game_field.field, soldier.corner, see_mines)

                screen.draw_message(game_result)
                time.sleep(3)

                running = False


        screen.draw_game(game_field.field, soldier.corner, see_mines)

pygame.quit()
sys.exit()




# game_field.create_field()
#--
# screen.draw_game(game_field.field, (0,0), see_mines)