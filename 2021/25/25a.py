import fileinput

data = [line.strip() for line in fileinput.input()]

height = len(data)
width = len(data[0])

cucumber_map = {}
for i in range(height):
    for j in range(width):
        cucumber_map[(j, i)] = data[i][j]

next_step = {
    "v": (0, 1),
    ">": (1, 0),
}

def step():
    # first east facing cucumbers
    to_move = []
    to_empty = []
    for coor in cucumber_map:
        if cucumber_map[coor] == ">":
            off_x, off_y = next_step[cucumber_map[coor]]
            new_x = coor[0] + off_x
            if new_x == width:
                new_x = 0
            neighbor = cucumber_map[new_x, coor[1]+off_y]
            if neighbor == ".":
                # save the coordinates to change the cucumber's pos
                to_empty.append(coor)
                to_move.append((new_x, coor[1]+off_y))


    for coor in to_empty:
        cucumber_map[coor] = "."
    for coor in to_move:
        cucumber_map[coor] = ">"
    
    to_move = []
    to_empty = []
    for coor in cucumber_map:
        if cucumber_map[coor] == "v":
            off_x, off_y = next_step[cucumber_map[coor]]
            new_y = coor[1] + off_y
            if new_y == height:
                new_y = 0
            neighbor = cucumber_map[coor[0]+off_x, new_y]
            if neighbor == ".":
                # save the coordinates to change the cucumber's pos
                to_empty.append(coor)
                to_move.append((coor[0]+off_x, new_y))

    # this is bogus, find the bug (384 in the input data)
    if not to_empty:
        print("not moving anymore")
        return False
    
    for coor in to_empty:
        cucumber_map[coor] = "."
    for coor in to_move:
        cucumber_map[coor] = "v"

    return True


def print_map():
    for x in range(height):
        for y in range(width):
            print(cucumber_map[y, x], end="")
        print()

i = 0
while True:
    i=i+1
    if not step():
        print(i)
        break
