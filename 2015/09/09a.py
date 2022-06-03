import re


with open("input", "r") as f:
    routes = f.read().splitlines()

route_map = {}
all_dests = set()

pattern = r"(\w+) to (\w+) = (\d+)"
for route in routes:
    if (matched := re.match(pattern, route)) is not None:
        departure = matched.group(1) 
        destination = matched.group(2)
        distance = int(matched.group(3))
        all_dests.add(departure)
        all_dests.add(destination)
        # Key: tuple of alphabetically sorted departure and destination places for easier lookup
        route_map[tuple(sorted([departure, destination]))] = distance

all_subtotals = set()

def count_distances(subtotal, visited_destinations):
    # base condition = we've traversed all the way through
    if len(visited_destinations) == len(all_dests):
        all_subtotals.add(subtotal)
        return
    
    current_departure = visited_destinations[-1]
    for next_dest in all_dests:
        if next_dest not in visited_destinations:
            new_subtotal = subtotal + route_map[tuple(sorted([current_departure, next_dest]))]
            new_visited_dests = list(visited_destinations)
            new_visited_dests.append(next_dest)
            count_distances(new_subtotal, new_visited_dests)

for departure in all_dests:
    count_distances(0, [departure])

print(min(all_subtotals))
print(max(all_subtotals))