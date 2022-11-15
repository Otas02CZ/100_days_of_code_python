# this programm will output the highest score from the inserted scores

print("Welcome to the highest score viewer!\n - Please input scores one by one and when you want to finish input -1.")
scores : list[float] = []

while 1:
    try:
        new_score : float = float(input("Please insert a score as a floating point number.\nLarger or equal 0 or -1 to end the input loop: "))
    except:
        print("You have inserted a number in a bad shape :<")
    else:
        if new_score >= 0:
            scores.append(new_score)
        elif new_score == -1:
            break
        else:
            print("You have inserted a number in a bad shape :<")

max_score : float = 0
for score in scores:
    if score > max_score:
        max_score = score
print(f"Highest score from the list of inputed scores is {max_score}")
# optimized code
print(f"Highest score from the list of inputed scores is {max(scores)}")