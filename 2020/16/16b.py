import fileinput
import re


def check_rules(rules, number):
    for rule in rules:
        a = int(rule[1]) <= number <= int(rule[2])
        b = int(rule[3]) <= number <= int(rule[4])
        if (a or b):
            return True
    return False


def check_rule(rule, number):
    a = int(rule[1]) <= number <= int(rule[2])
    b = int(rule[3]) <= number <= int(rule[4])
    if (a or b):
        return True
    return False


def parse_numbers(line):
    """Return list of numbers from the given input"""
    numbers = []
    matched = re.finditer(r'(\d+)', line)
    for match in matched:
        numbers.append(int(match.group()))
    return numbers


def get_nth_tickets(number):
    """Gets all 0th, 1st and so on number from each ticket."""
    tickets = []
    for i, ticket in enumerate(valid_tickets):
        tickets.append(valid_tickets[i][number])
    return tickets


def find_all_matching(rules, valid_tickets):
    all_matching_indices = {}
    # Start checking the rules on tickets
    for rule in rules:
        # print("checking rule", rule[0])
        for index in range(len(valid_tickets[0])):
            matching = True
            # check the rule against each 0th, 1st... number on tickets
            for number in get_nth_tickets(index):
                if not check_rule(rule, number):
                    matching = False
            if matching:
                matching_indices = all_matching_indices.get(rule[0])
                # Occurs first time - add to dictionary
                if not matching_indices:
                    all_matching_indices[rule[0]] = [index]
                # Occurs multiple times - append to values list
                else:
                    matching_indices.append(index)
                    all_matching_indices[rule[0]] = matching_indices
    return all_matching_indices


def parse_input():
    contents = [line.strip() for line in fileinput.input()]
    pattern = re.compile(r"(\S+\s*\S*): (\d+)-(\d+) or (\d+)-(\d+)")
    rules = []
    for line in contents:
        try:
            matched = re.search(pattern, line).groups()
            rules.append(matched)
        except AttributeError as e:
            break

    for i, line in enumerate(contents):
        if line.startswith("your"):
            your_ticket = contents[i+1]
        if line.startswith("nearby"):
            input_tickets = contents[i+1:]
            break
    return rules, your_ticket, input_tickets


def find_nearby_tickets(input_tickets):
    nearby_tickets = []
    for line in input_tickets:
        numbers = parse_numbers(line)
        nearby_tickets.append(numbers)
    return nearby_tickets


def find_valid_tickets(input_tickets):
    nearby_tickets = find_nearby_tickets(input_tickets)
    valid_tickets = []
    for line in nearby_tickets:
        valid = True
        for number in line:
            if not check_rules(rules, number):
                valid = False
        if valid:
            valid_tickets.append(line)
    return valid_tickets


def find_one_possible_value(sorted_values, all_matching_indices):
    """Return the value that has only one element."""
    for key, value in all_matching_indices.items():
        if len(value) == 1:
            sorted_values[key] = value[0]
            return value[0]


def erase_value(value, all_matching_indices):
    """Delete the given element from values of each dict key."""
    for val in all_matching_indices.values():
        if value in val:
            val.remove(value)


rules, your_ticket, input_tickets = parse_input()
valid_tickets = find_valid_tickets(input_tickets)
your_ticket = parse_numbers(your_ticket)
valid_tickets.append(your_ticket)
all_matching_indices = find_all_matching(rules, valid_tickets)

# This will find the only possible index number for each ticket key
sorted_values = {}
for i in range(len(all_matching_indices)):
    value = find_one_possible_value(sorted_values, all_matching_indices)
    erase_value(value, all_matching_indices)

# And this will find the value on respective index on your ticket
departure_vals = 1
for key, val in sorted_values.items():
    if key.startswith("departure"):
        value = your_ticket[val]
        departure_vals *= value

print(departure_vals)
