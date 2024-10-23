class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, node1, node2):
        if node1 not in self.adj_list:
            self.adj_list[node1] = []
        self.adj_list[node1].append(node2)
        if node2 not in self.adj_list:
            self.adj_list[node2] = []
        self.adj_list[node2].append(node1)

    def breadth_first_search(self, start, goal):
        if start not in self.adj_list and goal not in self.adj_list:
            return None
        queue = [[start]]
        visited = {start}
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == goal:
                return path
            for neighbor in self.adj_list[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(path + [neighbor])
        return None
    
    def depth_first_search(self, start, goal):
        if start not in self.adj_list or goal not in self.adj_list:
            return None
        stack = [[start]]
        visited = {start}
        while stack:
            path = stack.pop()
            node = path[-1]
            if node == goal:
                return path
            for neighbor in self.adj_list[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(path + [neighbor])
        return None
    
graph = Graph()
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("B", "E")
graph.add_edge("C", "F")
graph.add_edge("C", "G")
graph.add_edge("D", "H")
graph.add_edge("E", "I")
graph.add_edge("F", "J")
graph.add_edge("G", "K")
bfs_path = graph.breadth_first_search("A", "I")
print("BFS Path to I:", bfs_path)  
dfs_path = graph.depth_first_search("A", "I")
print("DFS Path to I:", dfs_path)  