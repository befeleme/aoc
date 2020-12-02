"""
Puzzle 1:
Each line gives the password policy and then the password.
The password policy indicates the lowest and highest number of times a given
letter must appear for the password to be valid.
For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.
"""
import re

with open("input_2", "r", encoding="utf-8") as f:
    contents = f.readlines()

# Example line: "1-3 a: abcde"
pattern = re.compile("(\d+)-(\d+)\s([a-z]):\s(\w+)")

total_count = 0

for line in contents:
    matched = pattern.match(line)

    start, stop, to_look, password = matched.groups()

    pattern_count = len(re.findall(to_look, password))

    if pattern_count in range(int(start), int(stop) + 1):
        total_count += 1

print(f"There are {total_count} passwords that match the rules.")
