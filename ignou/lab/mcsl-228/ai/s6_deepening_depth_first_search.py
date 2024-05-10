class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, u, v):
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        self.adjacency_list[u].append(v)

    def dls(self, start_node, target, max_depth):
        if start_node == target:
            return True
        if max_depth <= 0:
            return False
        if start_node not in self.adjacency_list:
            return False

        for neighbor in self.adjacency_list[start_node]:
            if self.dls(neighbor, target, max_depth - 1):
                return True
        return False

    def iddfs(self, start_node, target, max_depth):
        for depth in range(max_depth + 1):
            if self.dls(start_node, target, depth):
                return True
        return False

# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(2, 6)

start_node = 0
target = 6
max_depth = 3

print("IDDFS from", start_node, "to", target, "with max depth", max_depth, ":")
print(g.iddfs(start_node, target, max_depth))
