import fileinput
import itertools


contents = [int(line.strip()) for line in fileinput.input()]
preamble = 25


for number in contents[preamble:]:
    to_check = itertools.combinations(contents[:preamble], 2)
    to_check_list = list(to_check)
    for item in to_check_list:
        if sum(item) == number:
            del contents[0]
            break
    else:
        print(number)
        break
