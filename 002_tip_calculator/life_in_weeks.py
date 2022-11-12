# program to calculate life in weeks and show visual representation
from rich import print as rprint

print("""This program will calculate how many days, weeks, months and years
you have left depending on your age, if you were to die aged 90 and it also
shows a visual representation of your life""")
age : int = int(input("Write you age please and .... don't be afraid :) : "))

max_age : int = 90
max_months : int = max_age * 12
max_weeks : int = int(max_age * (365.25/7))
max_days : int = int(max_age * 365.25)

your_months : int = age * 12
your_weeks : int = int(age * (365.25/7))
your_days : int = int(age * 365.25)
print(max_days, max_weeks, max_months, max_age)
print(your_days, your_weeks, your_months, age)
print(f"You have {max_days - your_days} days, {max_weeks - your_weeks} weeks, {max_months - your_months} months and {max_age - age} years left.")

def visual_str_creator(y_size : int, x_size : int, compared_data : int, data_name : str) -> str:
    table : str = ""
    index : int = 0
    for y in range(y_size):
        for x in range(x_size):
            index += 1
            
            if index < compared_data:
                table += "[yellow] x [/yellow]"
            elif index > compared_data and index < 4696:
                table += "[blue] x [/blue]"
            elif index == compared_data:
                table += "[bold green] x [/bold green]"
        table += "\n"
    table += f"Your life in {data_name} visualisation"
    return table

rprint(visual_str_creator(9, 10, age, "years"))
rprint(visual_str_creator(30, 36, your_months, "months"))
rprint(visual_str_creator(91, 52, your_weeks, "weeks"))
    