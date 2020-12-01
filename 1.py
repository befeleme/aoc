"""Specifically, they need you to find the two/three entries that sum to 2020 and then multiply those two/three numbers together."""

import itertools

with open("input_1", "r", encoding="utf-8") as f:
    contents = [int(x) for x in f.readlines()]

# 1st puzzle part
combined = itertools.combinations(contents, 2)
for a, b in list(combined):
    if a + b == 2020:
        print("It's a match!", a, b)
        print("And the solution is...", a*b)

# 2nd puzzle part
combined = itertools.combinations(contents, 3)
for a, b, c in list(combined):
    if a + b + c == 2020:
        print("It's a match!", a, b, c)
        print("And the solution is...", a*b*c)
