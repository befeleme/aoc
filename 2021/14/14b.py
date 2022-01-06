import fileinput
import re
from collections import defaultdict, Counter
from copy import deepcopy
from math import ceil


data = [line.strip() for line in fileinput.input()]


start = data[0]
all_pairs = {}
for d in data[2:]:
    match = re.search(r"(\w{2}) -> (\w)", d)
    if match:
        all_pairs[match.group(1)] = match.group(2)


polymer = defaultdict(int)

for i, first in enumerate(start):
    try:
        second = start[i+1]
    except IndexError:
        break
    else:
        polymer[first + all_pairs[first+second]] += 1
        polymer[all_pairs[first+second] + second] += 1

def step(polymer):
    new_polymer = deepcopy(polymer)
    for key in polymer:
        old_val =  polymer[key]
        to_add = all_pairs[key]
        a, b = key
        new_polymer[a + to_add] += old_val
        new_polymer[to_add + b] += old_val
        new_polymer[key] -= old_val
    return new_polymer

for i in range(39):
    new_polymer = step(polymer)
    polymer = new_polymer

c = defaultdict(int)
for key, val in polymer.items():
    a, b = key
    c[a] += val
    c[b] += val

for key in c:
    c[key] = ceil(c[key] / 2)
print(c)


c = Counter(c)
by_occurrence = c.most_common()
res = by_occurrence[0][1] - by_occurrence[-1][1]
print(res)
