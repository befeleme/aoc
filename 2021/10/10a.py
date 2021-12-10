import fileinput
from collections import deque


data = [line.strip() for line in fileinput.input()]

opening = ("[", "(", "{", "<")
closing = ("]", ")", "}", ">")
scores = {
    "]": 57,
    ")": 3,
    "}": 1197,
    ">": 25137,
}

d = deque()
s = 0
for line in data:
    for parenthesis in line:
        if parenthesis in opening:
            d.append(parenthesis)
        elif parenthesis in closing:
            last_open = d.pop()
            if opening.index(last_open) == closing.index(parenthesis):
                continue
            else:
                s += scores[parenthesis]

print(s)