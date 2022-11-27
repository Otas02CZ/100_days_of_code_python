# contains the recipes for all the coffees which can be brewed by the machine
MENU : dict = {
    "espresso": {
        "ing": {
            "water": 50,
            "milk" : 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ing": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ing": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

STARTING_RESOURCES : dict = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

PENNY : float = 0.01
DIME : float = 0.1
NICKEL : float = 0.05
QUARTER : float = 0.25

import hashlib

hs = hashlib.sha256("admin".encode('utf-8')).hexdigest()
print(hs)

LOGO_IMG : str = """
 .d8888b.            .d888  .d888                       888b     d888                   888      d8b                   
d88P  Y88b          d88P"  d88P"                        8888b   d8888                   888      Y8P                   
888    888          888    888                          88888b.d88888                   888                            
888         .d88b.  888888 888888 .d88b.   .d88b.       888Y88888P888  8888b.   .d8888b 88888b.  888 88888b.   .d88b.  
888        d88""88b 888    888   d8P  Y8b d8P  Y8b      888 Y888P 888     "88b d88P"    888 "88b 888 888 "88b d8P  Y8b 
888    888 888  888 888    888   88888888 88888888      888  Y8P  888 .d888888 888      888  888 888 888  888 88888888 
Y88b  d88P Y88..88P 888    888   Y8b.     Y8b.          888   "   888 888  888 Y88b.    888  888 888 888  888 Y8b.     
 "Y8888P"   "Y88P"  888    888    "Y8888   "Y8888       888       888 "Y888888  "Y8888P 888  888 888 888  888  "Y8888 
"""

COFFEE_IMG : str = """

               _..,----,.._
            .-;'-.,____,.-';
           (( |            |
            `))            ;
             ` \\          /
        jgs .-' `,.____.,' '-.
           (     '------'     )
            `-=..________..--'
"""