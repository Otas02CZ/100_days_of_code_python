# a simple coffee machine simulator

from data import STARTING_RESOURCES, MENU, PENNY, DIME, NICKEL, QUARTER, COFFEE_IMG, LOGO_IMG
from rich.prompt import Prompt, IntPrompt
from rich.progress import track
from random import randint
import hashlib, time
from os import system

def print_report(res : dict) -> None:
    print(f"water - {res['water']}\nmilk - {res['milk']}\ncoffee - {res['coffee']}\nmoney - {res['money']}")

def authorize(password : str) -> bool:
    return password == Prompt.ask("hey mister, password?")

def insert_money() -> float:
    money : list[int] = [0, 0, 0, 0]
    money[0] = IntPrompt.ask("Please insert pennies (the count)")
    money[1] = IntPrompt.ask("Please insert dimes (the count)")
    money[2] = IntPrompt.ask("Please insert nickels (the count)")
    money[3] = IntPrompt.ask("Please insert quarters (the count)")
    return money[0]*PENNY + money[1]*DIME + money[2]*NICKEL + money[3]*QUARTER

def generate_random_problem(res : dict) -> bool:
    if randint(0, 100) < 18:
        match randint(0, 1):
            case 0:
                res['water'] = 0
                print("I'm sorry, I don't have enough water. Could you check the floor for water please?")
                print("It seems I have leaked, .... again. Oh no the maintainer won't be happy....")
            case 1:
                res['coffee'] = 0
                print("I'm sorry, I don't have enought coffee to produce your drink.")
                print("Weird, either some rats got into my guts and were so hungry to eat it, or .. there is a coffee thief!!")
                print("Anyway, please tell the maintainer.")
        return True
    else:
        return False

def check_resources(res : dict, brew : str) -> bool:
    enough_resources : bool = res['water'] >= MENU[brew]['ing']['water']
    enough_resources = enough_resources and res['milk'] >= MENU[brew]['ing']['milk']
    enough_resources = enough_resources and res['coffee'] >= MENU[brew]['ing']['coffee']
    return enough_resources

def progress_display() -> None:
    print("I am making your drink")
    for i in track(range(100), description="Preparing.."):
        time.sleep(0.01)
    for i in track(range(100), description="Brewing.."):
        time.sleep(0.02)
    for i in track(range(100), description="Finalizing.."):
        time.sleep(0.005)

def print_coffee(brew : str) -> None:
    print(COFFEE_IMG)
    print(f"Imagine this is your {brew}")

def control_brewing(res : dict, brew : str) -> None:
    print(f"You have chosen - {brew}")
    if check_resources(res, brew):
        print(f"Please insert ${MENU[brew]['cost']}")
        given_money : float = insert_money()
        print(f"Money given ${given_money}")
        if given_money >= MENU[brew]['cost']:
            if not generate_random_problem(res):
                res['money'] += MENU[brew]['cost']
                res['coffee'] -= MENU[brew]['ing']['coffee']
                res['water'] -= MENU[brew]['ing']['water']
                res['milk'] -= MENU[brew]['ing']['milk']
                change : float = given_money - MENU[brew]['cost']
                if change != 0:
                    print(f"Here is your change ${change}")
                progress_display()
                print_coffee(brew)
                print("Have a nice day and come back.")
            else:
                print(f"I am returning you ${given_money}")
        else:
            print("You didn't gimme enough money. Seems like there weren't enough batches, so no penny & dime moment.")
            print(f"I am giving you back {given_money}")       
    else:
        print("It seems I don't have enough resources to produce this brew.\nYou might wanna check the maintainer mode.")
    input("Continue ? [enter]")
    
res : dict = STARTING_RESOURCES
res["money"] = 0
running : bool = True

while running:
    system("clear")
    print(LOGO_IMG)
    match Prompt.ask("What would you like to order?", choices=["espresso", "cappuccino", "latte", "maintain"]):
        case "maintain":
            if authorize("admin"):
                print("hello mister")
                while 1:
                    match Prompt.ask("task -- ", choices=["report", "shutdown", "order", "exit", "take_money", "insert_money"]):
                        case "report":  print_report(res)
                        case "shutdown":
                            running = False
                            break
                        case "exit": break
                        case "take_money":
                            print(f"giving ${res['money']} through the change port")
                        case "insert_money":
                            print("insert money")
                            money : float = insert_money()
                            print(f"inserted ${money}")
                            res['money'] += money
                        case "order":
                            def order_smth(res : dict, what : str, cost : float, amount : int) -> None:
                                if res['money'] >= cost:
                                    res['money'] -= cost
                                    res[what] += amount
                                    print(f"{what} ordered, waiting....")
                                    time.sleep(4)
                                    print(f"{what} is here")
                                else:
                                    print("not enough money")
                            match Prompt.ask("water - 1 l for $0.5\nmilk - 1l for $1\ncoffee - 100 g for $2\nchoose", choices=["water", "milk", "coffee", "none"]):
                                case "none": pass
                                case "water":
                                    order_smth(res, "water", 0.5, 1000)
                                case "milk":
                                    order_smth(res, "milk", 1, 1000)
                                case "coffee":
                                    order_smth(res, "coffee", 2, 100)
            else:
                input("wrong password, good luck partner, press enter")
        case "espresso":
            control_brewing(res, "espresso")
        case "cappuccino":
            control_brewing(res, "cappuccino")
        case "latte":
            control_brewing(res, "latte")