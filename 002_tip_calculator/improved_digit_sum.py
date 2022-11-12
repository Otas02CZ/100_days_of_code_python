# This code will calculate digit sum of a number of variable digit length
print("""Welcome to the digit sum calculator\n
I will calculate the digit sum of the inputed number""")
number_str : str = input("Please insert the number: ")

digit_sum : int = 0

for digit in range(len(number_str)):
    digit_sum += int(number_str[digit])

print(f"Your digit sum is: {digit_sum}")

