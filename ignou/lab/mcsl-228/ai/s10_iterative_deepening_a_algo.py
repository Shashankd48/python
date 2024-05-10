# Write a Python Program to implement for IDA* (Iterative Deepening A*) algorithm

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, u, v, weight):
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        self.adjacency_list[u].append((v, weight))

    def heuristic(self, node, target):
        # This is a placeholder heuristic function, you should replace it with
        # an appropriate heuristic for your problem domain.
        return abs(node - target)

    def ida_star(self, start_node, target_node):
        bound = self.heuristic(start_node, target_node)
        while True:
            result, new_bound = self.search(start_node, target_node, 0, bound)
            if result == "FOUND":
                return new_bound
            if result == float('inf'):
                return None
            bound = new_bound

    def search(self, node, target, cost, bound):
        f = cost + self.heuristic(node, target)
        if f > bound:
            return f, f
        if node == target:
            return "FOUND", cost

        min_val = float('inf')
        for neighbor, weight in self.adjacency_list.get(node, []):
            result, new_bound = self.search(neighbor, target, cost + weight, bound)
            if result == "FOUND":
                return "FOUND", new_bound
            if result < min_val:
                min_val = result
        return min_val, min_val

# Example usage
g = Graph()
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 1)
g.add_edge(1, 3, 1)
g.add_edge(1, 4, 2)
g.add_edge(2, 5, 3)
g.add_edge(2, 6, 2)

start_node = 0
target_node = 6

print("IDA* from", start_node, "to", target_node, ":")
print("Shortest path cost:", g.ida_star(start_node, target_node))
