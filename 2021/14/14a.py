import fileinput
import re
from collections import Counter


def step(old_string):
    new_string = ""
    for i, first in enumerate(old_string):
        try:
            second = old_string[i+1]
        except IndexError:
            break
        else:
            new_string += first + all_pairs[first+second]
    new_string += old_string[-1]
    return new_string


data = [line.strip() for line in fileinput.input()]

all_pairs = {}
for d in data[2:]:
    match = re.search(r"(\w{2}) -> (\w)", d)
    if match:
        all_pairs[match.group(1)] = match.group(2)


old = data[0]
for i in range(10):
    new = step(old)
    old = new

c = Counter(new)
by_occurrence = c.most_common()
print(by_occurrence[0][1] - by_occurrence[-1][1])
