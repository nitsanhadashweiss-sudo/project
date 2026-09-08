# import consts
# import pygame
# import game_field
#
# # pygame setup
# pygame.init()

# clock = pygame.time.Clock()
# running = True
# dt = 0
#
# player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
#
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     # fill the screen with a color to wipe away anything from last frame
#     screen.fill(consts.GREEN)
#
#     # SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
#     # soldier_img=pygame.image.load("soldier.png") #soooolldierr
#     # imagerect = soldier_img.get_rect()
#     # screen.blit(soldier_img, imagerect)
#     # pygame.draw.circle(screen, "red", player_pos, 40)
#     # SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
#
#
#
#     # pygame.draw.circle(screen, "red", player_pos, 40)
#
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_UP]:
#         player_pos.y -= 300 * dt
#     if keys[pygame.K_DOWN]:
#         player_pos.y += 300 * dt
#     if keys[pygame.K_LEFT]:
#         player_pos.x -= 300 * dt
#     if keys[pygame.K_RIGHT]:
#         player_pos.x += 300 * dt
#
#     # flip() the display to put your work on screen
#     pygame.display.flip()
#
#     # limits FPS to 60
#     # dt is delta time in seconds since last frame, used for framerate-
#     # independent physics.
#     dt = clock.tick(60) / 1000
#
# pygame.quit()
#
#
# #https://stackoverflow.com/questions/8873219/how-can-i-draw-images-and-sprites-in-pygame





















#-------------------------------------------------------------------------------------------------------------
import consts
import pygame
import game_field
screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
#
# # pygame setup
# pygame.init()
# screen = pygame.display.set_mode((1280, 720))
# clock = pygame.time.Clock()
# running = True
# dt = 0
#
# # player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
# player_pos = pygame.Vector2(0, 0)
#
# background=game_field.field
#
#
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     # fill the screen with a color to wipe away anything from last frame
#     screen.fill(consts.GREEN)
#
#     # SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
#     # soldier_img=pygame.image.load("soldier.png") #soooolldierr
#     # imagerect = soldier_img.get_rect()
#     # screen.blit(soldier_img, imagerect)
#     # pygame.draw.circle(screen, "red", player_pos, 40)
#     # screen = create_graphics_screen()
#     # for i in range(6):
#     #     screen.blit(background[i], (i * 10, 0))
#     # playerpos = 3
#     # screen.blit(playerimage, (playerpos * 10, 0))
#     # SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
#
#
#
#     # pygame.draw.circle(screen, "red", player_pos, 40)
#
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_UP]:
#         player_pos.y -= 300 * dt
#     if keys[pygame.K_DOWN]:
#         player_pos.y += 300 * dt
#     if keys[pygame.K_LEFT]:
#         player_pos.x -= 300 * dt
#     if keys[pygame.K_RIGHT]:
#         player_pos.x += 300 * dt
#
#     # flip() the display to put your work on screen
#     pygame.display.flip()
#
#     # limits FPS to 60
#     # dt is delta time in seconds since last frame, used for framerate-
#     # independent physics.
#     dt = clock.tick(60) / 1000
#
# pygame.quit()







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




















#https://www.pygame.org/docs/tut/MoveIt.html