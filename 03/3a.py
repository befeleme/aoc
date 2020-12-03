"""
The toboggan can only follow a few specific slopes
(you opted for a cheaper model that prefers rational numbers);
start by counting all the trees you would encounter for the slope right 3, down 1:

From your starting position at the top-left,
check the position that is right 3 and down 1.
Then, check the position that is right 3 and down 1 from there,
and so on until you go past the bottom of the map.
Count the trees on the way.
"""

with open("input_3", "r", encoding="utf-8") as f:
    contents = [x.strip() for x in f.readlines()]

line_len = len(contents[0])  # 31

tree_count = 0
pos = 0

for line in contents:
    if line[pos] == "#":
        tree_count += 1
    pos = (pos + 3) % line_len

print(f"Total tree count of your way down is {tree_count}")
