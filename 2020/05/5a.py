"""
For example, consider just the first seven characters of FBFBBFFRLR:
Start by considering the whole range, rows 0 through 127.
F means to take the lower half, keeping rows 0 through 63.
B means to take the upper half, keeping rows 32 through 63.
F means to take the lower half, keeping rows 32 through 47.
B means to take the upper half, keeping rows 40 through 47.
B keeps rows 44 through 47.
F keeps rows 44 through 45.
The final F keeps the lower of the two, row 44.
The last three characters will be either L or R; these specify exactly
one of the 8 columns of seats on the plane (numbered 0 through 7).
The same process as above proceeds again, this time with only three steps.
L means to keep the lower half, while R means to keep the upper half.
"""

ROWS = list(range(128))
COLUMNS = list(range(8))

test_inp = [
    'BFFFBBFRRR',  # row 70, column 7, seat ID 567
    'FFFBBBFRRR',  # row 14, column 7, seat ID 119
    'BBFFBBFRLL',  # row 102, column 4, seat ID 820
]


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


def main():
    contents = get_input()
    max_seat_id = 0
    for seat in contents:
        rows = ROWS
        cols = COLUMNS
        for dir in seat[:7]:
            rows = narrow_choice(rows, dir)
        for dir in seat[7:]:
            cols = narrow_choice(cols, dir)
        seat_id = rows[0] * 8 + cols[0]
        if seat_id > max_seat_id:
            max_seat_id = seat_id
    print(f"The maximal seat ID value is {max_seat_id}")


if __name__ == "__main__":
    main()
