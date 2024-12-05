# 4. Write a program to implement best-first search traversal.

from queue import PriorityQueue

def best_first_search(graph, start_node, goal_node, heuristic):
    open_set = PriorityQueue()
    open_set.put((heuristic[start_node], start_node))
    visited = set()
    traversal = []

    while not open_set.empty():
        _, current = open_set.get()
        if current in visited:
            continue
        visited.add(current)
        traversal.append(current)
        
        if current == goal_node:
            return traversal
        
        for neighbor, _ in graph[current]:
            if neighbor not in visited:
                open_set.put((heuristic[neighbor], neighbor))
    
    return None

# Example graph (adjacency list with weights)
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 5)],
    'C': [('F', 2)],
    'D': [('G', 3)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

# Example heuristic function
heuristic = {
    'A': 7, 'B': 6, 'C': 2, 'D': 1, 'E': 4, 'F': 1, 'G': 0
}

# Run Best-First Search from 'A' to 'G'
best_first_path = best_first_search(graph, 'A', 'G', heuristic)
best_first_path
