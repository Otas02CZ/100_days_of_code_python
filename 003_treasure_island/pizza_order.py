# this code is a pizza order application

from tqdm import tqdm
from time import sleep
from random import randint
from os import system
from rich.prompt import Prompt

system("cls")
print("PIZZA_ORDER_AUTOMATOR - 2022 - v1.1beta2 - @PythonForPizza")
print("Loading ....")
for wait in tqdm(range(20)):
    sleep(randint(2, 10)/10)
system("cls")
print("Welcome to our pizza order Information System :D")
show_pricing : str = Prompt.ask("Do you wanna see the price chart?", choices=["y", "n"])
if show_pricing == "y":
    price_chart = """
------------
Price chart:
------------
Sizes:
 - S  - small    - $5
 - M  - medium   - $7
 - L  - large    - $9
 - XL - x-large  - $12
--------------
Toppings [Pizza Size - S, M, L, XL]:
 - Pepperoni     - $1, $1, $2, $2
 - Salami        - $1, $2, $2, $3
 - Schrooms      - $0.5, $0.5, $1, $1
 - Tuna          - $2, $3, $3, $4
 - Ham           - $1, $2, $2, $3
 - Extra Cheesse - $1, $2, $3, $4
--------------
Take-away:
 - packaging     - $1
"""
    print(price_chart)
print("Now please select your pizza")
size : str = Prompt.ask("Pizza size", choices=["S", "M", "L", "XL"])
pepperoni : str = Prompt.ask("Do you want pepperoni?", choices=["y", "n"])
salami : str = Prompt.ask("Do you want salami?", choices=["y", "n"])
schrooms : str = Prompt.ask("Do you want schrooms?", choices=["y", "n"])
tuna : str = Prompt.ask("Do you want tuna?", choices=["y", "n"])
ham : str = Prompt.ask("Do you want ham?", choices=["y", "n"])
extra_cheesse : str = Prompt.ask("Do you want extra cheesse?", choices=["y", "n"])
take_away : str = Prompt.ask("Take away (packaging cost)?", choices=["y", "n"])

total_price : float = 0.0

pricing : list = [
    [5, 7, 9, 12],
    [1, 1, 2, 2],
    [1, 2, 2, 3],
    [0.5, 0.5, 1, 1],
    [2, 3, 3, 4],
    [1, 2, 2, 3],
    [1, 2, 3, 4],
    [1]]

size_index : int = 0
summary_msg : str = "You have ordered "

match size:
    case "S":
        summary_msg += " a small pizza"
        total_price += pricing[0][0]
    case "M":
        summary_msg += " a medium sized pizza"
        size_index = 1
        total_price += pricing[0][1]
    case "L":
        summary_msg += " a large pizza"
        size_index = 2
        total_price += pricing[0][2]
    case "XL":
        summary_msg += " an extra large pizza"
        size_index = 3
        total_price += pricing[0][3]

if pepperoni=="y" or salami=="y" or schrooms=="y" or tuna=="y" or ham=="y" or extra_cheesse=="y":
    summary_msg += " with these toppings:"
    if pepperoni == "y":
        summary_msg += " pepperoni "
        total_price += pricing[1][size_index]
    if salami == "y":
        summary_msg += " salami "
        total_price += pricing[2][size_index]
    if schrooms == "y":
        summary_msg += " schrooms "
        total_price += pricing[3][size_index]
    if tuna == "y":
        summary_msg += " tuna "
        total_price += pricing[4][size_index]
    if ham == "y":
        summary_msg += " ham "
        total_price += pricing[5][size_index]
    if extra_cheesse == "y":
        summary_msg += " extra_cheesse "
        total_price += pricing[6][size_index]
else:
    summary_msg += " without any toppings"
if take_away == "y":
    summary_msg += " and you have chosen to take it with you."
    total_price += pricing[7][0]
else:
    summary_msg += " and you have chosen to eat it here."

print(f"---------------------\n{summary_msg}\nTotal cost : ${total_price}")
money_given : str = Prompt.ask("Do you agree and wanna pay?", choices=["y", "n"])
if money_given == "n":
    print("OK, then go you know where :<")
else:
    print("Thank you for your purchase, we are now baking your pizza")
    for wait in tqdm(range(20)):
        sleep(randint(2, 20)/10)
    print("Your pizza is done")
    if take_away == "y":
        print("Here is your pizza, bye")
        print("Error 404 - No pizza ascii art available, unable to open pizza_box_ascii.txt")
    elif randint(0, 1):
        print("But the chef ate it before I managed to take it, so here you have at least a slice")
        # credit https://github.com/ron-png/PizzaTime
        pizza_img : str = """
                                        ._
                                    ,(  `-.
                                    ,': `.   `.
                                ,` *   `-.   \\
                                ,'  ` :+  = `.  `.
                            ,~  (o):  .,   `.  `.
                            ,'  ; :   ,(__) x;`.  ;
                        ,'  :'  itz  ;  ; ; _,-'
                        .'O ; = _' C ; ;'_,_ ;
                    ,;  _;   ` : ;'_,-'   i'
                    ,` `;(_)  0 ; ','       :
                .';6     ; ' ,-'~
                ,' Q  ,& ;',-.'
            ,( :` ; _,-'~  ;
            ,~.`c _','
        .';^_,-' ~
        ,'_;-''
        ,,~
        i'
        :"""
        print(pizza_img)
    else:
        print("Here is your pizza, have a good taste")
        print("Error 404 - No pizza ascii art available, unable to open pizza_ascii.txt")