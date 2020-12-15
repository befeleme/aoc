import fileinput
import re
from itertools import product


def calculate(mask, place, number):
    inp = [x for x in f'{place:036b}']
    # Apply bitmask to the input
    for i, sym in enumerate(mask):
        if sym == "1" or sym == "X":
            inp[i] = sym

    # Fill in Xs with each possible combination of Os and 1s
    results = []
    possibilities = product("01", repeat=inp.count("X"))
    for possibility in possibilities:
        # possibility - tuple without a priori known length
        # use pos to navigate through "possibility" elements
        pos = 0
        output = list(inp)
        for i, sym in enumerate(inp):
            if sym == "X":
                output[i] = possibility[pos]
                pos += 1
        as_str = "".join(output)
        results.append(as_str)

    # Convert binary numbers in results to decimals
    # Write down the number to each of the address places
    for bin_number in results:
        deci_number = int(bin_number, 2)
        memory[deci_number] = number


contents = [line.strip() for line in fileinput.input()]
memory = {}

for line in contents:
    if line.startswith("mask"):
        mask = line[7:]
    else:
        matched = re.match(r'mem\[(\d+)\] = (\d+)', line)
        calculate(mask, int(matched.group(1)), int(matched.group(2)))

mem_sum = sum([value for value in memory.values()])
print(mem_sum)
