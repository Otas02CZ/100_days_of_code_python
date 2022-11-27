from turtle import Turtle, Screen
import turtle
from random import randint

def draw_square(jimmy : Turtle) -> None:
    for i in range(4):
        jimmy.forward(100)
        jimmy.left(90)

def draw_dashed_line(terry : Turtle) -> None:
    for i in range(10):
        terry.forward(20)
        terry.penup()
        terry.forward(20)
        terry.pendown()

def random_color() -> tuple:
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

# def random_color() -> str:
#     colors : list = ["red", "green", "blue", "yellow", "black", "pink", "orange"]
#     return colors[randint(0, len(colors)-1)]


def draw_multiple_shapes(tim : Turtle) -> None:
    for corners in range(3, 16):
        angle : float = 360/corners
        tim.color(random_color())
        for _ in range(0, corners):
            tim.forward(100)
            tim.right(angle)

def random_walk(luke : Turtle) -> None:
    luke.speed(10)
    luke.pensize(10)
    for _ in range(100, randint(200, 400)):
        match randint(0, 3):
            case 0: pass
            case 1: luke.left(90)
            case 2: luke.right(90)
            case 3: luke.left(180)
        luke.color(random_color())
        luke.forward(40)
   
def draw_spirograph(yorn : Turtle, gap_size : int) -> None:
    yorn.speed(0)
    for _ in range(int(360/ gap_size)):
        yorn.color(random_color())
        yorn.circle(100)
        yorn.setheading(yorn.heading() + gap_size)



jimmy : Turtle = Turtle()
turtle.colormode(255)
jimmy.shape("turtle")
jimmy.color("red")

# draw_square(jimmy)
# draw_dashed_line(jimmy)
# draw_multiple_shapes(jimmy)
# random_walk(jimmy)
# draw_spirograph(jimmy, 5)

screen = Screen()
screen.exitonclick()
