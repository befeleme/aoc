import fileinput
import re


def look_for_bags(bag_type):
    for line in contents:
        bag_contents = re.findall(content_pattern, line)
        bag = re.match(bag_pattern, line).group()
        if bag_type in bag_contents:
            primary_bags.append(bag)


contents = []
for line in fileinput.input():
    line = line.strip()
    if not line.endswith("no other bags."):
        contents.append(line)

content_pattern = re.compile(r"\d+ (\w+ \w+)")
bag_pattern = re.compile(r"^\w+ \w+")

primary_bags = []

look_for_bags('shiny gold')
for bag in primary_bags:
    look_for_bags(bag)

print(len(set(primary_bags)))
