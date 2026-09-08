import consts
import screen
import soldier
import game_field
import time
import pygame

game_field.create_field()


running = True
while running:
    screen.fill(consts.COLOR_BACKGROUND)
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

soldier.soldier_move(action)



    if lives <= 0:
        print("GAME OVER!")
        running = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()

def win():

    time.sleep(3)
    pass

def lose():

    pass
