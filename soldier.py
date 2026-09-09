import consts
import game_field

corner=(0,0)
touch_flag=False
touch_mine=False

def clean_soldier():
    for row in range(consts.SOLDIER_ROWS):
        for col in range(consts.SOLDIER_COLS):
            if game_field.field[row][col]==consts.HEAD or game_field.field[row][col]==consts.LEGS:
                game_field.field[row][col] = consts.EMPTY


def soldier(x,y):
    global touch_flag
    global touch_mine
    clean_soldier()
    global corner
    corner=(x,y)
    for row in range (y,y+consts.SOLDIER_BODY_ROWS-1):
        for col in range (x,x+consts.SOLDIER_COLS):
            if game_field.field[row][col]==consts.EMPTY:
                game_field.field[row][col]=consts.HEAD
            elif game_field.field[row][col]==consts.FLAG:
                touch_flag=True
    for col in range (x,x+consts.SOLDIER_COLS):
        if game_field.field[y+consts.SOLDIER_BODY_ROWS][col] == consts.EMPTY:
            game_field.field[y+consts.SOLDIER_BODY_ROWS][col]=consts.LEGS
        if game_field.field[y+consts.SOLDIER_BODY_ROWS][col] == consts.MINE:
            touch_mine=True

def can_move (action):
    global corner
    if action==1:
        if corner[1]==0:
            return False
    if action==2:
        if corner[0]==0:
            return False
    if action==3:
        if corner[1]==consts.BOARD_ROWS-1:
            return False
    if action==4:
        if corner[0]==consts.BOARD_COLS-1:
            return False
    return True


def soldier_move(action):
    if can_move(action):
        if action==1:
            soldier(corner[0],corner[1]-1)
        if action==2:
            soldier(corner[0]-1,corner[1])
        if action==3:
            soldier(corner[0],corner[1]+1)
        if action==4:
          soldier(corner[0]+1,corner[1])

message=""

def game_state():
    global touch_flag
    global touch_mine
    if touch_flag:
        return consts.WIN_MESSAGE
    elif touch_mine:
        return consts.LOSE_MESSAGE
    else:
        return "0"

