import fileinput
import re


def calculate(mask, place, number):
    inp = [x for x in f'{number:036b}']
    for i, sym in enumerate(mask):
        if sym != "X":
            inp[i] = sym
    inp = "".join(inp)
    inp = int(inp, 2)
    memory[place] = inp


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
