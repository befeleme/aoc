import fileinput
import re

data = [line.strip() for line in fileinput.input()]

first_total = 0
second_total = 0
pattern = r"(\d+)"
for section_assgnmt in data:
    matched = re.findall(pattern, section_assgnmt)
    if matched:
        matched = [int(x) for x in matched]
        first_from, first_to = int(matched[0]), int(matched[1])
        second_from, second_to = int(matched[2]), int(matched[3])

        first_range = range(first_from, first_to+1)
        second_range = range(second_from, second_to+1)

        if set(first_range) <= set(second_range) or \
            set(second_range) <= set(first_range):
            first_total += 1

        if not set(first_range).isdisjoint(set(second_range)) and \
            not set(second_range).isdisjoint(set(first_range)):
            second_total += 1

print(first_total, second_total)    
