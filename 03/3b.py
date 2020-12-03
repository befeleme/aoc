"""
Determine the number of trees you would encounter if,
for each of the following slopes,
you start at the top-left corner and traverse the map all the way to the bottom:

    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.

What do you get if you multiply together the number of trees encountered on each of the listed slopes?
"""
with open("input_3", "r", encoding="utf-8") as f:
    contents = [x.strip() for x in f.readlines()]


def traverse(rule):
    to_right, to_down = rule
    tree_count = 0
    pos = 0
    for line in contents:
        if contents.index(line) % to_down == 0:
            if line[pos] == "#":
                tree_count += 1
            pos = (pos + to_right) % line_len
    return tree_count


line_len = len(contents[0])

rules = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

all_counts = 1
for rule in rules:
    all_counts *= traverse(rule)

print(f"Total tree count of your way down is {all_counts}")
