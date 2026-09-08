import consts
import random
import soldier

field=[]

def create_field():
    global field
    #make the whole field empty
    field=[[consts.EMPTY]*consts.BOARD_COLS for i in range(consts.BOARD_ROWS)]

    #put soldier at start
    # for i in range(consts.SOLDIER_ROWS*consts.SOLDIER_COLS):
    #     for r in range(len(game_field)):
    #         for c in range(len(game_field[r])):
    #             if c<consts.SOLDIER_COLS and r<:
    soldier.soldier(0,0)




def create_row(row_number):
    pass


def add_random_mines():
    global field
    count = 0

    while count != consts.MINES_COUNT:
        rand_r = random.randint(0, consts.BOARD_ROWS - 1)  # but can't where soldier
        rand_c = random.randint(0, consts.BOARD_COLS - 1)

        place=field[rand_r][rand_c]
        if place!=consts.SOLDIER and place!=consts.FLAG:  # not where soldier starts and not where flag
            field[rand_r][rand_c] = consts.MINE  # add on that place mine
            count += 1

