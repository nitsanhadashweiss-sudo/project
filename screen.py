import pygame
import consts

pygame.init()
screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT-200))
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


def draw_game(field, soldier_pos, show_mines=False):
    screen.fill(consts.GREEN)

    for r in range(consts.BOARD_ROWS):
        for c in range(consts.BOARD_COLS):
            x = c * consts.CELL_SIZE
            y = r * consts.CELL_SIZE

            if field[r][c]==consts.BUSH and bush_img:
                screen.blit(bush_img,(x, y))
            elif field[r][c]==consts.MINE and show_mines and mine_img:
                screen.blit(mine_img,(x, y))
            elif field[r][c]==consts.SOLDIER_IMAGE and not show_mines: #and not injury
                screen.blit(soldier_img,(x, y))
            elif field[r][c]==consts.SOLDIER_IMAGE and show_mines:
                screen.blit(soldier_night_img,(x, y))
            elif field[r][c]==consts.FLAG:
                screen.blit(flag_img,(x, y))

            # elif r==consts.FLAG_ROWS-1 and c==consts.FLAG_COLS-1:
            #     screen.blit(flag_img, (x, y))

            #flag
            # x_flag=consts.CELL_SIZE*consts.FLAG_COLS
            # y_flag=consts.CELL_SIZE*consts.FLAG_ROWS
            # screen.blit(flag_img, (x_flag, y_flag))

            # elif field[r][c]==consts.SOLDIER_IMAGE and INJURY:
            #     screen.blit(injury_img,(x, y))



    if soldier_night_img and show_mines: #--------injury_img
        soldier_x = soldier_pos[0] * consts.CELL_SIZE
        soldier_y = soldier_pos[1] * consts.CELL_SIZE
        screen.blit(soldier_night_img, (soldier_x, soldier_y))
    # if injury_img:
    #     soldier_x = soldier_pos[0] * consts.CELL_SIZE
    #     soldier_y = soldier_pos[1] * consts.CELL_SIZE
    #     screen.blit(injury_img, (soldier_x, soldier_y))

    elif soldier_img:
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