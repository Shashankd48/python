# Write a Python Program to implement A* Algorithm 

import heapq

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, u, v, weight):
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        self.adjacency_list[u].append((v, weight))

    def astar(self, start_node, target_node):
        visited = set()
        priority_queue = [(0, start_node, [])]

        while priority_queue:
            cost, current_node, path = heapq.heappop(priority_queue)
            if current_node == target_node:
                return path + [current_node]
            if current_node not in visited:
                visited.add(current_node)
                for neighbor, weight in self.adjacency_list.get(current_node, []):
                    if neighbor not in visited:
                        heapq.heappush(priority_queue, (cost + weight, neighbor, path + [current_node]))
        return None

# Example usage
g = Graph()
g.add_edge('A', 'B', 4)
g.add_edge('A', 'C', 2)
g.add_edge('B', 'C', 5)
g.add_edge('B', 'D', 10)
g.add_edge('C', 'D', 3)
g.add_edge('C', 'E', 6)
g.add_edge('D', 'F', 2)
g.add_edge('E', 'F', 4)

start_node = 'A'
target_node = 'F'

print("Shortest path from", start_node, "to", target_node, ":", g.astar(start_node, target_node))
