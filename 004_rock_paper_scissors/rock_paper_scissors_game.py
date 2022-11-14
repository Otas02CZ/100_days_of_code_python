# this is a rock paper scissors game simulator

from rich.prompt import Prompt
from random import randint

hand_moves : dict = {
    "rock" : """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    """,

    "paper" : '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',

    "scissors" : '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
}

your_move : str = Prompt.ask("What is your move", choices=["rock", "paper", "scissors"])
print(f"Your move is {your_move}:\n{hand_moves[your_move]}")
computer_move : str = ""
match randint(0, 2):
    case 0:
        print(f"Computer move is rock:\n{hand_moves['rock']}")
        computer_move = "rock"
    case 1:
        print(f"Computer move is paper:\n{hand_moves['paper']}")
        computer_move = "paper"
    case 2:
        print(f"Computer move is scissors:\n{hand_moves['scissors']}")
        computer_move = "scissors"
        
if your_move == computer_move:
    print("It is a draw ")
elif your_move == "rock" and computer_move == "scissors":
    print("You have won")
elif your_move == "rock" and computer_move == "paper":
    print("You have lost")
elif your_move == "paper" and computer_move == "scissors":
    print("You have lost")
elif your_move == "paper" and computer_move == "rock":
    print("You have won")
elif your_move == "scissors" and computer_move == "paper":
    print("You have won")
else:
    print("You have lost")

# might optimize the elif statement hell