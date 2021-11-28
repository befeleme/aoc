"""
Puzzle 2:
Each policy actually describes two positions in the password,
where 1 means the first character, 2 means the second character, and so on.
(Be careful; Toboggan Corporate Policies have no concept of "index zero"!)
Exactly one of these positions must contain the given letter.
Other occurrences of the letter are irrelevant for the purposes of policy enforcement.
"""
import re

with open("input_2", "r", encoding="utf-8") as f:
    contents = f.readlines()

# Example line: "1-3 a: abcde"
parsed = re.compile("(\d+)-(\d+)\s([a-z]):\s(\w+)")

total_count = 0

for line in contents:
    matched = parsed.match(line)

    first_to_check, second_to_check, to_look, password = matched.groups()

    pattern = re.compile(to_look)

    # I need an index here, so -1
    matched_1 = pattern.match(password, int(first_to_check) - 1)
    matched_2 = pattern.match(password, int(second_to_check) - 1)

    # Only a match in one of the positions is valid
    if (matched_1 and not matched_2) or (matched_2 and not matched_1):
        total_count += 1

print(f"There are {total_count} passwords that match the rules.")
