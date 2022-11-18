# this code is a simple hangman application

from random_word import RandomWords

word_randomizer : RandomWords = RandomWords()
hangman_imgs : list[str] = []

word = word_randomizer.get_random_word()
print(word)

print("Welcome to hnagman game :D, hope you won't be hanged!!")

