# 3. Write a program to implement A* Algorithm.

from queue import PriorityQueue

def a_star_algorithm(graph, start_node, goal_node, heuristic):
    open_set = PriorityQueue()
    open_set.put((0, start_node))
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start_node] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start_node] = heuristic[start_node]
    
    while not open_set.empty():
        _, current = open_set.get()
        
        if current == goal_node:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start_node)
            return path[::-1]
        
        for neighbor, cost in graph[current]:
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic[neighbor]
                open_set.put((f_score[neighbor], neighbor))
    
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

# Run A* algorithm from 'A' to 'G'
a_star_path = a_star_algorithm(graph, 'A', 'G', heuristic)
a_star_path
