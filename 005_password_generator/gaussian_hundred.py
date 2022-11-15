# this code will give you a sum of the numbers from 1 to 100

summary : int = 50
for number in range(1, 51):
    summary += number + 100-number
print(summary)