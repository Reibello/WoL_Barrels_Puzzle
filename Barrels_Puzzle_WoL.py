#Barrels_and_Dials.py
import copy

NUM_BARRELS = 3
MIN_VALUE = 1
MAX_VALUE = 22

BARREL_DELTA = 1

#HACK START FOR NOW
b_left = 10
b_mid = 11
b_right = 12
barrels = [b_left, b_mid, b_right]

def check_input(s):
    s = s.upper()
    if s == 'LEFT':
        return 0
    elif s == 'MIDDLE':
        return 1
    elif s == 'RIGHT':
        return 2
    else:
        return -1

def increment_barrel(b, brls):
    if b < 0:
        print("ERROR 1")
        return brls
    if brls[b] == MAX_VALUE:
        return brls
    new = copy.copy(brls)
    for i in range(len(brls)):
        if i == b:
            pass
        else:
            if brls[i] > MIN_VALUE:
                new[i] -= BARREL_DELTA
                new[b] += BARREL_DELTA
    return new
            
#BODY - HACK START
while (barrels[0] != barrels[1] or barrels[1] != barrels[2]):
    print("left=", barrels[0], "middle=", barrels[1], "right=", barrels[2])
    b_sel = input("Choose Barrel to increment (LEFT, MIDDLE, RIGHT)")
    b_index = check_input(b_sel)
    barrels = increment_barrel(b_index, barrels)
    


    
                    
                
            
    
