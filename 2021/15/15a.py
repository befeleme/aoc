import fileinput


def print_matrix(d):
    for x in range(MAX_LENGTH):
        for y in range(MAX_LENGTH):
            print(d[y,x], end=" ")
        print()

def find_neighbors(coor):
    offsets = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    n = [(coor[0] + o[0], coor[1] + o[1]) for o in offsets]
    return [x for x in n if 0 <= x[0] < MAX_LENGTH and 0 <= x[1] < MAX_LENGTH]

def initialize_distances(d):
    distances = {}
    for coor in d:
        distances[coor] = 1000000000
    distances[(0, 0)] = 0
    return distances

def find_next_with_lowest_distance(d, visited_points):
    min_v = 10000000000000
    for k, v in d.items():
        if v < min_v and k not in visited_points:
            min_v = v
            min_k = k
    else:
        if min_v == 10000000000000:
            return False
    return min_k

d = {}
for i, line in enumerate(fileinput.input()):
    line = line.strip()
    for j, num in enumerate(line):
        d[j, i] = int(num)

MAX_LENGTH = len(line)
distances = initialize_distances(d)
visited_points = set()

while (next_point := find_next_with_lowest_distance(distances, visited_points)):
    length = distances[next_point]
    visited_points.add(next_point)
    neighbors = find_neighbors(next_point)
    for n in neighbors:
        if n not in visited_points:
            risk = d[n] + length
            if risk < distances[n]:
                distances[n] = risk

print(distances[(MAX_LENGTH-1, MAX_LENGTH-1)])
