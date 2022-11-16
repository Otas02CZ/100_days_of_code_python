def turn_right():
    for _x in range(3):
        turn_left()
x = 0
while x<6:
    x += 1
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()