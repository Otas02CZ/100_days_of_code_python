# this code can calculate how many cans of paint are needed to paint a wall of given dimensions
from rich.prompt import FloatPrompt
from math import ceil
print("Welcome to the paint area calculator")
can_capacity : float = FloatPrompt.ask("How many square metres can be painted with your can?")
area_x : float = FloatPrompt.ask("Tell me the width of the area in metres")
area_y : float = FloatPrompt.ask("Tell me the height of the area in metres")

def calc_can_count(can_cap : float, x : float, y : float) -> float:
    return (x * y) / can_cap

cans_needed : float = calc_can_count(can_capacity, area_x, area_y)
cans_ceiled : int = ceil(cans_needed)
print(f"You will need {cans_ceiled} cans to completely cover the area.")
left_in_can : float = cans_ceiled - cans_needed
if left_in_can != 0:
    print(f"{round(left_in_can*100)}% will remain in last can.")
else:
    print("You will use up all the cans.")