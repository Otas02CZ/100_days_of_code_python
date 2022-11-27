# oop version of the coffee machine using the template from udemy.com

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

running : bool = True

while running:
    choice : str = input(f"Please choose {menu.get_items()}:")
    match choice:
        case "report":  
            coffee_maker.report()
            money_machine.report()
        case "exit": break
        case  _:
            order = menu.find_drink(choice)
            if order != None:
                if coffee_maker.is_resource_sufficient(order):
                    if money_machine.make_payment(order.cost):
                        coffee_maker.make_coffee(order)
                        
                        
