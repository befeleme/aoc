import fileinput
import re


def get_matched_patterns(line):
    """Return tuple of matches containing bag and its contents."""
    content_pattern = re.compile(r"(\d+) (\w+ \w+)")
    bag_pattern = re.compile(r"^\w+ \w+")
    bag_contents = re.finditer(content_pattern, line)
    bag = re.match(bag_pattern, line).group()
    return bag, bag_contents


def get_all_bags():
    """
    Fill in a dict structure of data.
    Example structure: {'light red': {'bright white': 1, 'muted yellow': 2}}
    """
    bags = {}
    for line in contents:
        bag, bag_contents = get_matched_patterns(line)
        for bag_type in bag_contents:
            # The key doesn't exist - create entry
            if not bags.get(bag):
                bags[bag] = {bag_type.group(2): int(bag_type.group(1))}
            # The key already exists = add entry to existing value
            else:
                bags[bag][bag_type.group(2)] = int(bag_type.group(1))
    return bags


def count_bags(bags, bag):
    """Recursively count the bags of each type."""
    if not bags.get(bag):
        return 1
    else:
        counter = 0
        for bag_a in bags[bag]:
            counter += count_bags(bags, bag_a) * bags[bag][bag_a]
        return counter + 1


if __name__ == "__main__":
    # Load contents for file give as 1st argument in command line
    contents = [line.strip() for line in fileinput.input()]

    # -1 = don't count the 'shiny gold' in the final number ;)
    print(count_bags(get_all_bags(), "shiny gold") - 1)
