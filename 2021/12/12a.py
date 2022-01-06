import fileinput
from dataclasses import dataclass


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

    def find_visited(self, name, path):
        res = list(filter(lambda x: x.name == name, path))
        return res[0] if res else False

    # def add_nodes(self, a, b):
    #     if b == "start":
    #         return

    #     node_a = self.find_node_in_caves(a)
    #     node_b = self.find_node_in_caves(b)
    #     # if not node_a and not node_b:
    #     #     node_a = Node(a, [])
    #     #     node_b = Node(b, [])
    #     #     print("hec")
    #     # print(self.nodes)
    #     if not node_a:
    #         node_a = Node(a)
    #         self.nodes.append(node_a)
    #     if not node_b:
    #         node_b = Node(b)
    #         self.nodes.append(node_b)

    #     # print(node_a, node_b)
    #     if node_b not in node_a.neighbors:
    #         node_a.neighbors.append(node_b)

        # print("node_a", node_a)
        # if (node := self.find_node_in_caves(a)):
        #     if b not in node.neighbors:
        #         node.neighbors.append(b)
        # else:
        #     self.nodes.append(Node(a, [b]))

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
            if neighbour.name == 'end':
                self.paths.append(new_path)
                continue
            self.find_next(new_path)

    def is_valid_move(self, node, path):
        is_big_cave = (node.upper() == node)
        # print("big", is_big_cave)
        is_already_visited = True if self.find_visited(node, path) and not is_big_cave else False
        # print("visited", is_already_visited)
        return False if is_already_visited else True

    def find_next(self, path):
        # print("path", path)

        if path[-1].name == "end":
            print("ending")
            self.paths.append(path)
            print("path", path)
            return
        else:


        # print("start_node", start_node)
        # path.append(start_node)
        # if start_node.name == "end":
        #     print("ending")
        #     self.paths.append(path)
        #     return path

            for neighbour_name in path[-1].neighbors:
                neighbour = self.find_node_in_caves(neighbour_name)
                print(neighbour)
                print("valid", self.is_valid_move(neighbour_name, path))
                if self.is_valid_move(neighbour_name, path):
                    new_path = list(path)
                    new_path.append(neighbour)
                    self.find_next(new_path)
                else:
                    continue
            # if neighbour == "end":
            #     return path

        # else:
        #     print("IDK")
        #     return path

            # print(neighbour)
            # next_node = self.find_node_in_caves(neighbour)
            # print(next_node)

            # if not is_already_visited:
                # self.path.append(neighbour)
                # return self.find_next(neighbour, path)

        # self.path.append(next_node_name)
        # print(self.path)

        # neigh_counter = 0
        # # string - just a name
        # next_node_name = start_node.neighbors[neigh_counter]
        # print(next_node_name)
        # # the object
        # next_node = self.find_node_in_caves(next_node_name)
        # print(next_node)
        # is_big_cave = (next_node_name.upper() == next_node_name)
        # print(is_big_cave)
        # # if self.find_node(next_node_name, self.nodes)
        # is_already_visited = True if self.find_visited(next_node_name) and not is_big_cave else False
        # print(is_already_visited)

        # while is_already_visited:
        #     neigh_counter += 1
        #     next_node_name = start_node.neighbors[neigh_counter]
        #     print("checking", next_node_name)
        #     is_already_visited = True if self.find_visited(next_node_name) and not is_big_cave else False

        # # if next_node_name == "end":
        # #     return
        # # next_counter += 1
        # self.path.append(next_node_name)
        # print(self.path)
        # return next_node_name
        # return self.find_next(next_node_name)



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