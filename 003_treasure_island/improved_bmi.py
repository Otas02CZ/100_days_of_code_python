# this code is an improved bmi calculator
from rich import print as rprint

print("Welcome to the improved bmi calculator :D")
weight : float = float(input("Please insert your weight in kg (whole number) (don't cheat :< ): "))
height : float = float(input("Please insert your height in metres (decimal): "))
bmi : float = round(weight/(height ** 2))

if bmi < 18.5:
    rprint(f"Your bmi is [blue]{bmi}[/blue], so it seems you are [bold blue]underweight[/bold blue]")
elif bmi < 25:
    rprint(f"Your bmi is [green]{bmi}[/green], so it seems you have [bold green]normal weight[/bold green]")
elif bmi < 30:
    rprint(f"Your bmi is [red]{bmi}[/red], so it seems you are [bold red]overweight[/bold red]")
elif bmi < 35:
    rprint(f"Your bmi is [red]{bmi}[/red], so it seems you are [bold red]obese[/bold red]")
else:
    rprint(f"Your bmi is [red]{bmi}[/red], so it seems you are [bold red]clinically obese[/bold red]")
