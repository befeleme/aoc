"""
Better add some data validation, quick!

You can continue to ignore the cid field, but each other field has strict rules
about what values are valid for automatic validation:

    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most aoc.
    eyr (Expiration Year) - four digits; at least aoc and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.

Your job is to count the passports where all required fields are
both present and valid according to the above rules.
"""
import re

# That's hell. Never use regex like that in production code :D
RULES = {
    "byr": "^(19[2-9][0-9]|200[0-2])$",
    "iyr": "^20(1[0-9]|20)$",
    "eyr": "^20(2[0-9]|30)$",
    "hgt": "^(59|6[0-9]|7[0-6])(in)|(1(5[0-9]|[6-8][0-9]|9[0-3])(cm))$",
    "hcl": "^(#[0-9a-fA-F]{6})$",
    "ecl": "^(amb|blu|brn|gry|grn|hzl|oth)$",
    "pid": "^\d{9}$",
}


def is_valid(line):
    """Validate the line accoring to rules in translation table."""
    for key, value in line.items():
        val_pattern = RULES.get(key)
        if val_pattern:
            matched = re.match(val_pattern, value)
            if matched is None:
                return False
    return True


with open("input_4", "r", encoding="utf-8") as f:
    contents = f.read().split("\n\n")

counter = 0
# Example input: "ecl:blu hcl:#abc123"
pattern = re.compile("(\w{3}):(\W*\w+)")
for line in contents:
    matched = dict(pattern.findall(line))
    if (len(matched) == 8) or (len(matched) == 7) and ("cid" not in matched):
        if is_valid(matched):
            counter += 1

print(f"There are {counter} valid passports")
