import fileinput
from enum import Enum
from collections import namedtuple


class Direction(Enum):
    N = 0
    E = 90
    S = 180
    W = 270

    def __add__(self, other):
        return Direction((self.value + other.value) % 360)

    def __sub__(self, other):
        return Direction((self.value - other.value) % 360)

    def rotate(self, rotation):
        if rotation.type == "L":
            return self - rotation
        return self + rotation


class Ship:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = Direction.E

    def __repr__(self):
        return f"x: {self.x}, y: {self.y}, direction: {self.direction}"

    def rotate(self, rotation):
        self.direction = self.direction.rotate(rotation)

    def go_forward(self, instruction):
        delta = self._get_delta(self.direction)
        self._move(delta, instruction)

    def move(self, instruction):
        delta = self._get_delta(instruction.type)
        self._move(delta, instruction)

    def _get_delta(self, direction):
        deltas = {
            Direction.N: (0, -1),
            Direction.E: (1, 0),
            Direction.S: (0, 1),
            Direction.W: (-1, 0),
        }
        return deltas[direction]

    def _move(self, delta, instruction):
        self.x = self.x + delta[0] * instruction.value
        self.y = self.y + delta[1] * instruction.value

    def parse_instructions(self, instruction):
        if instruction.type in ("R", "L"):
            self.rotate(instruction)
        elif instruction.type == "F":
            self.go_forward(instruction)
        else:
            self.move(instruction)


def read_instructions():
    instruction = namedtuple("Instruction", "type value")
    instructions = []
    directions = {
        "N": Direction.N,
        "E": Direction.E,
        "S": Direction.S,
        "W": Direction.W,
        }
    for line in fileinput.input():
        val = directions.get(line[0], line[0])
        instructions.append(instruction(val, int(line[1:])))
    return instructions


def main():
    instructions = read_instructions()
    ship = Ship()
    for instruction in instructions:
        ship.parse_instructions(instruction)
    print(ship.x + ship.y)


if __name__ == "__main__":
    main()
