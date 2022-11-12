# this code can calculate tip given by each person from the user input

from rich.prompt import IntPrompt, FloatPrompt

print("Welcome to the tip calculator")
total_bill : float = FloatPrompt.ask("What was the total bill? $")
tip_percentage : int = IntPrompt.ask("What percentage tip would you like to give?", choices=["10", "12", "15"])
people_count : int = IntPrompt.ask("How many people to split the bill?")
bill_with_tip : float = total_bill * (1 + tip_percentage/100)
print(f"Each person should pay: ${round(bill_with_tip / people_count, 2)}")