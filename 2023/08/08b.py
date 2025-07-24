import fileinput
from itertools import cycle
import math


def part2_bad(nodes_dict, instructions):
    starting = [node for node in nodes_dict if node.endswith("A")]
    print(starting)
    steps = 0
    current = starting
    for element in instructions:
        new = []
        for node in current:
            new_node = nodes_dict[node][int(element)]
            new.append(new_node)
        steps += 1
        if all(map(lambda x: x.endswith("Z"), new)):
            return steps
        current = new


def part2(nodes_dict, instructions):
    starting = [node for node in nodes_dict if node.endswith("A")]
    all_steps = []
    steps = 0
    for node in starting:
        steps = 0
        current = node
        for element in instructions:
            current = nodes_dict[current][int(element)]
            steps += 1
            if current.endswith("Z"):
                break
        all_steps.append(steps)
    return math.lcm(*all_steps)


if __name__ == "__main__":
    raw_data = [line.strip() for line in fileinput.input()]
    instructions = cycle(raw_data[0].replace("R", "1").replace("L", "0"))
    nodes_dict = {node[:3]: (node[7:10], node[12:15]) for node in raw_data[2:]}
    print(part2(nodes_dict, instructions))
