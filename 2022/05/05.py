# test -> CMZ

"""
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2

In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.

Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 

In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:

        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3

Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:

        [Z]
        [N]
[M]     [D]
[C]     [P]
 1   2   3

Finally, one crate is moved from stack 1 to stack 2:

        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3

The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.
"""

import fileinput
import re

data = [line.strip('\n') for line in fileinput.input()]
# print(data)

cargos = [[] for i in range(9)]
for row in data[:8]:
    next_cargo = 0
    # print(row[1], row[5], row[9])
    for i in range(1, len(row), 4):
        if row[i] != " ":
            cargos[next_cargo].insert(0, row[i])
        next_cargo += 1

# print(cargos)

for move in data[10:]:
    pattern = r"move (\d+) from (\d) to (\d)"
    matched = re.match(pattern, move)
    if matched:
        how_many, col_from, col_to = (int(x) for x in matched.groups())
        col_from = col_from-1
        col_to = col_to-1
        cargos[col_to].extend(cargos[col_from][-how_many:])
        for _ in range(how_many):
            cargos[col_from].pop()
        # for _ in range(how_many):
        #     cargos[col_to].append(cargos[col_from].pop())

for cargo in cargos:
    print(cargo[-1], end="")

print()