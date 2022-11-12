# this code is a bmi calculator
from rich import print as rprint

print("Welcome to the bmi calculator :D")
weight : int = int(input("Please insert your weight in kg (whole number) (don't cheat :< ): "))
height : float = float(input("Please insert your height in metres (decimal): "))
bmi : float = (weight/(height ** 2))

if bmi < 18.5:
    rprint(f"Your bmi is [blue]{round(bmi, 2)}[/blue]\nIt seems you are [bold blue]underweight[/bold blue]")
elif bmi < 24.9:
    rprint(f"Your bmi is [green]{round(bmi, 2)}[/green]\nIt seems you have [bold green]normal weight[/bold green]")
else:
    rprint(f"Your bmi is [red]{round(bmi, 2)}[/red]\nIt seems you are [bold red]obese[/bold red]")