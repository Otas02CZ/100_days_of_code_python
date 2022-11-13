# this code is a leap year checker

from rich.prompt import IntPrompt

print("Welcome to the leap year checker application :D")
year : int = IntPrompt.ask("Enter a year please")

if year <0:
    print("You inputed a very interesting year :D")

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"Year {year} is a leap year")
else:
    print(f"Year {year} is not a leap year")
    