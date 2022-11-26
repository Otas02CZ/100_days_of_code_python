# slightly modified version of the higher lower game

from options_database import options, options_len
from random import randint
from rich.prompt import Prompt, IntPrompt
from art import vs, logo
from os import system

def random_option(used_options : list) -> int:
    index : int = -1
    tries : int = 0
    while 1:
        try:
            index = randint(0, options_len-1)
            used_options.index(index)
            tries += 1
            if tries > 1000:
                return -1
        except:
            return index
    return index

def generate_append_option(used_options : list) -> bool:
    new_option_index = random_option(used_options)
    if new_option_index == -1:
        return False
    else:
        used_options.append(new_option_index)
        return True

def show_current_options(used_options : list, show_last : bool) -> None:
    index = len(used_options)-2
    print(f"Option A : {options[used_options[index]][0]} has {options[used_options[index]][1]} views.")
    print(vs)
    if show_last:
        print(f"Option B : {options[used_options[index+1]][0]} has {options[used_options[index+1]][1]} views.")
    else:
        print(f"Option B : {options[used_options[index+1]][0]}.")

def user_choice() -> str:
    return Prompt.ask("Please give me you choice", choices=["A", "B", "exit"])

def guessed_right(used_options : list, choice : str) -> bool:
    item_a = options[used_options[len(used_options)-2]][1]
    item_b = options[used_options[len(used_options)-1]][1]
    match choice:
        case "A": return True if item_a >= item_b else False
        case "B": return True if item_b >= item_a else False
        case  _ : return False

used_options : list = []
score : int = 0
guessed_all : bool = False
first_run : bool = True
quited : bool = False
show_last : bool = False

while 1:
    system("clear")
    print(logo)
    if first_run:
        print("Welcome to the higher lower game:D\n")
        generate_append_option(used_options)
    if not generate_append_option(used_options):
        guessed_all = True
        break
    print("Which one do you think has more searches on google ?")
    show_current_options(used_options, show_last)
    choice : str = user_choice()
    match choice:
        case "exit":
            quited = True
            break
        case "A":
            if guessed_right(used_options, "A"):
                score += 1
                print("You guessed correctly")
                show_current_options(used_options, True)
                item_b : int = used_options.pop()
                item_a : int = used_options.pop()
                used_options.append(item_b)
                used_options.append(item_a)
            else:
                print("You didn't guess correctly")
                show_current_options(used_options, True)
                break
        case "B":
            if guessed_right(used_options, "B"):
                score += 1
                print("You guessed correctly")
                show_current_options(used_options, True)
            else:
                print("You didn't guess correctly")
                show_current_options(used_options, True)
                break
    input("Press enter for a next round.")
    if first_run:
        first_run = False

if score !=0:
    print(f"Your score is {score}")
    if score < 3:
        print("Well, you did not play very well.")
    elif score <5:
        print("Not great, not terrible, yet you are still better than many others.")
    elif score <8:
        print("A very nice score, kudos for that!!")
    elif score >10:
        print("Aren't you a god??")
    elif guessed_all:
        print("You are a god, that is certain.")
else:
    if first_run and quited:
        print("You just quit the game, didn't you?")
    else:
        print("Try again, ...... or maybe rather not?")