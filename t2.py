from collections import deque

def breadth_first_search(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return []

def depth_first_search(graph, start, goal):
    stack = [(start, [start])]
    visited = set()

    while stack:
        node, path = stack.pop()
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
    return []

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'H'],        
    'D': [],
    'E': [],
    'F': [],
    'H': []
}

print(breadth_first_search(graph, 'A', 'H'))  
print(depth_first_search(graph, 'A', 'H'))    
