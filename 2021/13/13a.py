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
            m[(x, y)] = "x"
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y
    return m, max_x, max_y

def print_coor():
    # radek
    for y in range(MAX_Y_LENGTH+1):
        # sloupec
        for x in range(MAX_X_LENGTH+1):
            # print(y, x, end=" ")
            print(m[x,y], end=" ")
        print()


data = [line.strip().split(',') for line in fileinput.input()]


m, MAX_X_LENGTH, MAX_Y_LENGTH = create_data_matrix(data)

print(MAX_X_LENGTH, MAX_Y_LENGTH)
pattern = r"fold \w+ ([xy])=(\d+)"

# to_fold = re.findall(pattern, data[-2][0])
matches = []
for d in data:
    to_fold = re.search(pattern, d[0])
    if to_fold:
        matches.append(to_fold)

my_match_ax = matches[0].group(1)
my_match_val = int(matches[0].group(2))
print(my_match_ax, my_match_val)

def fold_y(fold_val, m):

    new_m = defaultdict(lambda: ".")
    revert = {x: y for (x,y) in zip(reversed(range(MAX_Y_LENGTH+1)), range(MAX_Y_LENGTH+1)) }

    for a, b in m:
        if b < fold_val:
            val_old = m[(a, b)]
            val_new = new_m[(a, b)]
            # print(val_new, val_old)
            if "x" in (val_old, val_new):
                val = "x"
            else:
                val = "."
            # print(val)
            new_m[a, b] = val
        elif b == fold_val:
            continue
        else:
            # val = m[(a, b)]
            val_rev = m[(a, revert[b])]
            val_old = m[(a, b)]
            if "x" in (val_old, val_rev):
                val = "x"
            else:
                val = "."
            # print("tu", a, b)
            # print("tu2", a, revert[b])
            new_m[(a, revert[b])] = val
            # print("setting", a, revert[b], new_m[(a, revert[b])])
    return new_m


def fold_x(fold_val, m):

    new_m = defaultdict(lambda: ".")
    revert = {x: y for (x,y) in zip(reversed(range(MAX_X_LENGTH+1)), range(MAX_X_LENGTH+1))}

    for a, b in m:
        # print("checking", a, b)
        if a < fold_val:
            val_old = m[(a, b)]
            val_new = new_m[(a, b)]
            # print(val_new, val_old)
            if "x" in (val_old, val_new):
                val = "x"
            else:
                val = "."
            # print(val)
            new_m[a, b] = val
        elif a == fold_val:
            continue
        else:
            # val = m[(a, b)]
            val_rev = m[(revert[a], b)]
            val_old = m[(a, b)]
            if "x" in (val_old, val_rev):
                val = "x"
            else:
                val = "."
            # print("tu", a, b)
            # print("tu2", revert[a], b)
            new_m[(revert[a], b)] = val
            # print("setting", revert[a], b, new_m[(revert[a], b)])
    return new_m
print_coor()
print("done")
if my_match_ax == "x":
    m = fold_x(my_match_val, m)
elif my_match_ax == "y":
    m = fold_y(my_match_val, m)
# print()
print_coor()

c = 0
for i in m:
    if m[i] == "x":
        c += 1
print(c)