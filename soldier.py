import consts
import game_field


def soldier(x,y):
    for row in range (y,y+consts.SOLDIER_BODY_ROWS-1):
        for col in range (x,x+consts.SOLDIER_COLS):
            game_field.field()[row][col]="HEAD"
    for col in range (x,x+consts.SOLDIER_COLS):
        game_field.field()[y+consts.SOLDIER_BODY_ROWS][col]="LEGS"


def move (action)
    if action==1:
        for











def touch_flag(): #[(0,0),(0,1)]
    #body
    pass

#gets list of leg places in matrix, and list of flag places in matrix
def touch_mine(lst_legs, lst_mine): #[(0,0),(0,1)]
    for leg in lst_legs:
        if leg in lst_mine:
            return True
    return False



    #win message 3 seconds
    pass