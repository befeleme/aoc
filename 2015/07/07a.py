from pathlib import Path
import re


def values_as_numbers(connections, *wires):
    numbers = []
    for wire in wires:
        try:
            numbers.append(int(wire))
        except ValueError:
            wire_val = connections.get(wire)
            if wire_val is None:
                return False
            else:
                numbers.append(wire_val)
    return numbers


connections = {}
raw_instructions = Path('input').read_text().split('\n')

# Use a helper list to remove decoded values
# Use pattern matching to perform the matching action
# Store decoded connections in connections dict
# If value of "a" was decoded in the previous traversal, print and break - we found it
# If not, proceed (the worst case: until the instruction list is completely exhausted)
cp_raw_instructions = list(raw_instructions)
pattern = r'([\w+\s?]*) -> (\w+)'

while cp_raw_instructions:
    if (a_val := connections.get("a")) is not None:
        print(a_val)
        break
    for instruction in raw_instructions:
        if (m := re.match(pattern, instruction)):
            action, res = m.groups()
            match action.split():
                case [x, operator, y]:
                    if (numbers := values_as_numbers(connections, x, y)):
                        x, y = numbers
                        if operator == 'AND':
                            connections[res] = x & y
                        elif operator == 'LSHIFT':
                            connections[res] = x << y
                        elif operator == 'RSHIFT':
                            connections[res] = x >> y
                        elif operator == 'OR':
                            connections[res] = x | y
                        cp_raw_instructions.remove(instruction)
                case ['NOT', x]:
                    if (x := values_as_numbers(connections, x)):
                        connections[res] = ~ x[0]
                        cp_raw_instructions.remove(instruction)
                case [x]:
                    if (x := values_as_numbers(connections, x)):
                        connections[res] = x[0]
                        cp_raw_instructions.remove(instruction)
    raw_instructions = cp_raw_instructions
