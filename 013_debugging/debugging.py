############DEBUGGING#####################

# Describe Problem
def my_function():
  for i in range(1, 21):
    if i == 20:
      print("You got it")
my_function()

# Reproduce the Bug
from random import randint
dice_imgs : list = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num : int= randint(0, 5)
print(dice_imgs[dice_num])

# Play Computer
year : int = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year >= 1994:
  print("You are a Gen Z.")

# Fix the Errors
age : int = int(input("How old are you?"))
if age >= 18:
    print(f"You can drive at age {age}.")

#Print is Your Friend
pages : int = 0
word_per_page : int = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words : int = pages * word_per_page
print(total_words)

#Use a Debugger
def mutate(a_list):
  b_list : list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])

number : int = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

from rich.prompt import IntPrompt

year : int = IntPrompt.ask("Enter a year please")

if year <0:
    print("You inputed a very interesting year :D")

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"Year {year} is a leap year")
else:
    print(f"Year {year} is not a leap year")

for number in range(1, 101):
    
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number %3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print([number])























