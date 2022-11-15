# this programm will calculate average height from inputed heights

print("Welcome to the average height calculator!\n - Please input heights one by one and when you want to finish input 0.")
heights : list[float] = []

while 1:
    try:
        new_height : float = float(input("Please insert a height as a floating point number.\nLarger than 0 or zero to end the input loop: "))
    except:
        print("You have inserted a number in a bad shape :<")
    else:
        if new_height > 0:
            heights.append(new_height)
        elif new_height == 0:
            break
        else:
            print("You have inserted a number in a bad shape :<")

if len(heights) > 0:
    print(f"The average height is {round(sum(heights)/len(heights))} cm.")
else:
    print("It seems you haven't inserted any numbers.")

# the unoptimized way of doing it
heights_sum : float = 0
heights_len : int = 0
for height in heights:
    heights_len += 1
    heights_sum += height

if len(heights) > 0:
    print(f"The average height is {round(heights_sum/heights_len)} cm.")
else:
    print("It seems you haven't inserted any numbers.")