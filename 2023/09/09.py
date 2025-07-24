import fileinput


def give_differences(single_row, cnt):
    if not any(single_row):
        return cnt

    diffs = compute_differences(single_row)

    cnt += diffs[-1]
    return give_differences(diffs, cnt)


def compute_differences(single_row):
    diffs = []
    for i, val in enumerate(single_row):
        try:
            next_val = single_row[i+1]
        except IndexError:
            break
        else:
            diffs.append(int(next_val) - int(val))
    return diffs


def part1(raw_data):
    cnt = 0
    for row in raw_data:
        row = list(map(int, row))
        cnt += give_differences(row, row[-1])
    return cnt


def compute(all_rows):
    start = 0
    while all_rows:
        first_last = all_rows.pop()[0]
        start = first_last - start
    return start


def part2(raw_data):
    cnt = 0
    for row in raw_data:
        row = list(map(int, row))
        computed_rows = []
        computed_rows.append(row)
        new_row = compute_differences(row)
        while any(new_row):
            computed_rows.append(new_row)
            new_row = compute_differences(new_row)
        cnt += compute(computed_rows)
    return cnt


if __name__ == "__main__":
    raw_data = [line.strip().split(" ") for line in fileinput.input()]
    print(part1(raw_data))
    print(part2(raw_data))