import fileinput

def find_neighbors(coor, max_len):
    offsets = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    n = [(coor[0] + o[0], coor[1] + o[1]) for o in offsets]
    return [x for x in n if 0 <= x[0] < max_len and 0 <= x[1] < max_len]

def initialize_distances(risk_map):
    distances = {coor: 1000000000 for coor in risk_map}
    distances[(0, 0)] = 0
    return distances

def find_next_with_lowest_distance(unvisited_points, distances):
    min_v = 10000000000000
    for coor in unvisited_points:
        if distances[coor] < min_v:
            min_v = distances[coor]
            min_k = coor
    else:
        if min_v == 10000000000000:
            return False
    return min_k

def dijkstra(distances, d, max_len):
    visited_points = set()
    unvisited_points = {(0,0)}
    while (next_point := find_next_with_lowest_distance(unvisited_points, distances)):
        length = distances[next_point]
        visited_points.add(next_point)
        unvisited_points.remove(next_point)
        neighbors = find_neighbors(next_point, max_len)
        for n in neighbors:
            if n not in visited_points:
                unvisited_points.add(n)
                risk = d[n] + length
                if risk < distances[n]:
                    distances[n] = risk
    return distances[(max_len-1, max_len-1)]

def create_datagrid():
    d = {}
    for i, line in enumerate(fileinput.input()):
        line = line.strip()
        for j, num in enumerate(line):
            d[j, i] = int(num)
    max_len = len(line)
    return d, max_len

# That's the hottest candidate for refactoring,
# but I just want to get it over with :/
def create_whole_map(d, max_len):
    new_d = dict(d)
    # two neighbor fields
    for (x, y), val in d.items():
        new_val = val + 1
        if new_val > 9:
            new_val = new_val % 9
        new_d[x+max_len, y] = new_val
        new_d[x, y+max_len] = new_val

    # three x2
    for (x, y), val in d.items():
        new_val = val + 2
        if new_val > 9:
            new_val = new_val % 9
        new_d[x+max_len*2, y] = new_val
        new_d[x, y+max_len*2] = new_val
        new_d[x+max_len, y+max_len] = new_val

    # four x3
    for (x, y), val in d.items():
        new_val = val + 3
        if new_val > 9:
            new_val = new_val % 9
        new_d[x+max_len*3, y] = new_val
        new_d[x, y+max_len*3] = new_val
        new_d[x+max_len, y+max_len*2] = new_val
        new_d[x+max_len*2, y+max_len] = new_val

    # five x4
    for (x, y), val in d.items():
        new_val = val + 4
        if new_val > 9:
            new_val = new_val % 9
        new_d[x+max_len*4, y] = new_val
        new_d[x, y+max_len*4] = new_val
        new_d[x+max_len, y+max_len*3] = new_val
        new_d[x+max_len*3, y+max_len] = new_val
        new_d[x+max_len*2, y+max_len*2] = new_val

    # four x5
    for (x, y), val in d.items():
        new_val = val + 5
        if new_val > 9:
            new_val = new_val % 9
        new_d[x+max_len, y+max_len*4] = new_val
        new_d[x+max_len*2, y+max_len*3] = new_val
        new_d[x+max_len*3, y+max_len*2] = new_val
        new_d[x+max_len*4, y+max_len] = new_val

    # three x6
    for (x, y), val in d.items():
        new_val = val + 6
        if new_val > 9:
            new_val = new_val % 9
        new_d[x+max_len*2, y+max_len*4] = new_val
        new_d[x+max_len*4, y+max_len*2] = new_val
        new_d[x+max_len*3, y+max_len*3] = new_val

    # two x7
    for (x, y), val in d.items():
        new_val = val + 7
        if new_val > 9:
            new_val = new_val % 9
        new_d[x+max_len*3, y+max_len*4] = new_val
        new_d[x+max_len*4, y+max_len*3] = new_val

    # one x8
    for (x, y), val in d.items():
        new_val = val + 8
        if new_val > 9:
            new_val = new_val % 9
        new_d[x+max_len*4, y+max_len*4] = new_val

    return new_d

def main():
    risk_map, max_len = create_datagrid()
    risk_map = create_whole_map(risk_map, max_len)
    max_len = max_len*5
    distances = initialize_distances(risk_map)
    print(dijkstra(distances, risk_map, max_len))

if __name__ == "__main__":
    main()