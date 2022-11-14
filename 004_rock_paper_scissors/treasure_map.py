# this code will allow you to show a map, add a treasure to it and then to show the map with a mark on the spot of the treasure

print("Welcome to treasure map making programm")

size_x : int = 10 # row
size_y : int = 10 # collumn

def print_map(map : list) -> None:
    text_map : str = " "
    for x in range(len(map[1])):
        text_map += "--"
    text_map += " \n"
    for x in range(len(map[0])):
        text_map += "|"
        for y in range(len(map[1])):
            text_map += map[x][y]
        text_map += "|\n"
    text_map += " " 
    for x in range(len(map[1])):
        text_map += "--"
    text_map += " \n"
    print(text_map)

map : list = []
for x in range(size_x):
    map.append([])
    for y in range(size_y):
        map[x].append("  ")

print_map(map)

cross_x : int = int(input("Please insert row coordinate for the treasure spot [0, 10]: "))
cross_y : int = int(input("Please insert collumn coordinate for the treasure spot [0, 10]: "))

map[cross_x][cross_y] = " x"

print_map(map)
 