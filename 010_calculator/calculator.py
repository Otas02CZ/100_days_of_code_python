# this is a simple calculator

from rich.prompt import IntPrompt, Prompt

logo : str = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \\     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \\_|  | || |    / /\\ \\    | || |    | |       | || |  / .'   \\_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \\   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \\ `.___.'\\  | || | _/ /    \\ \\_ | || |   _| |__/ |  | || |  \\ `.___.'\\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def calculate(num_a : float, num_b : float, operation : str) -> tuple[float, str]:
    match operation:
        case "+":   result: float = num_a + num_b; return result, f"{num_a} {operation} {num_b} = {result}"
        case "-":   result: float = num_a - num_b; return result, f"{num_a} {operation} {num_b} = {result}"
        case "*":   result: float = num_a * num_b; return result, f"{num_a} {operation} {num_b} = {result}"
        case "/":
            if num_b == 0:
                return 0, "Cannot divide by zero"
            else:
                result: float = num_a / num_b; return result, f"{num_a} {operation} {num_b} = {result}"
        case  _ :
            return 0, "unknown"

def get_number(which : str) -> float:
    return IntPrompt.ask(f"Please insert the {which} number")

def get_operation() -> str:
    return Prompt.ask("Please specify the operation", choices=["+", "-", "*", "/"])

def get_choose_next() -> str:
    return Prompt.ask("Do you want to continue calculation with your current number, or no? Or would you like to end", choices=["yes", "no", "end"])

print(logo)
print("Welcome to the calculator!!")

use_last : bool = False
number_a : float = 0

while 1:
    if not use_last:
        number_a : float = get_number("first")
    operation : str = get_operation()
    number_b : float = get_number("second")
    msg : str
    result : float
    result, msg = calculate(number_a, number_b, operation)
    print(msg)
    match get_choose_next():
        case "yes":
            number_a = result
            use_last = True
        case "no":
            use_last = False
        case "end":
            print("Thank you for being here, the Interpreter is pleased by your presence.")
            break
