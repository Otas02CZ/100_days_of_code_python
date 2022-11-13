# this program will tell whether the inputed number is oddd or even

from rich.prompt import IntPrompt

input_number : int = IntPrompt.ask("Please insert a whole number")

if input_number % 2 == 0:
    print(f"{input_number} is even")
else:
    print(f"{input_number} is odd")