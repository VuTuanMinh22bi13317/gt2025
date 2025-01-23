edges = [
    (1, 2),
    (1, 3),
    (2, 5),
    (2, 6),
    (5, 7),
    (3, 4),
    (4, 8)
]

def create_adjacency_matrix(edges, num_nodes):
    
    matrix = [[0] * num_nodes for _ in range(num_nodes)]
    
 
    for src, dest in edges:
        matrix[src - 1][dest - 1] = 1  
    
    return matrix

def print_adjacency_matrix(matrix):
    print("Adjacency Matrix:")
    for row in matrix:
        print(" ".join(map(str, row)))

def inorder_traversal(graph, node, visited=None):
    if visited is None:
        visited = set()

    visited.add(node)

    for child in graph.get(node, []):
        if child not in visited:
            inorder_traversal(graph, child, visited)

    print(node, end=" ")

num_nodes = 8  
adj_matrix = create_adjacency_matrix(edges, num_nodes)

print_adjacency_matrix(adj_matrix)

adj_list = {i + 1: [] for i in range(num_nodes)}
for i in range(num_nodes):
    for j in range(num_nodes):
        if adj_matrix[i][j] == 1:
            adj_list[i + 1].append(j + 1)

try:
    start_node = int(input("\nEnter the starting node label (1-8): "))
    if start_node < 1 or start_node > num_nodes:
        raise ValueError("Node label out of range.")
except ValueError as e:
    print(f"Invalid input: {e}")
else:
    print(f"\nInorder traversal of subtree rooted at {start_node}:")
    inorder_traversal(adj_list, start_node)
