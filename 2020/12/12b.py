import fileinput
from collections import namedtuple


class Ship:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.waypoint = (10, -1)

    def __repr__(self):
        return f"x: {self.x}, y: {self.y}, waypoint: {self.waypoint}"

    def rotate(self, instruction):
        steps = instruction.value // 90
        for step in range(steps):
            x, y = self.waypoint
            if instruction.type == "L":
                self.waypoint = y, -x
            else:
                self.waypoint = -y, x

    def go_forward(self, instruction):
        new_x, new_y = self.waypoint
        self.x = self.x + new_x * instruction.value
        self.y = self.y + new_y * instruction.value

    def move_waypoint(self, instruction):
        x, y = self.waypoint
        if instruction.type == "N":
            self.waypoint = x, y-instruction.value
        elif instruction.type == "E":
            self.waypoint = x+instruction.value, y
        elif instruction.type == "S":
            self.waypoint = x, y+instruction.value
        elif instruction.type == "W":
            self.waypoint = x-instruction.value, y

    def parse_instructions(self, instruction):
        if instruction.type in ("R", "L"):
            self.rotate(instruction)
        elif instruction.type == "F":
            self.go_forward(instruction)
        else:
            self.move_waypoint(instruction)


def read_instructions():
    instruction = namedtuple("Instruction", "type value")
    instructions = []
    for line in fileinput.input():
        instructions.append(instruction(line[0], int(line[1:])))
    return instructions


def main():
    instructions = read_instructions()
    ship = Ship()
    for instruction in instructions:
        ship.parse_instructions(instruction)
    print(abs(ship.x+ship.y))


if __name__ == "__main__":
    main()
