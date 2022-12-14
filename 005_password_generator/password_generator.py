# this is a PyPassword Generator

from rich.prompt import IntPrompt
from random import randint, sample

lc_letters : str = "abcdefghijklmnopqrstuvwxyz"
uc_letters : str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers : str = "0123456789"
symbols : str = "!#$%&()*+"

print("Welcome to the PyPassword Generator")
length : int = randint(8, 64)
config = {
    "length" : length,
    "uc_letters" : randint(1, int(length/4)),
    "numbers" : randint(1, int(length/4)),
    "symbols" : randint(1, int(length/4)),
    "lc_letters" : 0
}

configure : int = IntPrompt.ask("Would you like to configure the generator? (False, True)", choices=["0", "1"])
if configure:
    length : int = IntPrompt.ask("Please specify the password length <8, 64>")
    if length < 8 or length > 64:
        print(f"You have inserted incorrect number ({length}) we will revert to autogenerated value {config['length']}")
    else:
        config["length"] = length
    n_uc_letters : int = IntPrompt.ask(f"Please specify the number of upper case letters <1, {config['length']-1}>")
    if n_uc_letters < 1 or n_uc_letters > length - 1:
        print(f"You have inserted incorrect number ({n_uc_letters}) we will revert to autogenerated value {config['uc_letters']}")
    else:
        config["uc_letters"] = n_uc_letters
    possible_counts : list = [str(number) for number in range(1, config['length']-config['uc_letters'])]
    if len(possible_counts) == 0:
        print("Not enough space numbers, symbols and lower_case characters")
        config["symbols"] = config["numbers"] = 0
    else:
        config["numbers"] = IntPrompt.ask("Please specify the count of numbers", choices=possible_counts)
        possible_counts : list = [str(number) for number in range(1, config['length']-config['uc_letters']-config["numbers"])]
        if len(possible_counts) == 0:
            print("Not enough space symbols and lower_case characters")
            config["symbols"] = 0
        else:
            config["symbols"] = IntPrompt.ask("Please specify the count of symbols", choices=possible_counts)
            n_lc_letters : int = config["length"] - config["numbers"] - config["symbols"] - config["uc_letters"]
            if n_lc_letters > 0:
                print(f"There will also be {n_lc_letters} lower case letters")
                config["lc_letters"] = n_lc_letters
            else:
                print("There is no space for lower case letters left")
else:
    config.update({"lc_letters" : config["length"] - config["numbers"] - config["symbols"] - config["uc_letters"]})
print(f"The configuration is as follows:\n - lenght - {config['length']}\n - uc_letters - {config['uc_letters']}")
print(f" - lc_letters - {config['lc_letters']}\n - symbols - {config['symbols']}\n - numbers - {config['numbers']}")

def pswd_chunk(length : int, symbols : str) -> str:
    pswd_chunk : str = ""
    for symbol in range(length):
        pswd_chunk += symbols[randint(0, len(symbols)-1)]
    return pswd_chunk

password : str = pswd_chunk(config["lc_letters"], lc_letters) + pswd_chunk(config["numbers"], numbers) +  pswd_chunk(config["uc_letters"], uc_letters) + pswd_chunk(config["symbols"], symbols)

password = "".join(sample(password, len(password)))
print(f"Your generated password is here:\n{password}")