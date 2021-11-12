def turn_right():
    turn_left()
    turn_left()
    turn_left()    

def jump():
    # move()
    turn_left()
    while right_is_clear() == False:
        # if wall_in_front:
        move()
    turn_right()
    move()
    turn_right()
    while wall_in_front() == False:
        #if wall_in_front:
        move()
    turn_left()

while at_goal() == False:
    if wall_in_front():
        jump()
    elif front_is_clear():
        move()

# for i in range(6):
#    jump()
    
#while at_goal() == False:
#    jump()
