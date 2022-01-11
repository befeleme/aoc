import fileinput
import re
from collections import defaultdict, Counter
from itertools import product

cubes = defaultdict(lambda: 0)

data = [line.strip() for line in fileinput.input()]
print(data)
seen = set()
actions = {"on": 1, "off": 0}
pattern = r"(\w+) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)"
for line in data:
    action, x_from, x_to, y_from, y_to, z_from, z_to = re.findall(pattern, line)[0]
    # print(matched)
    x_from, x_to, y_from, y_to, z_from, z_to = [int(x) for x in (x_from, x_to, y_from, y_to, z_from, z_to)]
    print(x_to+1 - x_from, y_to+1 - y_from, z_to+1 - z_from)
    print((x_to+1 - x_from) * (y_to+1 - y_from) * (z_to+1 - z_from))

    cuboids_to_act = set(product(range(x_from, x_to+1), range(y_from, y_to+1), range(z_from, z_to+1)))
    # print(len(cuboids_to_act))
    for cuboid in cuboids_to_act:
        cubes[cuboid] = actions[action]
        if cuboid in seen:
            print(cuboid)
        seen.add(cuboid)
# print(cubes)

ons = 0
for cube in cubes:
    ons += cubes[cube]

print(ons)

