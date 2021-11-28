import fileinput

tiles_dir = [dir.strip() for dir in fileinput.input()]

STARTING_TILE = 0, 0
OFFSETS = {
    "nw": lambda x, y: (x-1, y-1),
    "ne": lambda x, y: (x+1, y-1),
    "e": lambda x, y: (x+2, y),
    "se": lambda x, y: (x+1, y+1),
    "sw": lambda x, y: (x-1, y+1),
    "w": lambda x, y: (x-2, y),
}


def parse_dir(tile):
    coordinates = STARTING_TILE
    while tile:
        start_char = tile[0]
        if start_char == "e" or start_char == "w":
            dir = start_char
            tile = tile[1:]
        else:
            # direction has got 2 characters, adjust tile accordingly
            dir = start_char + tile[1]
            tile = tile[2:]
        coordinates = OFFSETS[dir](*coordinates)
    return coordinates


def count_blacks(tiles):
    counter = 0
    for color in tiles.values():
        counter += 1 if color else 0
    return counter


def flip(tile):
    # Get flipped value, if not present, start with white and add to tiles
    is_black = tiles.get(tile, False)
    flipped = False if is_black else True
    tiles[tile] = flipped


def count_black_neighbours(tile):
    counter = 0
    for dir in OFFSETS:
        neighbour = OFFSETS[dir](*tile)
        is_black = tiles.get(neighbour, False)
        if is_black:
            counter += 1
    return counter


def find_new_neighbours():
    to_add = []
    for tile in tiles:
        for dir in OFFSETS:
            neighbour = OFFSETS[dir](*tile)
            try:
                tiles[neighbour]
            except KeyError:
                to_add.append(neighbour)
    return to_add


# 1st round
tiles = {}
for tile_dir in tiles_dir:
    tile_coordinates = parse_dir(tile_dir)
    flip(tile_coordinates)

# next rounds
for i in range(100):
    # expand the grid with neighbours
    to_add = find_new_neighbours()
    for tile in to_add:
        tiles[tile] = False

    to_add = []
    to_flip = []
    for tile, is_black in tiles.items():
        blacks = count_black_neighbours(tile)
        if is_black:
            if blacks == 0 or blacks > 2:
                to_flip.append(tile)
        else:
            if blacks == 2:
                to_flip.append(tile)

    for tile in to_flip:
        flip(tile)


print(count_blacks(tiles))
