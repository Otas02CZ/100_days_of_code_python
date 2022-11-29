from turtle import Turtle, Screen
from random import randint


def color_text(colors : list[str]) -> str:
    text : str = "("
    for color in colors:
        text += color + ", "
    text = text[:-2] + ")"
    return text

def add_turtles(turtles : list[Turtle], colors : list[str]) -> None:
    y = -100
    for color in colors:
        turtle : Turtle = Turtle(shape="turtle")
        turtle.color(color)
        turtle.penup()
        turtle.goto(x=-230, y=y)
        turtle.speed(10)
        turtles.append(turtle)
        y += 20

def move_turtle_randomly(turtle : Turtle) -> None:
    turtle.forward(randint(4, 12))

def check_winning(turtle : Turtle) -> bool:
    if turtle.pos()[0] >= 230:
        return True
    else:
        return False

defined_colors : list[str] = ["red", "blue", "yellow", "green", "pink", "purple", "brown", "cyan", "magenta"]
turtles : list[Turtle] = []    
    
screen = Screen()
screen.setup(width=500, height=400)
bet_color : str = str(screen.textinput(title="Bet please", prompt=f"Which turtle will win the race? Enter a color:\n{color_text(defined_colors)}"))



add_turtles(turtles, defined_colors)

running : bool = True

while running:
    for turtle in turtles:
        move_turtle_randomly(turtle)
        if check_winning(turtle):
            if turtle.pencolor() == bet_color:
                print("Yep, your turtle won, you are winning $0")
                
            else:
                print("Unfortunately your turtle lost. Give it more lettuce and it might win next time.")
            running = False
            break
        else:
            continue


# jim = Turtle(shape="turtle")
# jim.color("blue")
# jim.penup()
# jim.goto(x=-230, y=-100)

screen.exitonclick()