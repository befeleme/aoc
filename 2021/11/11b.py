import fileinput
from itertools import product
from collections import Counter


def create_data_matrix(data):
    m = {}
    for i, row in enumerate(data):
        for j, pos in enumerate(data[i]):
            m[(j, i)] = int(pos)
    return m

def find_neighbors(coor):
    # calculate all neighbors from offsets
    n = [(coor[0] + x[0], coor[1] + x[1]) for x in OFFSETS]
    # don't process the actually checked coordinates
    n.remove(coor)
    # filter only those who are within the field
    return [x for x in n if 0 <= x[0] < MAX_LENGTH and 0 <= x[1] < MAX_LENGTH]


def flash(coor, flashed):
    flashed.add(coor)
    neighbors = find_neighbors(coor)
    for neighbor in neighbors:
        if neighbor not in flashed:
            octopuses[neighbor] += 1
            if octopuses[neighbor] > 9:
                flash(neighbor, flashed)
    else:
        for coor in flashed:
            octopuses[coor] = 0
        return

def step():
    # Energy level of each octopus rises
    for coor in octopuses:
        octopuses[coor] += 1
    # Check for those who flash
    flashed = set()
    for coor in octopuses:
        if octopuses[coor] > 9:
            flash(coor, flashed)

def print_octos():
    for x in range(MAX_LENGTH):
        for y in range(MAX_LENGTH):
            print(octopuses[y,x], end=" ")
        print()


OFFSETS = list(product(range(-1, 2), repeat=2))
data = [line.strip() for line in fileinput.input()]
octopuses = create_data_matrix(data)
MAX_LENGTH = len(data)

i = 0
while True:
    i += 1
    step()

    counter = list(filter(lambda x: octopuses[x] == 0, octopuses))
    if len(counter) == 100:
        print(i)
        break

# print_octos()
