import fileinput
from itertools import cycle


START = "AAA"
END = "ZZZ"


def part1(nodes_dict, instructions):
    steps = 0
    current = START
    for element in instructions:
        current = nodes_dict[current][int(element)]
        steps += 1
        if current == END:
            break
    return steps


if __name__ == "__main__":
    raw_data = [line.strip() for line in fileinput.input()]
    instructions = cycle(raw_data[0].replace("R", "1").replace("L", "0"))
    nodes_dict = {node[:3]: (node[7:10], node[12:15]) for node in raw_data[2:]}
    print(part1(nodes_dict, instructions))
