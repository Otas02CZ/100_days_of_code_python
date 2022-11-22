# a simple number guessing game

from art import logo
from rich.prompt import Prompt, IntPrompt
from random import randint
from os import system

def wanna_continue() -> bool:
    if Prompt.ask("Do you want to play again?", choices=["yes", "no"]) == "yes":
        return True
    else:
        return False

def choose_diff() -> int:
    match Prompt.ask("Please choose the difficulty.", choices=["hard", "easy"]):
        case "hard":    return 5
        case "easy":    return 10
        case    _  :    return 10

def guess_number() -> int:
    number : int = 0
    while number < 1 or number > 100:
        number = IntPrompt.ask("What is your guess? <1, 100>")
        if number < 1 or number > 100:
            print("Please guess a number in the given range, as .. as I did.")
    return number

running : bool = True
first : bool = True


while running:
    system("cls")
    print(logo)
    if first:
        print("Welcome to the number guessing game :D")
        first = False
    print("I'm guessing a number between 1 and 100.")
    number : int = randint(1, 100)
    guess : int = 0
    remaining_attempts : int = choose_diff()
    
    while remaining_attempts != 0:
        print(f"You have {remaining_attempts} remaining attemtps.")
        guess = guess_number()
        if guess == number:
            print("Correct, you got my number. Well done.")
            break
        else:
            remaining_attempts -= 1
            if guess > number:
                print("Too high.")
            else:
                print("Too low.")
    
    if remaining_attempts == 0:
        print("Well, it seems you have ran out of attempts. Eat some cabbage, it might do you some good.")
        print(f"The number was {number}.")
    
    
    running = wanna_continue()
print("Bye, Bye. I'm looking forward to another round of guessing.")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
