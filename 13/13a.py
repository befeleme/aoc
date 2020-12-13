import fileinput


contents = [x.strip() for x in fileinput.input()]
departure = int(contents[0])
buses = contents[1].split(",")

# dummy big value to start with comparing
next = 10000000000000000
for bus in buses:
    if bus != "x":
        bus = int(bus)
        next_cyclus = ((departure // bus) * bus + bus) - departure
        if next_cyclus < next:
            next = next_cyclus
            bus_no = bus

print(bus_no*next)
