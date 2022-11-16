def turn_right():
    for _x in range(3):
        turn_left()
  
while not at_goal():
    if not right_is_clear():
        if not front_is_clear():
            turn_left()
        else:
            move()
    else:
        turn_right()
        if front_is_clear():
            move()