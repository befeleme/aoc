import re
from collections import Counter

test = "target area: x=20..30, y=-10..-5"
ostr = "target area: x=236..262, y=-78..-58"
x, y = 0,0

pattern = r"target area: x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)"
x_from, x_to, y_from, y_to = [int(x) for x in re.findall(pattern, ostr)[0]]

def process_probe(x_velocity, y_velocity):
    x, y = 0, 0
    max_y = -50000
    while x <= x_to or y >= y_to:
        if y < y_from:
            break

        x = x + x_velocity
        y = y + y_velocity

        if x_velocity > 0:
            x_velocity = x_velocity -1
        elif x_velocity < 0:
            x_velocity = x_velocity +1
        y_velocity = y_velocity -1
        if y > max_y:
            max_y = y
        if x_from <= x <= x_to and y_from <= y <= y_to:
            return max_y
    return


c = Counter()

for x_velocity in range(x_to+1):
    for y_velocity in range(y_from, 600):
        max_y = process_probe(x_velocity, y_velocity)
        if max_y is not None:
            c[(x_velocity, y_velocity)] = max_y

print(len(c))
