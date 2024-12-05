# 1. Write a program to implement breadth-first search traversal.

from collections import deque

def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])
    traversal = []

    while queue:
        current_node = queue.popleft()
        if current_node not in visited:
            visited.add(current_node)
            traversal.append(current_node)
            queue.extend(graph[current_node])
    
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

# Run BFS starting from node 'A'
bfs_result = bfs(graph, 'A')
bfs_result
