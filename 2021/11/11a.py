import fileinput
from itertools import product


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
    if coor in n:
        n.remove(coor)
    # filter only those who are within the field
    return [x for x in n if 0 <= x[0] < MAX_LENGTH and 0 <= x[1] < MAX_LENGTH]

def flash(coor, flashed):
    flashed.add(coor)
    neighbors = find_neighbors(coor)
    for neighbor in neighbors:
        if neighbor in flashed:
            continue
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
    # Check for those who flash:
    flashed = set()
    for coor in octopuses:
        if octopuses[coor] > 9:
            flash(coor, flashed)


def print_octos():
    for x in range(MAX_LENGTH):
        for y in range(MAX_LENGTH):
            print(octopuses[y,x], end=" ")
        print()


data = [line.strip() for line in fileinput.input()]
octopuses = create_data_matrix(data)
OFFSETS = list(product(range(-1, 2), repeat=2))
MAX_LENGTH = len(data)

counter = 0
for i in range(100):
    step()
    new_flashed = len(list(filter(lambda x: octopuses[x] == 0, octopuses)))
    counter += new_flashed

print(counter)
