from collections import defaultdict
from pathlib import Path
import re


def turn_on(from_x, from_y, to_x, to_y, lights):
    for y in range(from_y, to_y+1):
        for x in range(from_x, to_x+1):
            if not lights.get((x, y)):
                lights[(x, y)] = 1
    return lights

def turn_off(from_x, from_y, to_x, to_y, lights):
    for y in range(from_y, to_y+1):
        for x in range(from_x, to_x+1):
            if lights.get((x, y)):
                del lights[(x, y)]
    return lights

def toggle(from_x, from_y, to_x, to_y, lights):
    for y in range(from_y, to_y+1):
        for x in range(from_x, to_x+1):
            if lights.get((x, y)) == 1:
                del lights[(x, y)]
            else:
                lights[(x, y)] = 1
    return lights

def _increase_brightness(from_x, from_y, to_x, to_y, lights, step):
    for y in range(from_y, to_y+1):
        for x in range(from_x, to_x+1):
                lights[(x, y)] += step
    return lights

def increase_brightness_by_one(from_x, from_y, to_x, to_y, lights):
    return _increase_brightness(from_x, from_y, to_x, to_y, lights, 1)

def increase_brightness_by_two(from_x, from_y, to_x, to_y, lights):
    return _increase_brightness(from_x, from_y, to_x, to_y, lights, 2)

def decrease_brightness(from_x, from_y, to_x, to_y, lights):
    for y in range(from_y, to_y+1):
        for x in range(from_x, to_x+1):
                if lights[(x, y)] > 0:
                    lights[(x, y)] -= 1
    return lights

def change_lights(actions, action, from_x, from_y, to_x, to_y, lights):
    return actions[action](from_x, from_y, to_x, to_y, lights)

def _solve_puzzle(lightbulb_grid, actions, ranges, pattern):
    for r in ranges:
        matched = re.finditer(pattern, r)
        for m in matched:
            action, from_x, from_y, to_x, to_y = m.groups()
            from_x, from_y, to_x, to_y = int(from_x), int(from_y), int(to_x), int(to_y)
            lightbulb_grid = change_lights(actions, action, from_x, from_y, to_x, to_y, lightbulb_grid)
    return lightbulb_grid

def part_1(ranges, pattern, actions):
    lights = _solve_puzzle({}, actions, ranges, pattern)
    return len(lights)

def part_2(ranges, pattern, actions):
    lights = _solve_puzzle(defaultdict(int), actions, ranges, pattern)
    return sum([lights[coor] for coor in lights])


part_1_actions = {
    "on": turn_on,
    "off": turn_off,
    "toggle": toggle,
}
part_2_actions = {
    "on": increase_brightness_by_one,
    "off": decrease_brightness,
    "toggle": increase_brightness_by_two,
}

ranges = Path('input').read_text().split('\n')
pattern = r'(\w+) (\d+),(\d+) through (\d+),(\d+)'
print(part_1(ranges, pattern, part_1_actions))
print(part_2(ranges, pattern, part_2_actions))
