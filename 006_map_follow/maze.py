def turn_right():
    for _x in range(3):
        turn_left()
  
while not at_goal():
    if not wall_on_right():
        turn_right()
        if not wall_in_front():
            move()
    elif not wall_in_front():
        move()
    else:
        turn_left()