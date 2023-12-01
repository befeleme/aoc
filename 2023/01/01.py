import fileinput
import re


def part1(data):
    total = 0
    for line in data:
        digits = re.findall(r"(\d)", line)
        total += int(digits[0] + digits[-1])
    return total


def digitize(inp):
    spelled_digits = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    if inp.isdigit():
        return inp
    return spelled_digits[inp]


def part2(data):
    pattern = r"(\d|one|two|three|four|five|six|seven|eight|nine)"
    total = 0
    for line in data:
        found = []
        while match := re.search(pattern, line):
            found.append(match.group())
            line = line[match.start()+1:]
        total += int(digitize(found[0]) + digitize(found[-1]))
    return total


if __name__ == "__main__":
    data = [line.strip() for line in fileinput.input()]
    print(part1(data))
    print(part2(data))