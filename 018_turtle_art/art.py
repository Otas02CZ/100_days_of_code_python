

# import colorgram

# rgb_colors : list[tuple] = []
# colors : list = colorgram.extract("018_turtle_art/image.jpg", 30)

# for color in colors:
#     r : float = color.rgb.r
#     g : float = color.rgb.g
#     b : float = color.rgb.b
#     rgb_colors.append((r, g, b))

# print(rgb_colors)

rgb_colors : list[tuple] = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]


from turtle import Turtle, Screen
import turtle
from random import choice


turtle.colormode(255)
jim : Turtle = Turtle()

jim.speed(10)
jim.penup()
jim.hideturtle()
jim.setheading(225)
jim.forward(300)
jim.setheading(0)
number_of_dots : int = 100


for dot_count in range(1, number_of_dots + 1):
    jim.dot(20, choice(rgb_colors))
    jim.forward(50)
    if dot_count % 10 == 0:
        jim.setheading(90)
        jim.forward(50)
        jim.setheading(180)
        jim.forward(500)
        jim.setheading(0)

screen = Screen()
screen.exitonclick()

