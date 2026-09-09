from logging import disable

import pygame
import time
import consts

pygame.init()
screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT-250))
pygame.display.set_caption("Flag Game")

soldier_img =pygame.transform.scale(
        pygame.image.load(consts.SOLDIER_IMAGE),
        (consts.SOLDIER_COLS * consts.CELL_SIZE*2, consts.SOLDIER_ROWS * consts.CELL_SIZE))
bush_img =pygame.transform.scale(
        pygame.image.load(consts.BUSH_IMAGE),
        (consts.CELL_SIZE * consts.BUSH_COLS, consts.CELL_SIZE * consts.BUSH_ROWS))
mine_img =pygame.transform.scale(
        pygame.image.load(consts.MINE_IMAGE),
        (consts.MINE_COLS * consts.CELL_SIZE, consts.MINE_ROWS * consts.CELL_SIZE))

soldier_night_img=pygame.transform.scale(
        pygame.image.load(consts.SOLDIER_NIGHT),
        (consts.SOLDIER_COLS * consts.CELL_SIZE*2, consts.SOLDIER_ROWS * consts.CELL_SIZE))

injury_img=pygame.transform.scale(
        pygame.image.load(consts.SOLDIER_INJURY),
        (consts.SOLDIER_COLS * consts.CELL_SIZE*2, consts.SOLDIER_ROWS * consts.CELL_SIZE))

flag_img=pygame.transform.scale(
        pygame.image.load(consts.FLAG_IMAGE),
        (consts.FLAG_COLS * consts.CELL_SIZE, consts.FLAG_ROWS * consts.CELL_SIZE))


def draw_ENTER_game(field, soldier_pos):
    screen.fill(consts.GREEN)
    count_flag = 0

    screen.fill(consts.BLACK)
    for c in range(consts.BOARD_COLS + 1):
        x = c * consts.CELL_SIZE
        start_pos=(x, 0)
        end_pos=(x, consts.BOARD_ROWS * consts.CELL_SIZE)
        pygame.draw.aaline(screen, consts.GREEN, start_pos, end_pos)

    for r in range(consts.BOARD_ROWS + 1):
        y = r * consts.CELL_SIZE
        start_pos = (0, y)
        end_pos = (consts.BOARD_COLS * consts.CELL_SIZE, y)
        pygame.draw.aaline(screen, consts.GREEN, start_pos, end_pos)

    if soldier_night_img:  # --------injury_img
        soldier_x = soldier_pos[0] * consts.CELL_SIZE
        soldier_y = soldier_pos[1] * consts.CELL_SIZE
        screen.blit(soldier_night_img, (soldier_x, soldier_y))

    for r in range(consts.BOARD_ROWS):
        for c in range(consts.BOARD_COLS):
            x = c * consts.CELL_SIZE
            y = r * consts.CELL_SIZE
            if field[r][c] == consts.MINE and mine_img:
                screen.blit(mine_img, (x, y))


def  draw_game(field, soldier_pos):
    screen.fill(consts.GREEN)
    count_flag = 0

    for r in range(consts.BOARD_ROWS):
        for c in range(consts.BOARD_COLS):
            x = c * consts.CELL_SIZE
            y = r * consts.CELL_SIZE


            if field[r][c]==consts.BUSH and bush_img :
                screen.blit(bush_img,(x, y))

            elif field[r][c]==consts.SOLDIER_IMAGE: #and not injury
                screen.blit(soldier_img,(x, y))
            elif field[r][c]==consts.SOLDIER_IMAGE :
                screen.blit(soldier_night_img,(x, y))
            elif field[r][c]==consts.FLAG  and count_flag==0:
                screen.blit(flag_img,(x, y))
                count_flag+=1




    if soldier_img:
        soldier_x=soldier_pos[0]*consts.CELL_SIZE
        soldier_y=soldier_pos[1]*consts.CELL_SIZE
        screen.blit(soldier_img, (soldier_x, soldier_y))
    # elif injury_img:
    #     soldier_x = soldier_pos[0] * consts.CELL_SIZE
    #     soldier_y = soldier_pos[1] * consts.CELL_SIZE
    #     screen.blit(injury_img, (soldier_x, soldier_y))


    pygame.display.flip()


def draw_message(msg):
    font = pygame.font.SysFont(consts.FONT_NAME, consts.FONT_SIZE)
    text_img = font.render(msg, True, consts.BLACK)
    # screen.blit(rendered_text, (consts.WINDOW_WIDTH // 2 - 50, consts.WINDOW_HEIGHT // 2)) #
    screen.blit(text_img, (0,0))
    pygame.display.flip()