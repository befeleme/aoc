import fileinput
import re

from functools import reduce
from operator import mul


CUBES_IN_1ST_GAME = {
    "blue": 14,
    "green": 13,
    "red": 12,
}

GAME_NO = re.compile(r"Game (\d+)")
AMOUNT_AND_COLOR = re.compile(r"(\d+) (\w+)+")


def part1(games):
    total = 0
    for game in games:
        for amount, color in re.findall(AMOUNT_AND_COLOR, game):
            if int(amount) > CUBES_IN_1ST_GAME[color]:
                break
        else:
            total += int(re.match(GAME_NO, game).group(1))
    return total


def part2(games):
    total = 0
    for game in games:
        cubes_in_game = {}
        for amount, color in re.findall(AMOUNT_AND_COLOR, game):
            amount = int(amount)
            if cubes_in_game.get(color, 0) < amount:
                cubes_in_game[color] = amount
        total += reduce(mul, cubes_in_game.values())
    return total


if __name__ == "__main__":
    games = [line.strip() for line in fileinput.input()]
    print(part1(games))
    print(part2(games))