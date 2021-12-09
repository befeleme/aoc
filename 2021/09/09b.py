import fileinput


def create_data_matrix(data):
    m = {}
    for i, row in enumerate(data):
        for j, pos in enumerate(data[i]):
            m[(j, i)] = int(pos)
    return m


def traverse_neighbors(k, heights, basin):
    offsets = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    # Finish processing if encountered 9
    if heights[k] == 9:
        return False

    basin.append(k)
    # Get all neighbors
    neighbors = [(k[0] + o[0], k[1] + o[1]) for o in offsets]
    for x, y in neighbors:
        # Invalid coordinates, ignore
        if x < 0 or y < 0 or x >= maxim or y >= maxim:
            continue
        # Already processed, ignore
        if (x, y) in basin:
            continue
        # 9 was encountered, but don't return until all fields are went through
        if not traverse_neighbors((x, y), heights, basin):
            continue
    else:
        return basin


def check_cave(heights):
    for k, v in heights.items():
        if v == 9:
            continue
        return traverse_neighbors(k, heights, basin=[])


data = [line.strip() for line in fileinput.input()]

# Real input is 100x100
maxim = len(data)
heights = create_data_matrix(data)

basins_size = []
while heights:
    basin_elements = check_cave(heights)
    if basin_elements is None:
        break
    basins_size.append(len(basin_elements))
    # Create a new map without already processed fields and replace the old one with it
    new_heights = {}
    for k, v in heights.items():
        if k not in basin_elements:
            new_heights[k] = v
    heights = new_heights


basins_size.sort()
print(basins_size[-1] * basins_size[-2] * basins_size[-3])