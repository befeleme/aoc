import hashlib


def find_number(puzzle_input, expected_start):
    n = 1
    while True:
        m = hashlib.md5()
        m.update(puzzle_input)
        m.update(str(n).encode())
        if m.hexdigest().startswith(expected_start):
            return n
        n += 1


puzzle_input = "ckczppom".encode()
print(find_number(puzzle_input, "00000"))
print(find_number(puzzle_input, "000000"))