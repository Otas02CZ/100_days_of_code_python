# this code will calculate digit sum of a number with variable digit length into a number smaller than 10
print("""Welcome to the digit sum calculator\n
I will calculate the absolute digit sum of the inputed number""")
number_str : str = input("Please insert the number: ")

digit_sum : int = int(number_str)

while len(number_str)>1:
    digit_sum = 0
    for digit in range(len(number_str)):
        digit_sum += int(number_str[digit])
    number_str = str(digit_sum)

print(f"Your absolute digit sum is: {digit_sum}")

