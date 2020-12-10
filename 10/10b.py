import fileinput


contents = [int(line.strip()) for line in fileinput.input()]

# Add outlet and device joltages (0 and max+3 of the list)
contents.extend([0, max(contents) + 3])
contents.sort()
# I want to run it from the highest value
contents.reverse()

rolling_adapters = dict()


def count_arrangements(joltage, in_contents):
    # Get last value from the adapters dict and add it to currents
    curr_value = 0
    for item in in_contents:
        last_val = rolling_adapters.get(item, 0)
        curr_value += last_val
    rolling_adapters[joltage] = curr_value


# Start - first number has one possible arrangement
rolling_adapters[contents[0]] = 1
# Continue - 2nd number till the end
for joltage in contents[1:]:
    # Find matching possibilities in the actual list
    to_check = set((joltage+1, joltage+2, joltage+3))
    in_contents = to_check.intersection(set(contents))
    count_arrangements(joltage, in_contents)

print(rolling_adapters[0])
