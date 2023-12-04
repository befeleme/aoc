import fileinput
import re

from collections import defaultdict


pattern = re.compile(r"(\d+)")


def find_my_winning(game):
    winning, chosen = game.split("|")
    winning_numbers = set(map(int, re.findall(pattern, winning)))
    chosen_numbers = set(map(int, re.findall(pattern, chosen)))
    return winning_numbers & chosen_numbers


def part1(games):
    total = 0
    for game in games:
        if my_winning := find_my_winning(game):
            total +=  2 ** (len(my_winning) - 1)
    return total


def part2(games):
    total = 0
    game_results = defaultdict(int)
    for i, game in enumerate(games, start=1):
        game_results[i] += 1
        if my_winning := find_my_winning(game):
            for k in range(game_results[i]):
                for j in range(1, len(my_winning)+1):
                    game_results[i+j] += 1
    return sum(game_results.values())


if __name__ == "__main__":
    games = [line.strip().split(":")[1] for line in fileinput.input()]
    print(part1(games))
    print(part2(games))