import fileinput

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
    """Return True if seat is empty. If occupied return False. """
    return True if seat_map[seat] == "L" else False


def is_floor(seat):
    """Return True if seat is floor. Else: False. """
    return True if seat_map[seat] == "." else False


def is_valid(value, mode):
    """Return True if value is in range of map size.
    Mode: WIDTH or HEIGHT, depending what value is checked."""
    return False if value < 0 or value > mode-1 else True


def count_occupied_neighbours(seat):
    """Return the number of occupied seats according to the new rules.
    This could use some nicer implementation."""
    x, y = seat
    offsets = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
    count_occupied = 0
    for offset in offsets:
        off_x, off_y = offset
        new_x, new_y = x + off_x, y + off_y
        while True:
            if is_valid(new_x, WIDTH) and is_valid(new_y, HEIGHT):
                new_point = new_x, new_y
                if not is_floor(new_point):
                    if not is_empty(new_point):
                        count_occupied += 1
                        break
                    else:
                        break
                else:
                    new_x, new_y = new_x + off_x, new_y + off_y
            else:
                break
    return count_occupied


def check_state(seat, seat_map):
    """Check whether the rules may be applied on given seat.
    If no occupied seat around - add to list of seats to occupy.
    If more than or exactly 5 seats are occupied, add to the list to release."""
    occupied = count_occupied_neighbours(seat)
    if occupied >= 5:
        to_release.append(seat)
    elif occupied == 0:
        to_occupy.append(seat)


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
            check_state(seat, seat_map)
    change_state(seat_map)


def count_occupied_seats(seat_map):
    """Count all occupied seats at the end of the round."""
    occupied = 0
    for state in seat_map.values():
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
        if counter in occupied_seats:
            break
        occupied_seats.append(count_occupied_seats(seat_map))
        to_occupy.clear()
        to_release.clear()
    print(occupied_seats[-1])
