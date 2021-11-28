"""
Count the number of valid passports - those that have all required fields. Treat cid as optional.
"""
import re

EXPECTED = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}

with open("input_4", "r", encoding="utf-8") as f:
    contents = f.read().split("\n\n")

counter = 0
pattern = re.compile("(\w{3}):")

for line in contents:
    matched = set(pattern.findall(line))
    if matched == EXPECTED:
        counter += 1
    # this may be an overkill for the task :)
    elif matched.issubset(EXPECTED):
        if (len(matched) == 7) and ("cid" not in matched):
            counter += 1

print(f"There are {counter} valid passports")


# Naive implementation that doesn't actually validate the keys - but works ;)
#
# counter = 0
# pattern = re.compile("(\w{3}):")
#
# for line in contents:
#     matched = pattern.findall(line)
#     if (len(matched) == 8) or (len(matched) == 7) and ("cid" not in matched):
#         counter += 1
#
# print(f"There are {counter} valid passports")
