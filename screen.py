import pygame
import consts

pygame.init()
screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
pygame.display.set_caption("Flag Game")

soldier_img =pygame.transform.scale(
        pygame.image.load(consts.SOLDIER_IMAGE),
        (consts.SOLDIER_COLS * consts.CELL_SIZE, consts.SOLDIER_ROWS * consts.CELL_SIZE))
bush_img =pygame.transform.scale(
        pygame.image.load(consts.BUSH_IMAGE),
        (consts.CELL_SIZE, consts.CELL_SIZE))
mine_img =pygame.transform.scale(
        pygame.image.load(consts.MINE_IMAGE),
        (consts.MINE_COLS * consts.CELL_SIZE, consts.MINE_ROWS * consts.CELL_SIZE))

soldier_night=pygame.transform.scale(
        pygame.image.load(consts.SOLDIER_NIGHT),
        (consts.SOLDIER_COLS * consts.CELL_SIZE, consts.SOLDIER_ROWS * consts.CELL_SIZE))

# soldier_injury=pygame.transform.scale(
#         pygame.image.load(consts.SOLDIER_INJURY),
#         (consts.SOLDIER_COLS * consts.CELL_SIZE, consts.SOLDIER_ROWS * consts.CELL_SIZE))




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
            # elif field[r][c]==consts.SOLDIER and soldier_pos: #dellll
            elif field[r][c]==consts.SOLDIER_IMAGE and not show_mines: #and not injury
                screen.blit(soldier_img,(x, y))
            elif field[r][c]==consts.SOLDIER_IMAGE and show_mines:
                screen.blit(soldier_night,(x, y))
            # elif field[r][c]==consts.SOLDIER_IMAGE and INJURY:
            #     screen.blit(soldier_injury,(x, y))



    if soldier_img:
        soldier_x=soldier_pos[0]*consts.CELL_SIZE
        soldier_y=soldier_pos[1]*consts.CELL_SIZE
        screen.blit(soldier_img, (soldier_x, soldier_y))

    pygame.display.flip()


def draw_message(msg):
    font = pygame.font.SysFont(consts.FONT_NAME, consts.FONT_SIZE)
    text_img = font.render(msg, True, consts.BLACK)
    # screen.blit(rendered_text, (consts.WINDOW_WIDTH // 2 - 50, consts.WINDOW_HEIGHT // 2)) #
    screen.blit(text_img, (0,0))
    pygame.display.flip()