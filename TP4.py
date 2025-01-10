import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    # Function to add an edge to the graph (for Kruskal's algorithm)
    def addEdge(self, u, v, w):
        # For Kruskal's algorithm, we store edges in a list
        self.graph[u][v] = w
        self.graph[v][u] = w  # Because it's an undirected graph

    # A utility function to find set of an element i (for Kruskal's algorithm)
    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    # A function that does union of two sets (for Kruskal's algorithm)
    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

    # Prim's Minimum Spanning Tree (MST) algorithm
    def primMST(self, root):
        key = [sys.maxsize] * self.V
        parent = [-1] * self.V  # Fix: Start with -1 to indicate no parent yet
        mstSet = [False] * self.V
        
        key[root] = 0  # Start with root node
        
        for cout in range(self.V):
            # Select the vertex with the minimum key value that is not yet included in MST
            u = self.minKey(key, mstSet)
            mstSet[u] = True

            for v in range(self.V):
                # Update key[v] if a smaller weight edge is found and vertex v is not yet included in MST
                if self.graph[u][v] > 0 and not mstSet[v] and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.printMST(parent)

    # Utility function for Prim's algorithm to find the vertex with the minimum key
    def minKey(self, key, mstSet):
        min = sys.maxsize
        min_index = -1
        for v in range(self.V):
            if key[v] < min and not mstSet[v]:
                min = key[v]
                min_index = v
        return min_index

    # Print the MST and calculate the total weight for Prim's algorithm
    def printMST(self, parent):
        print("\nPrim's Algorithm MST:")
        total_weight = 0
        for i in range(self.V):  # Loop through all vertices
            if parent[i] != -1:  # Check if parent is valid
                print(f"{parent[i]} - {i} \t {self.graph[i][parent[i]]}")
                total_weight += self.graph[i][parent[i]]
        print("Total Weight of MST (Prim's):", total_weight)

    # Kruskal's Minimum Spanning Tree (MST) algorithm
    def KruskalMST(self):
        result = []
        i = 0  # Index for sorted edges
        e = 0  # Number of edges in MST
        edges = []

        # Collect edges from the adjacency matrix
        for u in range(self.V):
            for v in range(u + 1, self.V):
                if self.graph[u][v] > 0:
                    edges.append([u, v, self.graph[u][v]])

        # Sort edges by weight
        edges = sorted(edges, key=lambda item: item[2])
        
        parent = [node for node in range(self.V)]
        rank = [0] * self.V

        # Run Kruskal's algorithm to find the MST
        while e < self.V - 1:
            u, v, w = edges[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        # Print the results
        minimumCost = 0
        print("\nKruskal's Algorithm MST:")
        for u, v, weight in result:
            minimumCost += weight
            print(f"{u} -- {v} == {weight}")
        print("Total Weight of MST (Kruskal's):", minimumCost)

# Driver code
if __name__ == '__main__':
    vertices = 9  # Number of vertices (adjust based on your graph)
    g = Graph(vertices)
    
    # Input edges for the graph (adjust to zero-based indexing)
    g.addEdge(0, 1, 4)
    g.addEdge(0, 4, 1)
    g.addEdge(0, 6, 2)
    g.addEdge(1, 2, 7)
    g.addEdge(1, 5, 5)
    g.addEdge(2, 3, 1)
    g.addEdge(2, 5, 8)
    g.addEdge(3, 6, 4)
    g.addEdge(4, 5, 9)
    g.addEdge(4, 6, 10)
    g.addEdge(5, 8, 2)
    g.addEdge(6, 7, 2)
    g.addEdge(7, 3, 4)
    g.addEdge(7, 8, 8)
    
    # Ask the user for the root node for Prim's algorithm (0-based index)
    root_node = int(input("Enter the root node (0-8): "))

    # Run both algorithms
    g.primMST(root_node)
    g.KruskalMST()
