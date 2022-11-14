# this code is a banker roulette game

from random import randint

print("Welcome to the banker roulette. Please input names, and I will tell you who will pay today")
names : list[str] = input("Input names separated by comma and a space Angela, Richard: ").split(", ")
print(f"This time {names[randint(0, len(names)-1)]} will pay")