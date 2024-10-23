class Graph:
    def __init__(self):
        self.adj_list={}

    def add_edge(self, node1, node2):
        if node1 not in self.adj_list:
            self.adj_list[node1]=[]
        self.adj_list[node1].append(node2)
        if node2 not in self.adj_list:
            self.adj_list[node2]=[]
        self.adj_list[node2].append(node1)
    
    def delete_edge(self, node1, node2):
        if node1 in self.adj_list and node2 in self.adj_list[node1]:
            self.adj_list[node1].remove(node2)
        if node2 in self.adj_list and node1 in self.adj_list[node2]:
            self.adj_list[node2].remove[node1]
    
    def print_graph(self):
        for i in self.adj_list:
            print(f"{i} : {self.adj_list[i]}")
    
    def are_connected(self,node1,node2):
        if node1 in self.adj_list[node2] and node2 in self.adj_list[node1]:
            return True
        return False
    
    def get_edge(self,node1,node2):
        if self.are_connected(node1,node2):
            return (node1,node2)
        return None
    
    def is_valid_path(self, path):
        for i in range(len(path)-1):
            if not self.are_connected(path[i],path[i+1]):
                return False
        return True
    
graph=Graph()

graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("C", "D")
graph.add_edge("D", "E")
# print("Graph adjacency list")
# graph.print_graph()

path1 = ["A", "B", "D"]
path2 = ["A", "C", "D", "E"]
path3 = ["A", "B", "E"]

print("Path1 valid:", graph.is_valid_path(path1))  
print("Path2 valid:", graph.is_valid_path(path2))  
print("Path3 valid:", graph.is_valid_path(path3))  

print("\n")

print("Edge between A and B:", graph.get_edge("A", "B"))  
print("Edge between B and E:", graph.get_edge("B", "E"))  