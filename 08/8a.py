import fileinput


def traverse_instructions(index, acc_val, indices_passed):
    if index in indices_passed:
        return acc_val
    indices_passed.append(index)
    if contents[index][0] == "nop":
        new_index = index + 1
    elif contents[index][0] == "acc":
        acc_val += contents[index][1]
        new_index = index + 1
    elif contents[index][0] == "jmp":
        new_index = index + contents[index][1]
    return traverse_instructions(new_index, acc_val, indices_passed)


if __name__ == "__main__":
    contents = [(line[:3], int(line[4:].strip())) for line in fileinput.input()]

    # Start with 1st instruction
    # accelerator value is initially 0
    # There are no indices passed at the beginning
    print(traverse_instructions(0, 0, []))
