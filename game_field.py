import consts
import random
import soldier

field=[]

def create_field():
    global field
    #make the whole field empty
    field=[[consts.EMPTY for c in range(consts.BOARD_COLS)] for i in range(consts.BOARD_ROWS)]

    #put HEAD
    for r in range(0,consts.SOLDIER_BODY_ROWS):
        for c in range(0,consts.SOLDIER_COLS):
            field[r][c]=consts.HEAD

    #put LEGS
    start_feet=consts.SOLDIER_BODY_ROWS
    end_feet=consts.SOLDIER_BODY_ROWS+consts.SOLDIER_FEET_ROWS
    for r in range(start_feet,end_feet):
        for c in range(0,consts.SOLDIER_COLS):
            field[r][c] = consts.LEGS


    #put FLAG at end
    start_r_f=consts.BOARD_ROWS-consts.FLAG_ROWS
    start_c_f=consts.BOARD_COLS-consts.FLAG_COLS
    for r in range(start_r_f,consts.BOARD_ROWS):
        for c in range(start_c_f,consts.BOARD_COLS):
            field[r][c]=consts.FLAG

    add_random_mines()


def create_row(row_number):
    pass


def add_random_mines():
    global field
    count = 0

    while count != consts.MINES_COUNT:
        rand_r = random.randint(0, consts.BOARD_ROWS - 1)  # but can't where soldier
        rand_c = random.randint(0, consts.BOARD_COLS - 1)

        place=field[rand_r][rand_c]
        if place!=consts.HEAD and place!=consts.LEGS and place!=consts.FLAG and place!=consts.MINE:  # not where soldier starts and not where flag
            field[rand_r][rand_c] = consts.MINE  # add on that place mine
            count += 1