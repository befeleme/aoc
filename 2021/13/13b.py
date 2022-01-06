import fileinput
from collections import defaultdict
import re


def create_data_matrix(data):
    max_x = 0
    max_y = 0
    m = defaultdict(lambda: ".")
    for coor in data:
        if coor == [""]:
            break
        else:
            x, y = coor
            x, y = int(x), int(y)
            m[(x, y)] = "█"
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y
    return m, max_x, max_y

def print_coor(max_x, max_y):
    # radek
    for y in range(max_y+1):
        # sloupec
        for x in range(max_x+1):
            # print(y, x, end=" ")
            print(m[x,y], end=" ")
        print()


def fold_y(fold_val, m, max_y):

    new_m = defaultdict(lambda: ".")
    # revert = {x: y for (x,y) in zip(reversed(range(max_y+1)), range(max_y+1)) }

    for a, b in m:
        if b < fold_val:
            val_old = m[(a, b)]
            val_new = new_m[(a, b)]
            # print(val_new, val_old)
            if "█" in (val_old, val_new):
                val = "█"
            else:
                val = "."
            # print(val)
            new_m[a, b] = val
        elif b == fold_val:
            continue
        else:
            revert_b = fold_val - (b - fold_val)
            val_rev = m[(a, revert_b)]
            val_old = m[(a, b)]
            if "█" in (val_old, val_rev):
                val = "█"
            else:
                val = "."
            # print("tu", a, b)
            # print("tu2", a, revert[b])
            new_m[(a, revert_b)] = val
            # print("setting", a, revert[b], new_m[(a, revert[b])])
    return new_m


def fold_x(fold_val, m, max_x):

    new_m = defaultdict(lambda: ".")
    revert = {x: y for (x,y) in zip(reversed(range(max_x+1)), range(max_x+1))}

    for a, b in m:
        # print("checking", a, b)
        if a < fold_val:
            val_old = m[(a, b)]
            val_new = new_m[(a, b)]
            # print(val_new, val_old)
            if "█" in (val_old, val_new):
                val = "█"
            else:
                val = "."
            # print(val)
            new_m[a, b] = val
        elif a == fold_val:
            print("toerase x", a, b, m[a, b])
            continue
        else:
            # val = m[(a, b)]
            val_rev = m[(revert[a], b)]
            val_old = m[(a, b)]
            if "█" in (val_old, val_rev):
                val = "█"
            else:
                val = "."
            # print("tu", a, b)
            # print("tu2", revert[a], b)
            new_m[(revert[a], b)] = val
            # print("setting", revert[a], b, new_m[(revert[a], b)])
    return new_m


data = [line.strip().split(',') for line in fileinput.input()]


m, max_x, max_y = create_data_matrix(data)

print(max_x, max_y)
pattern = r"fold \w+ ([xy])=(\d+)"

matches = []
for d in data:
    to_fold = re.search(pattern, d[0])
    if to_fold:
        matches.append(to_fold)
print_coor(max_x, max_y)
print("done")

for match in matches:
    print(max_x, max_y)
    my_match_ax = match.group(1)
    my_match_val = int(match.group(2))
    print(my_match_ax, my_match_val)

    if my_match_ax == "x":
        m = fold_x(my_match_val, m, max_x)
        max_x = my_match_val-1
    elif my_match_ax == "y":
        m = fold_y(my_match_val, m, max_y)
        max_y = my_match_val-1
    print(max_x, max_y)
    print_coor(max_x, max_y)

# print()
# print_coor()
