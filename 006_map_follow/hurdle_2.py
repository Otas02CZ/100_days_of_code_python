def turn_right():
    for _x in range(3):
        turn_left()

while not at_goal():
    if front_is_clear():
        move()
    else:
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()