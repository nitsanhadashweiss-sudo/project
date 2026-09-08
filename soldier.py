import consts
import game_field
import main

corner=(0,0)

def clean_soldier():
    for row in range(consts.SOLDIER_ROWS):
        for col in range(consts.SOLDIER_COLS):
            if game_field.field[row][col]==consts.HEAD or game_field.field[row][col]==consts.LEGS:
                game_field.field[row][col] = consts.EMPTY


def soldier(x,y):
    clean_soldier()
    global corner
    corner=(x,y)
    for row in range (y,y+consts.SOLDIER_BODY_ROWS-1):
        for col in range (x,x+consts.SOLDIER_COLS):
            if game_field.field[row][col]==consts.EMPTY:
                game_field.field[row][col]=consts.HEAD
            elif game_field.field[row][col]==consts.FLAG:
                main.win()
    for col in range (x,x+consts.SOLDIER_COLS):
        if game_field.field[y+consts.SOLDIER_BODY_ROWS][col] == consts.EMPTY:
            game_field.field[y+consts.SOLDIER_BODY_ROWS][col]=consts.LEGS
        if game_field.field[y+consts.SOLDIER_BODY_ROWS][col] == consts.MINE:
            main.lose()

def can_move (action):
    global corner
    if action==1:
        if corner[1]==0:
            return False
    if action==2:
        if corner[0]==0:
            return False
    if action==3:
        if corner[1]==consts.SOLDIER_COLS:
            return False
    if action==4:
        if corner[0]==consts.SOLDIER_BODY_ROWS:
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


