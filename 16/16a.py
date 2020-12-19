import fileinput
import re


def check_rules(rules, number):
    for rule in rules:
        a = int(rule[0]) <= number <= int(rule[1])
        b = int(rule[2]) <= number <= int(rule[3])
        if (a or b):
            return True
    return False


contents = [line.strip() for line in fileinput.input()]
pattern = re.compile(r"(\d+)-(\d+) or (\d+)-(\d+)")
rules = []
for line in contents:
    try:
        matched = re.search(pattern, line).groups()
        rules.append(matched)
    except AttributeError as e:
        break

for i, line in enumerate(contents):
    if line.startswith("nearby"):
        input_tickets = contents[i+1:]
        break

nearby_tickets = []
for line in input_tickets:
    numbers = []
    matched = re.finditer(r'(\d+)', line)
    for match in matched:
        numbers.append(int(match.group()))
    nearby_tickets.append(numbers)


invalid_tickets = []
for line in nearby_tickets:
    for number in line:
        if not check_rules(rules, number):
            invalid_tickets.append(number)
print(sum(invalid_tickets))
