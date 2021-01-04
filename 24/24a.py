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


tiles = {}
for tile_dir in tiles_dir:
    tile_coordinates = parse_dir(tile_dir)
    # Get flipped value, if not present, start with white
    is_black = tiles.get(tile_coordinates, False)
    flipped = False if is_black else True
    tiles[tile_coordinates] = flipped

counter = 0
for color in tiles.values():
    counter += 1 if color else 0

print(counter)
