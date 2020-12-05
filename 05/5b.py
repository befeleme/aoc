"""
It's a completely full flight, so your seat should be the only missing
boarding pass in your list. However, there's a catch:
some of the seats at the very front and back of the plane don't exist on this aircraft,
so they'll be missing from your list as well.

Your seat wasn't at the very front or back, though;
the seats with IDs +1 and -1 from yours will be in your list.
"""

ROWS = list(range(128))
COLUMNS = list(range(8))


def get_input():
    with open("input_5", "r", encoding="utf-8") as f:
        return [x.strip() for x in f.readlines()]


def narrow_choice(my_list, direction):
    """
    Find the middle list index and return either the first or the second half of the list.
    Middle index is respectively start or end point of the new list.
    """
    index = len(my_list) // 2
    if direction == "F" or direction == "L":
        new_list = my_list[:index]
    elif direction == "B" or direction == "R":
        new_list = my_list[index:]
    return new_list


def find_seat_id(seat):
    """Given the encrypted seat number, find its ID."""
    rows = ROWS
    cols = COLUMNS
    for dir in seat[:7]:
        rows = narrow_choice(rows, dir)
    for dir in seat[7:]:
        cols = narrow_choice(cols, dir)
    seat_id = rows[0] * 8 + cols[0]
    return seat_id


def find_missing_id(seats):
    """Sort the list and print the two IDs which don't have -1 and +2 item."""
    seats.sort()
    for i in range(len(seats)):
        # ignore first and last indexes
        if i == 0 or i == len(seats) - 1:
            continue
        if not (seats[i] - 1 == seats[i-1] and seats[i] + 1 == seats[i+1]):
            print(f"Not matching ID: {seats[i]}")


def main():
    contents = get_input()
    seat_ids = []
    for seat in contents:
        seat_ids.append(find_seat_id(seat))
    find_missing_id(seat_ids)


if __name__ == "__main__":
    main()
