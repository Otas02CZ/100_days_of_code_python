# this programm simulates blind auction

from rich.prompt import IntPrompt, Prompt
from os import system

auction_bids : list[dict] = []

logo : str = '''
                         ___________
                         \\         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

def add_auction_bidder(auction_bids : list[dict], name : str, bid : int) -> None:
    auction_bids.append({"name" : name, "bid" : bid})

def get_highest_bidder(auction_bids : list[dict]) -> dict:
    highest_bid_dict : dict = {"name" : "", "bid" : 0}
    for bid in auction_bids:
        if highest_bid_dict["bid"] < bid["bid"]:
            highest_bid_dict = bid
    return highest_bid_dict
        

print("Welcome to the blind auction :D")
print(logo)
input("Press Enter to begin ")

while 1:
    name : str = input("Please tell us your name: ")
    bid : int = IntPrompt.ask("Please specify your bid $")
    add_auction_bidder(auction_bids, name, bid)
    if Prompt.ask("Is there somebody else to bid?", choices=["yes", "no"]) == "yes":
        system("cls")
    else:
        break
highest_bid : dict = get_highest_bidder(auction_bids)
print(f"The highest bidder is {highest_bid['name']} with a bid of ${highest_bid['bid']}.")

