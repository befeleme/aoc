import fileinput


def traverse_instructions(index, acc_val, indices_passed, instructions):
    if index in indices_passed:
        return False, acc_val
    elif index == len(instructions):
        return True, acc_val
    indices_passed.append(index)
    if instructions[index][0] == "nop":
        new_index = index + 1
    elif instructions[index][0] == "acc":
        acc_val += instructions[index][1]
        new_index = index + 1
    elif instructions[index][0] == "jmp":
        new_index = index + instructions[index][1]
    return traverse_instructions(new_index, acc_val, indices_passed, instructions)


def change_instructions(contents, position):
    changed = False
    changed_contents = []
    # Add all items before the one that will be changed
    changed_contents.extend(contents[:position])
    # Find and replace the instruction to change, the rest should stay unchanged
    for index, instruction in enumerate(contents[position:], start=position+1):
        item, value = instruction
        if item == "jmp" and not changed:
            position = index
            changed_contents.append(("nop", value))
            changed = True
        elif item == "nop" and not changed:
            position = index
            changed_contents.append(("jmp", value))
            changed = True
        else:
            changed_contents.append((item, value))
    return changed_contents, position


def call(changed_contents, position):
    result, acc_value = traverse_instructions(0, 0, [], changed_contents)
    if result:
        return result, acc_value
    else:
        changed_contents, position = change_instructions(contents, position)
        return call(changed_contents, position)


if __name__ == "__main__":
    contents = [(line[:3], int(line[4:].strip())) for line in fileinput.input()]
    print(call(contents, 0)[1])
