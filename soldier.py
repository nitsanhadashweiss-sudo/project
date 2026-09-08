import consts




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