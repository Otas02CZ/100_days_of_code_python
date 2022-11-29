from turtle import Turtle, Screen

jim : Turtle = Turtle()
screen = Screen()

def move_forwards() -> None:
    jim.forward(10)

def turn_left() -> None:
    jim.left(10)

def turn_right() -> None:
    jim.right(10)

def move_backwards() -> None:
    jim.back(10)

def exit_game() -> None:
    screen.exitonclick()

def clear() -> None:
    jim.clear()
    jim.penup()
    jim.home()
    jim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="s", fun=move_backwards)
screen.exitonclick()