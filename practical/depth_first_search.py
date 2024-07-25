def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    dfs_order.append(start)
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return dfs_order

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_vertex = 'A'
dfs_order = []
dfs(graph, start_vertex)
print("DFS Order:", dfs_order)
