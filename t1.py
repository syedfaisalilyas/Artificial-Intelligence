class AdjNode:
    def __init__(self, value):
        self.vertex = value
        self.next = None


class Graph:
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V

    
    def add_edge(self, s, d):
        
        node = AdjNode(d)
        node.next = self.graph[s]
        self.graph[s] = node

        
        node = AdjNode(s)
        node.next = self.graph[d]
        self.graph[d] = node

    
    def print_agraph(self):
        for i in range(self.V):
            print("Vertex " + str(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")

    
    def get_connected_nodes(self, node):
        connected_nodes = []
        temp = self.graph[node]
        while temp:
            connected_nodes.append(temp.vertex)
            temp = temp.next
        return connected_nodes

    
    def get_edge(self, node1, node2):
        temp = self.graph[node1]
        while temp:
            if temp.vertex == node2:
                return (node1, node2)  
            temp = temp.next
        return None  

    
    def are_connected(self, node1, node2):
        return self.get_edge(node1, node2) is not None

    
    def is_valid_path(self, path):
        for i in range(len(path) - 1):
            if not self.are_connected(path[i], path[i + 1]):
                return False
        return True

    
    def delete_edge(self, s, d):
        
        self._remove_edge(s, d)
        
        self._remove_edge(d, s)

    def _remove_edge(self, src, dest):
        temp = self.graph[src]
        prev = None
        while temp:
            if temp.vertex == dest:
                if prev:
                    prev.next = temp.next
                else:
                    self.graph[src] = temp.next
                return
            prev = temp
            temp = temp.next


if __name__ == "__main__":
    V = 5
    graph =     Graph(V)

    
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)

    graph.print_agraph()

    
    print(f"Connected nodes to vertex 0: {graph.get_connected_nodes(0)}")

    
    print(f"Edge between 0 and 1: {graph.get_edge(0, 1)}")
    print(f"Edge between 1 and 3: {graph.get_edge(1, 3)}")

    
    print(f"Are 0 and 1 connected? {graph.are_connected(0, 1)}")
    print(f"Are 1 and 3 connected? {graph.are_connected(1, 3)}")

    
    path1 = [0, 1, 2]
    path2 = [0, 1, 3]
    print(f"Is path {path1} valid? {graph.is_valid_path(path1)}")
    print(f"Is path {path2} valid? {graph.is_valid_path(path2)}")

    
    graph.delete_edge(0, 1)
    graph.print_agraph()


