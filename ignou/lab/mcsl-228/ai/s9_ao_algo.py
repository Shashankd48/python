# Write a Python Program to implement AO* Algorithm

import heapq

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, u, v, weight):
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        self.adjacency_list[u].append((v, weight))

    def ao_star(self, start_node, target_node):
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
                        new_cost = cost + weight
                        heapq.heappush(priority_queue, (new_cost, neighbor, path + [current_node]))
                        # Update the cost of previously visited nodes
                        for i, (p_cost, p_node, p_path) in enumerate(priority_queue):
                            if p_node == neighbor:
                                priority_queue[i] = (new_cost, p_node, path + [current_node])
                                heapq.heapify(priority_queue)
                                break
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
g.add_edge('F', 'G', 4)

start_node = 'A'
target_node = 'E'

print("Shortest path from", start_node, "to", target_node, ":", g.ao_star(start_node, target_node))
