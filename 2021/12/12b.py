import fileinput
from dataclasses import dataclass
from collections import Counter

@dataclass()
class Node:
    name: str
    neighbors: list


@dataclass
class Caves:
    nodes = []
    path = []
    paths = []

    def find_node_in_caves(self, name):
        res = list(filter(lambda x: x.name == name, self.nodes))
        return res[0] if res else False

    # def how_many_times_visited(self, name, path):
    #     res = list(filter(lambda x: x.name == name, path))
    #     return len(res) if res else False

    def can_still_be_visited(self, node_name, path):
        res = [node.name for node in path]
        c = Counter(res)
        # once_only = ["start", "end"]
        # print(c)
        if node_name not in c:
            return True
        for name in c:
            # print("checking", name)
            if name.upper() == name:
                # print("upper, don't check")
                continue
            else:
                # print(name, c[name])
                if c[name] > 1:
                    return False
        else:
            return True

        # res = list(filter(lambda x: x.name == name, path))
        # return len(res) if res else False

    def add_nodes(self, a, b):
        if b == "start":
            return
        if (node := self.find_node_in_caves(a)):
            if b not in node.neighbors:
                node.neighbors.append(b)
        else:
            self.nodes.append(Node(a, [b]))

    def find_path(self):
        start_node_name = "start"
        start_node = self.find_node_in_caves(start_node_name)
        path = [start_node]
        for neighbour_name in start_node.neighbors:
            new_path = list(path)
            neighbour = self.find_node_in_caves(neighbour_name)
            new_path.append(neighbour)
            self.find_next(new_path)

    def is_valid_move(self, node, path):
        is_big_cave = (node.upper() == node)
        # print("big", is_big_cave)
        if is_big_cave:
            return True
        else:
            if self.can_still_be_visited(node, path):
                return True
            else:
                return False
        # is_already_visited = True  and not is_big_cave else False
        # print("visited", is_already_visited)
        # return False if is_already_visited else True

    def find_next(self, path):
        # print("path", path)

        if path[-1].name == "end":
            # print("ending")
            self.paths.append(path)
            # print("path", path)
            return
        else:

            for neighbour_name in path[-1].neighbors:
                neighbour = self.find_node_in_caves(neighbour_name)
                # print("neigh", neighbour)
                valid = self.is_valid_move(neighbour_name, path)
                # print("valid", valid)
                if valid:
                    new_path = list(path)
                    new_path.append(neighbour)
                    self.find_next(new_path)
                # else:
                #     continue


data = [line.strip().split('-') for line in fileinput.input()]
# print(data)
c = Caves()
for a, b in data:
    c.add_nodes(a, b)
    c.add_nodes(b, a)

# for node in c.nodes:
# #     for neighbor in node.neighbors:
# #         print(neighbor)
#     print(node.neighbors)
# print("nodes", c.nodes)
c.find_path()
print(len(c.paths))
# print(len(c.nodes[0].neighbors))
# print(len(c.nodes))