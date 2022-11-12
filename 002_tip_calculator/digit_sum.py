# this code will calculate a digit sum of a number with two digits
print("""Welcome to the digit sum calculator\n
I will calculate the digit sum\nof the inputed (2 digit) number""")
number_str : str = input("Please insert the number: ")
if len(number_str) != 2:
    print("What ???? I said two digits !!\nTry again, .... please")
else:
    print(f"Your digit sum is: {int(number_str[0]) + int(number_str[1])}")
