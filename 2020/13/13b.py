import fileinput
from sympy.ntheory.modular import crt


contents = [x.strip() for x in fileinput.input()]
buses = contents[1].split(",")

offsets = []
looked_for_buses = []
for index, bus in enumerate(buses):
    if bus != "x":
        bus = int(bus)
        dep_offset = bus - index
        offsets.append(dep_offset)
        looked_for_buses.append(bus)


starting_timestamp = crt(looked_for_buses, offsets)[0]
print(starting_timestamp)
