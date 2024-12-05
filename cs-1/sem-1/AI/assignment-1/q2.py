# 2. Write a program to implement depth-first search traversal.

def dfs(graph, start_node, visited=None):
    if visited is None:
        visited = set()
    visited.add(start_node)
    traversal = [start_node]
    
    for neighbor in graph[start_node]:
        if neighbor not in visited:
            traversal.extend(dfs(graph, neighbor, visited))
    
    return traversal

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': ['G'],
    'E': [],
    'F': ['G'],
    'G': []
}

# Run DFS starting from node 'A'
dfs_result = dfs(graph, 'A')
dfs_result
