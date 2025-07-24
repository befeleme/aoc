import fileinput
import re


MAP_NAME = re.compile(r"(\w+)-to-(\w+)")
GARDEN_RANGES = re.compile(r"(\d+)")
ORDER = ["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]
SEEDS = [2982244904, 337763798]

def parse(data):
    mapping = {}
    for line in data[1:]:
        if line == "":
            continue
        elif match := re.search(MAP_NAME, line):
            current_map = match
            mapping[current_map.group(0)] = {current_map.group(1): [], current_map.group(2): []}
        else:
            r = list(map(int, re.findall(GARDEN_RANGES, line)))
            mapping[current_map.group(0)][current_map.group(1)].append(range(r[1], r[1]+r[2]))
            mapping[current_map.group(0)][current_map.group(2)].append(range(r[0], r[0]+r[2]))
    return mapping


def part1(almanac):
    locations = []
    for my_val in SEEDS:
        for i, key_name in enumerate(ORDER):
            for mapping_key, values in almanac.items():
                if mapping_key.startswith(key_name):
                    for a, b in zip(values[key_name], values[ORDER[i+1]]):
                        if my_val in a:
                            my_val = b[a.index(my_val)]
                            break
        locations.append(my_val)
    print(min(locations))


def count_seeds():
    real_seeds = []
    while SEEDS:
        starting = SEEDS.pop(0)
        count = SEEDS.pop(0)
        # print(starting, count)
        real_seeds.append((range(starting, starting+count)))
    return real_seeds

def part2(almanac):
    with open("output", "a") as f:

        location = 99999999999999999999999999999999999999999
        for my_val in range(3165202104, 3165206704):
            print("starting with", my_val, file=f)

            for i, key_name in enumerate(ORDER):
                for mapping_key, values in almanac.items():
                    if mapping_key.startswith(key_name):
                        for a, b in zip(values[key_name], values[ORDER[i+1]]):
                            if my_val in a:
                                my_val = b[a.index(my_val)]
                                break
            if my_val < location:
                location = my_val
                print("new minimum", location, file=f)
        print(location)


if __name__ == "__main__":
    raw_data = [line.strip() for line in fileinput.input()]
    almanac = parse(raw_data)
    part2(almanac)