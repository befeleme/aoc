label = [int(char) for char in "219347865"]
MOD_VAL = len(label)


def rotate(cups, curr_cup, index):
    if cups[index] == curr_cup:
        return cups
    else:
        cups = cups[1:] + cups[:1]
        return rotate(cups, curr_cup, index)


for i in range(100):
    curr_index = i % MOD_VAL
    curr_cup = label[curr_index]
    pick_up = [
        label[(curr_index+1) % MOD_VAL],
        label[(curr_index+2) % MOD_VAL],
        label[(curr_index+3) % MOD_VAL],
    ]
    new_label = []
    for cup in label:
        if cup not in pick_up:
            new_label.append(cup)

    # Find destination cup
    dest_cup = curr_cup - 1
    while True:
        if dest_cup < min(new_label):
            dest_cup = max(new_label)
            break
        elif dest_cup in pick_up:
            dest_cup -= 1
        else:
            break

    cut_index = new_label.index(dest_cup)
    label = new_label[:cut_index+1] + pick_up + new_label[cut_index+1:]
    label = rotate(label, curr_cup, curr_index)

cups = rotate(label, 1, 0)
to_str = [str(x) for x in cups]
string_cups = "".join(to_str[1:])
print(string_cups)
