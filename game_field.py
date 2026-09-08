import consts
import random
import soldier

field=[]

def create_field():
    # global field
    # #make the whole field empty
    # field=[[consts.EMPTY]*consts.BOARD_COLS for i in range(consts.BOARD_ROWS)]
    #
    # #put soldier at start
    # # for i in range(consts.SOLDIER_ROWS*consts.SOLDIER_COLS):
    # for r in range(0,consts.SOLDIER_BODY_ROWS):
    #     for c in range(0,consts.SOLDIER_FEET_ROWS):
    #         field[r][c]=consts.HEAD
    #
    # for r in range(consts.SOLDIER_BODY_ROWS, consts.SOLDIER_BODY_ROWS + consts.SOLDIER_FEET_ROWS):
    #     for c in range(0,consts.SOLDIER_FEET_ROWS):
    #         field[r][c] = consts.LEGS
    #
    # # soldier.soldier(0,0)
    #
    # #put flag at end
    # for i in range(consts.FLAG_ROWS*consts.FLAG_COLS):
    #     for r in range(len(field)-1,0,-1):
    #         for c in range(len(field[r])-1,0,-1):
    #             if r>len(field)-1-consts.FLAG_ROWS and c>len(field[r])-1-consts.FLAG_COLS:
    #                 field[r][c]=consts.FLAG

    global field
    #make the whole field empty
    field=[[consts.EMPTY]*consts.BOARD_COLS for i in range(consts.BOARD_ROWS)]

    #put soldier at start
    # for r in range(0,consts.SOLDIER_BODY_ROWS):
    #     for c in range(0,consts.SOLDIER_COLS):
    #         field[r][c]=consts.HEAD
    #
    # for r in range(consts.SOLDIER_BODY_ROWS, consts.SOLDIER_BODY_ROWS + consts.SOLDIER_FEET_ROWS):
    #     for c in range(0,consts.SOLDIER_COLS):
    #         field[r][c] = consts.LEGS

    soldier.soldier(0,0)

    # #put flag at end
    # for i in range(consts.FLAG_ROWS*consts.FLAG_COLS):
    #     for r in range(len(field)-1,0,-1):
    #         for c in range(len(field[r])-1,0,-1):
    #             if r>len(field)-1-consts.FLAG_ROWS and c>len(field[r])-1-consts.FLAG_COLS:
    #                 field[r][c]=consts.FLAG



create_field()
# print(field)
for row in field:
    print(row)


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

