import fileinput
from collections import defaultdict

def is_number(a):
    try:
        int(a)
        return True
    except ValueError:
        return False

def process(inp, vars, instructions):
    for line in instructions:
        line = line.split()
        if line[0] == "inp":
            vars[line[1]] = inp[0]
            del inp[0]
        
        elif line[0] == "add":
            if is_number(line[2]):
                vars[line[1]] = vars[line[1]] + int(line[2])
            else:
                vars[line[1]] = vars[line[1]] + vars[line[2]]
        
        elif line[0] == "mul":
            if is_number(line[2]):
                vars[line[1]] = vars[line[1]] * int(line[2])
            else:
                vars[line[1]] = vars[line[1]] * vars[line[2]] 

        elif line[0] == "div":
            if is_number(line[2]):
                vars[line[1]] = vars[line[1]] // int(line[2])
            else:
                vars[line[1]] = vars[line[1]] // vars[line[2]]

        elif line[0] == "mod":
            if is_number(line[2]):
                vars[line[1]] = vars[line[1]] % int(line[2])
            else:
                vars[line[1]] = vars[line[1]] % vars[line[2]]

        elif line[0] == "eql":
            if is_number(line[2]):
                if vars[line[1]] == int(line[2]):
                    vars[line[1]] = 1
                else:
                    vars[line[1]] = 0
            else:
                if vars[line[1]] == vars[line[2]]:
                    vars[line[1]] = 1
                else:
                    vars[line[1]] = 0
    return vars



data = [line.strip() for line in fileinput.input()]
instructions = defaultdict(list)
i = 1
for line in data:
    if line == "":
        i += 1
    else:
        instructions[i].append(line)

processed = {}

for i in range(1, 10):
    to_process = [i]
    vars = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
    to_process = [i]
    new_vars = process(to_process, vars, instructions[1])
    processed[new_vars["z"]] = i

new_processed = {}
for j in range(2, 15):
    for i in range(1, 10):
        # to_process = [i]
        for zets, inp in processed.items():
            # print(inp, vars)
            vars = {'w': 0, 'x': 0, 'y': 0, 'z': zets}
            vars_to_change = dict(vars)
            to_process = [i]
            new_vars = process(to_process, vars_to_change, instructions[j])
            key_is_present = new_processed.get(new_vars["z"], 999999999999999)
            if key_is_present > int(str(inp) + str(i)):
                new_processed[new_vars["z"]] = int(str(inp) + str(i))

    processed = new_processed
    new_processed = {}

print(processed[0])
