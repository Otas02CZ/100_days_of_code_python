# this code can check whether the inputed number is a prime

from rich.prompt import IntPrompt

print("Welcome to the prime number checker :D")

number : int = IntPrompt.ask("Give me a number you want me to check")

if number < 0:
    print("The number will be inverted in positive sense")
    number *= -1
if number == 0:
    print(f"{number} is not a prime.")
elif number == 1:
    print(f"{number} is not a prime.")
else:
    prime : bool = True
    for divisor in range(2, number-1):
        if (number % divisor) == 0:
            prime = False
            break
    if prime:
        print(f"{number} is a prime.")
    else:
        print(f"{number} is not a prime.")