import fileinput
import re

examples = [x.strip() for x in fileinput.input()]

# Get rules from examples, create dictionary rule no: value
rules = {}
for example in examples:
    matched = re.search(r'(\d+): (.+)', example)
    if matched:
        value = matched.group(2).split()
        if "a" in value[0] or "b" in value[0]:
            value = value[0][1]
        rules[matched.group(1)] = value

# Get examples to check with the rules
to_check = []
for example in examples:
    if example.startswith("a") or example.startswith("b"):
        to_check.append(example)


def fill_rules(rules):
    """Change values in rules for pattern for regex"""
    for key, rule in rules.items():
        # print(values)
        for char in rule:
            # print(value)
            if char.isdigit():
                # print("value", value)
                found = rules.get(char)
                # If it's a list, skip for now
                if isinstance(found, list):
                    continue
                else:
                    # print("found", found)
                    rule[rule.index(char)] = found
        fill_in_regex(key, rule)


def fill_in_regex(key, value):
    """Take values in list and prepare a string in regex format.
    If there is a digit in value, don't change anything,
    it's not ready yet.
    This implementation makes toooo many parenthesis in the effect,
    but for regex this doesn't matter."""
    to_string = ""
    for i in value:
        ready = True
        if i.isdigit():
            ready = False
            break
        to_string += i
    if ready:
        if len(to_string) > 1:
            rules[key] = f"({to_string})"
        else:
            rules[key] = to_string


def is_match(pattern, example):
    matched = re.search(pattern, example)
    if not matched:
        return
    else:
        try:
            rest = matched.group("rest")
            if not rest:
                return True
        except IndexError:
            return True
        else:
            a = is_match(match_all_42, rest)
            return a if a else is_match(match_11, rest)


# Loop through rules until the rule 0 changes to string
while isinstance(rules["0"], list):
    fill_rules(rules)

# Change in rules
# 8: 42 | 42 8
# 11: 42 31 | 42 11 31
# 0: 8 11
rule_42 = rules["42"]
rule_31 = rules["31"]

# Define patterns to check
# 1st - default, all must fulfill it
# Then it may be either 42 to the end or some combination of 42 and 31
# (42 count must be exactly the same as or more than 31)
# Go through pattern and cut out the possibilities to match only the right ones
# 0 means: Twice 42 on the beginning, once 31 on the end
default_pattern = re.compile(r"^(" + rule_42 + "){2}(?P<rest>.*)(" + rule_31 + ")$")
match_all_42 = re.compile(r"^(" + rule_42 + ")+$")
match_11 = re.compile(r"^(" + rule_42 + ")(?P<rest>.*)(" + rule_31 + ")$")


counter = 0
for example in to_check:
    if is_match(default_pattern, example):
        counter += 1
print(counter)

# First working implementation, replaced with is_match()
# counter = 0
# for example in to_check:
#     matched = re.search(default_pattern, example)
#     if matched:
#         rest = matched.group("rest")
#         if not rest:
#             # whole example has been processed - it's a match!
#             counter += 1
#         while rest:
#             new_matched = re.search(match_all_42, rest)
#             if new_matched:
#                 # 42's till the end of regex, it's a match!
#                 counter += 1
#                 break
#             else:
#                 # Check for rule 11 in the remaining example part
#                 new_matched = re.search(match_11, rest)
#                 if new_matched:
#                     rest = new_matched.group("rest")
#                     if not rest:
#                         # whole example has been processed - it's a match!
#                         counter += 1
#                         break
#                 else:
#                     break
