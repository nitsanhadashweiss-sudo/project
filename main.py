import consts
import screen
import soldier
import game_field
import time

game_field.create_field()

running = True


running = True
while running:
    screen.fill(COLOR_PANEL)
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if current_time - last_move_time > move_delay:
        dr, dc = 0, 0
        if keys[pygame.K_UP]:
            dr = -1
        elif keys[pygame.K_DOWN]:
            dr = 1
        elif keys[pygame.K_LEFT]:
            dc = -1
        elif keys[pygame.K_RIGHT]:
            dc = 1

        if dr != 0 or dc != 0:
            player_r, player_c, pts, mine = move_player(dungeon, player_r, player_c, dr, dc)
            score += pts
            if mine:
                lives -= 1
                print("BOOM! Hit a mine. Lives left:", lives)
            last_move_time = current_time

    remaining = count_remaining_diamonds(dungeon)
    if remaining == 0:
        level += 1
        print(f"Level {level} Complete! Generating new dungeon...")
        dungeon = generate_random_dungeon(GRID_ROWS, GRID_COLS)
        player_r, player_c = 1, 1

    for r in range(GRID_ROWS):
        for c in range(GRID_COLS):
            # באג 6 תוקן: c מייצג X (עמודה) ו-r מייצג Y (שורה)
            rect_x = c * CELL_SIZE
            rect_y = r * CELL_SIZE

            tile_type = dungeon[r][c]
            color = COLOR_EMPTY
            if tile_type == TILE_WALL:
                color = COLOR_WALL
            elif tile_type == TILE_DIAMOND:
                color = COLOR_DIAMOND
            elif tile_type == TILE_MINE:
                color = COLOR_MINE

            pygame.draw.rect(screen, color, (rect_x, rect_y, CELL_SIZE - 2, CELL_SIZE - 2))

    player_x = player_c * CELL_SIZE + 4
    player_y = player_r * CELL_SIZE + 4
    pygame.draw.rect(screen, COLOR_PLAYER, (player_x, player_y, CELL_SIZE - 8, CELL_SIZE - 8))

    nearest_pos, dist = find_nearest_diamond(dungeon, player_r, player_c)
    dist_str = f"{dist:.1f}" if nearest_pos else "N/A"

    info_str = f"Score: {score} | Lives: {lives} | Level: {level} | Nearest Diamond: {dist_str} tiles"
    txt_surface = FONT.render(info_str, True, COLOR_TEXT)
    screen.blit(txt_surface, (10, HEIGHT - 40))

    if lives <= 0:
        print("GAME OVER!")
        running = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()




















for row in game_field.field:
    print(row)




def lose():
    pass
    #legs to mine


def win():
    pass
    #body to flag
