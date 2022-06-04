def step(input_str):
    output_str = ""
    counter = 0
    cur_letter = input_str[0]
    for let in input_str:
        if let == cur_letter:
            counter += 1
        else:
            output_str += str(counter) + cur_letter
            cur_letter = let
            counter = 1
    # Empty out the last sequence in memory
    output_str += str(counter) + cur_letter
    return output_str

inp = "1113222113"
for i in range(50):
    inp = step(inp)

print(len(inp))