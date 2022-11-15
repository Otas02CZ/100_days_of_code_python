# this programm will give you the sum of even numbers from the given range

print("Welcome to the even numbers in range calculator!")
range_a : int = int(input("Insert starting point of the range (whole number): "))
range_b : int = int(input("Insert ending point of the range(Whole number): "))
if range_a > range_b:
    helper : int = range_a
    range_a = range_b
    range_b = helper
    print("The points had to be switched")
print(f"The range is ({range_a}, {range_b})")

evens : list[int] = []
evens_text_form : str = ""
for even in range(range_a, range_b, 2):
    evens.append(even)
    evens_text_form += str(even) + ", "

if len(evens) == 0:
    print("There are no even numbers in the given range")
else:
    evens_text_form = evens_text_form[:-2]
    print(f"The evens in the given range are:\n{evens_text_form}\nThere are {len(evens)} even numbers.")