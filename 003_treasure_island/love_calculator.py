# this programm will calculate a true love between to objects

print("Welcome to the true love calculator :D")
name_a : str = input("Insert the name of the first object: ").lower()
name_b : str = input("Insert the name of the second object: ").lower()


first_digit = 0 + name_a.count("t") + name_a.count("r") + name_a.count("u") + name_a.count("e")
first_digit += name_b.count("t") + name_b.count("r") + name_b.count("u") + name_b.count("e")
second_digit = 0 + name_a.count("l") + name_a.count("o") + name_a.count("v") + name_a.count("e")
second_digit += name_b.count("l") + name_b.count("o") + name_b.count("v") + name_b.count("e")
love_index = 10*first_digit + second_digit

if love_index < 10 or love_index > 90:
    print(f"Dear {name_a} and {name_b}, your score is {love_index}, you go together like coke and mentos.")
elif love_index > 40 and love_index < 50:
    print(f"Dear {name_a} and {name_b}, your score is {love_index}, you will shine together.")
else:
    print(f"Dear {name_a} and {name_b}, your score is {love_index}, better not talk about it......")