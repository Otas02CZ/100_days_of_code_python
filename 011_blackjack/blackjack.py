# well just a blackjack

from art import logo
from rich.prompt import Prompt
from random import randint
from os import system

cards : list[int] = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

def want_play(first : bool) -> str:
    if first:
        return Prompt.ask("Do you wanna play a game of blackjack?", choices=["yes", "no"])
    else:
        return Prompt.ask("Do you wanna play another game of blackjack?", choices=["yes", "no"])

def want_draw() -> str:
    return Prompt.ask("Do you want another card or do you want to pass?", choices=["yes", "no"])

def draw_card() -> int:
    return cards[randint(0, 11)]

def print_hand(hand : list[int]) -> str:
    hand_text : str = ""
    for card in hand:
        hand_text += str(card) + ", "
    return hand_text[:-2]

def normalize_hand(hand : list[int]) -> tuple:
    hand_sum : int = sum(hand)
    while hand_sum > 21:
        try:
            hand[hand.index(11)] = 1
            hand_sum = sum(hand)
        except:
            hand_sum = 0
            break
    return hand, hand_sum

while want_play(True) == "yes":
    your_hand : list[int] = [draw_card(), draw_card()]
    computer_hand : list[int] = [draw_card(), draw_card()]
    
    system("cls")
    print(logo) 
    print(f"Your cards are: {print_hand(your_hand)}.")
    print(f"Computer's first card is {computer_hand[0]}")
    while want_draw() == "yes":
        your_hand.append(draw_card())
        print(f"Your cards are: {print_hand(your_hand)}.")
        print(f"Computer's first card is {computer_hand[0]}")
    if sum(computer_hand) < 12:
        computer_hand.append(draw_card())
        
    computer_sum : int
    your_sum : int
    computer_hand, computer_sum = normalize_hand(computer_hand)
    your_hand, your_sum = normalize_hand(your_hand)
    
    print(f"Your final hand is: {print_hand(your_hand)}.")
    print(f"Computer's final hand is {print_hand(computer_hand)}")
    if your_sum == 0:
        print("You have a trop.")
        if computer_sum == 0:
            print("Computer has a trop.")
            print("Nobody has won, it is a draw.")
        else:
            print("Computer has not.")
            print("Computer has won.")
    else:
        print(f"Your sum is {your_sum}.")
        if computer_sum == 0:
            print("Computer has a trop.")
            print("You have won.")
        else:
            print(f"Computer has a sum of {computer_sum}.")
            if your_sum > computer_sum:
                print("You have won.")
            elif your_sum == computer_sum:
                print("It is a draw.")
            else:
                print("Computer has won.")
print("Have a nice day.")