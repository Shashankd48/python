# Write a Python Program to implement Depth First Search.

class Graph:
    def __init__(self):
        # Initialize an empty dictionary to store the graph
        self.graph = {}

    def add_edge(self, u, v):
        # Add edge from vertex u to vertex v
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs_util(self, v, visited):
        # Mark the current vertex as visited and print it
        visited.add(v)
        print(v, end=' ')

        # Recur for all the vertices adjacent to this vertex
        if v in self.graph:
            for neighbor in self.graph[v]:
                if neighbor not in visited:
                    self.dfs_util(neighbor, visited)

    def dfs(self, start):
        # Create a set to store visited vertices
        visited = set()

        # Call the recursive helper function to print DFS traversal
        self.dfs_util(start, visited)


# Example usage:
if __name__ == "__main__":
    # Create a graph object
    g = Graph()
    
    # Add edges to the graph
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    # Perform DFS traversal starting from vertex 2
    print("\nDepth First Traversal starting from vertex 2:")
    g.dfs(2)
