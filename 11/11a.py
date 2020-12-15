import fileinput
# from collections import Counter

contents = [x.strip() for x in fileinput.input()]

WIDTH = len(contents[0])
HEIGHT = len(contents)


def create_initial_map():
    """Return a map of (x, y) coordinates and a matching symbol from contents."""
    seat_map = dict()
    for y in range(HEIGHT):
        for x in range(WIDTH):
            point = x, y
            seat_map[point] = contents[y][x]
    return seat_map


def is_empty(seat):
    """Return True if seat is empty. Treat floor as an empty seat.
    If occupied return False. """
    return True if seat_map[seat] == "L" or seat_map[seat] == "." else False


def is_valid(value, mode):
    """Return True if value is in range of map size.
    Mode: WIDTH or HEIGHT, depending what value is checked."""
    return False if value < 0 or value > mode-1 else True


def find_neighbours(seat):
    """Return list of all immediate neighbours of given point."""
    scope = (-1, 0, 1)
    x, y = seat
    neighbours = []
    for x_offset in scope:
        new_x = x + x_offset
        for y_offset in scope:
            new_y = y + y_offset
            if is_valid(new_x, WIDTH) and is_valid(new_y, HEIGHT):
                new_point = new_x, new_y
                if new_point != seat:
                    neighbours.append(new_point)
    return neighbours


def check_state(seat):
    """Check whether the rules may be applied on given seat.
    If no occupied seat around - add to list of seats to occupy.
    If more than or exactly 4 seats are occupied, add to the list to release."""
    occupied = 0
    neighbours = find_neighbours(seat)
    for neighbour in neighbours:
        if not is_empty(neighbour):
            occupied += 1
    if occupied >= 4:
        to_release.append(seat)
    elif occupied == 0:
        to_occupy.append(seat)


# First implementation - unnecessarily complicated
# But a nice excercise for map() and all() :)
# def check_state(seat):
#
#     neighbours = find_neighbours(seat)
#     are_empty_neighbours = map(is_empty, neighbours)
#     if is_empty(seat):
#         if all(are_empty_neighbours):
#             to_occupy.append(seat)
#     else:
#         c = Counter(list(are_empty_neighbours))
#         if c[False] >= 4:
#             to_release.append(seat)


def change_state(seat_map):
    """Occupy and release the seats present in respective lists."""
    for seat in to_occupy:
        seat_map[seat] = "#"
    for seat in to_release:
        seat_map[seat] = "L"


def traverse_map(seat_map):
    """Go through the map and check state for each seat that isn't floor."""
    for seat in seat_map:
        if seat_map[seat] != ".":
            check_state(seat)
    change_state(seat_map)


def count_occupied_seats(seat_map):
    """Count all occupied seats at the end of the round."""
    occupied = 0
    for seat, state in seat_map.items():
        if state == "#":
            occupied += 1
    return occupied


if __name__ == "__main__":
    to_occupy = []
    to_release = []
    occupied_seats = []
    seat_map = create_initial_map()
    while True:
        traverse_map(seat_map)
        counter = count_occupied_seats(seat_map)
        # This would mean the numbers have stabilised - end of cycle
        if counter in occupied_seats:
            break
        occupied_seats.append(count_occupied_seats(seat_map))
        to_occupy.clear()
        to_release.clear()
    print(occupied_seats[-1])
