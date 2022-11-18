# this code is a simple hangman application

from random_word import RandomWords
from art import stages, logo
from os import system

def print_status(blank : list[str], lives : int, last_guess : int, last_char : str) -> None:
    print("".join([char + " " for char in blank]))
    if lives < 7:
        print(stages[lives])
    match last_guess:
        case 1: print(f"{last_char} is not in the word, might i tighten the knot?")
        case 2: print(f"Yes {last_char} is in the word, well you might even escape the gallows.")
        case 3: print("Ooopsie, you have already tried this one, I'm afraid you will be soon hanging in the wind my friend.")
    if lives == 0:
        print("Well, sorry, we have just hanged you :<")
        
def insert_char() -> str:
    while 1:
        char : str = input("Guess a character (insert only one): ")
        if len(char) == 1:
            return char.lower()
        
def check_occurence(char : str, word : list[str], blank : list[str]) -> int:
    if char in word:
        for index in [i for i, value in enumerate(word) if value == char]:
            blank[index] = char
        return 2
    else:
        return 1

word_randomizer : RandomWords = RandomWords()

word : list[str] = [char for char in word_randomizer.get_random_word()]
blank : list[str] = ["_" for i in range(len(word))]
lives : int = 7
guessed : list[str] = []
last_guess : int = 0
char : str = ""
print(logo)
print("Welcome to hangman game :D, hope you won't be hanged!!")
input("Press Enter to start the game: ")
while lives != 0:
    system("cls")
    print_status(blank, lives, last_guess, char)
    char : str = insert_char()
    if char in guessed:
        lives -= 1
        last_guess = 3
    else:
        last_guess = check_occurence(char, word, blank)
        if last_guess == 1:
            lives -= 1
    guessed.append(char)
print_status(blank, lives, last_guess, char)
if lives == 0:
    print(f"The guessed word was {''.join(word)}")
else:
    print("Congratulations, you have WON")
