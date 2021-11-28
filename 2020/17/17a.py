from itertools import product
import fileinput


contents = [x.strip() for x in fileinput.input()]

WIDTH = len(contents[0])
HEIGHT = len(contents)
DEPTH = 1


def create_initial_map():
    """Return a map of (x, y) coordinates and a matching symbol from contents."""
    seat_map = dict()
    for y in range(HEIGHT):
        for x in range(WIDTH):
            for z in range(DEPTH):
                point = x, y, z
                seat_map[point] = contents[y][x]
    return seat_map


def is_active(seat):
    """Return True if seat is empty. If occupied return False. """
    active = seat_map.get(seat, ".")
    return True if active == "#" else False


def count_occupied_neighbours(seat):
    """Return the number of occupied seats according to the new rules.
    This could use some nicer implementation."""
    x, y, z = seat
    offsets = product([-1, 0, 1], repeat=3)
    count_occupied = 0
    new_points = []
    for offset in offsets:
        off_x, off_y, off_z = offset
        new_x, new_y, new_z = x + off_x, y + off_y, z + off_z
        while True:
            new_point = new_x, new_y, new_z
            new_points.append(new_point)
            if new_point == seat:
                break
            if is_active(new_point):
                count_occupied += 1
                break
            else:
                new_x, new_y, new_z = x + off_x, y + off_y, z + off_z
                break
        else:
            break
    return count_occupied, new_points


def check_state(seat, seat_map):
    """Check whether the rules may be applied on given seat.
    If no occupied seat around - add to list of seats to occupy.
    If more than or exactly 5 seats are occupied, add to the list to release."""
    occupied, new_points = count_occupied_neighbours(seat)
    if is_active(seat):
        if occupied in (2, 3):
            to_occupy.append(seat)
        else:
            to_release.append(seat)
    else:
        if occupied == 3:
            to_occupy.append(seat)
        else:
            to_release.append(seat)
    return new_points


def change_state(seat_map):
    """Occupy and release the seats present in respective lists."""
    for seat in to_occupy:
        seat_map[seat] = "#"
    for seat in to_release:
        seat_map[seat] = "."


def traverse_map(seat_map):
    """Go through the map and check state for each seat that isn't floor."""
    points_to_add = set()
    for seat in seat_map:
        new_points = check_state(seat, seat_map)
        points_to_add.update(new_points)
    add_points_to_map(points_to_add)
    for seat in seat_map:
        new_points = check_state(seat, seat_map)
        points_to_add.update(new_points)
    change_state(seat_map)


def count_occupied_seats(seat_map):
    """Count all occupied seats at the end of the round."""
    occupied = 0
    for state in seat_map.values():
        if state == "#":
            occupied += 1
    return occupied


def add_points_to_map(points_to_add):
    for point in points_to_add:
        value = seat_map.get(point, ".")
        seat_map[point] = value


if __name__ == "__main__":
    to_occupy = []
    to_release = []
    occupied_seats = []
    seat_map = create_initial_map()
    for i in range(6):
        print("ROUND", i)
        traverse_map(seat_map)
        print(count_occupied_seats(seat_map))
        to_occupy.clear()
        to_release.clear()
