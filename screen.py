import pygame
import consts
import game_field

screen = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
def draw_message(message):
    font = pygame.font.SysFont(consts.FONT_NAME, consts.FONT_SIZE)
    text_img = font.render(message, True, consts.BLACK)
    screen.blit(text_img, consts.LOCATION)

    def draw_soldier():
        soldier_img = pygame.image.load(consts.SOLDIER_IMAGE)
        imagerect = soldier_img.get_rect()

        while True:
            # screen.fill(consts.BLACK)
            screen.blit(soldier_img, imagerect)
            pygame.display.flip()

    def draw_mine():
        pass

    def draw_bush():
        pass

    def draw_game():
        screen.fill(consts.GREEN)

        draw_soldier()

        pygame.display.flip()


def draw_grid():
    for i in range(consts.BOARD_ROWS):
        pygame.draw.line(screen,(0,i),(consts.WINDOW_WIDTH,i),(consts.WINDOW_WIDTH,i))

