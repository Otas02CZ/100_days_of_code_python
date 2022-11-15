# this is a rock paper scissors game simulator

from rich.prompt import IntPrompt
from random import randint

hand_moves : list[list[str]] = [
    ["rock", """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    """],
    ["paper", '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''],
    ["scissors", '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']]

print("Welcome to rock/paper/scissors game")
your_move : int = IntPrompt.ask("What is your move (rock, paper, scissors)", choices=["0", "1", "2"])
print(f"Your move is {hand_moves[your_move][0]}:\n{hand_moves[your_move][1]}")
computer_move : int = randint(0, 2)
print(f"Computer move is {hand_moves[computer_move][0]}:\n{hand_moves[computer_move][1]}")
if your_move == computer_move:
    print("It is a draw ")
else:
    match your_move:
        case 0: # rock
            if computer_move == 1: # paper
                print("You have lost")
            else: # scissors
                print("You have won")
        case 1: # paper
            if computer_move == 2: # scissors
                print("You have lost")
            else: # rock
                print("You have won")
        case 2: # scissors
            if computer_move == 0: # rock
                print("You have lost")
            else: # paper
                print("You have won")