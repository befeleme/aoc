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


# Loop through rules until the rule 0 changes to string
while isinstance(rules["0"], list):
    fill_rules(rules)

counter = 0
for example in to_check:
    rule = rules["0"]
    to_match = f"^{rule}$"
    matched = re.match(to_match, example)
    if matched:
        counter += 1

print(counter)
