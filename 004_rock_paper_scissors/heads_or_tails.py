# this programm will simulate the heads and tails (coin randomization)
from random import randint

input("Welcome to rock paper scissors!\nContinue - Enter")
if randint(0, 1):
    print("Its a head")
else:
    print("Its a tail")