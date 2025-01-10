#-Find component of a graph which is represented by Adjacency matrix.
#-Behavior
 #              Input: Graph represented by matrix
  #             Output: Number of components both weak and strong 
import networkx as nx
import numpy as np

def create_graph():
    
    G = nx.DiGraph()

    edges = [
        (1, 2), (1, 4),
        (2, 3), (2, 6),
        (6, 3), (6, 4),
        (5, 4), (5, 5), (5, 9),
        (7, 3), (7, 5), (7, 6), (7, 8),
        (8, 3), (8, 9)
    ]
    G.add_edges_from(edges)

    return G

def edges_to_adjacency_matrix(edges, num_nodes):
    
    matrix = np.zeros((num_nodes, num_nodes), dtype=int)
    for u, v in edges:
        matrix[u - 1][v - 1] = 1  
    return matrix

def find_components_matrix(matrix):
    
    
    G = nx.from_numpy_array(np.array(matrix), create_using=nx.DiGraph)

    
    weak_components = nx.number_weakly_connected_components(G)

    
    strong_components = nx.number_strongly_connected_components(G)

    return weak_components, strong_components

if __name__ == "__main__":
    
    G = create_graph()

    
    edges = list(G.edges())
    num_nodes = len(G.nodes())
    adjacency_matrix = edges_to_adjacency_matrix(edges, num_nodes)

    print("Adjacency Matrix G:")
    print(adjacency_matrix)

    # Find components from the adjacency matrix
    weak,strong = find_components_matrix(adjacency_matrix)
    #strong = find_components_matrix(adjacency_matrix)

    print(f"Number of weakly connected components: {weak}")
    print(f"Number of strongly connected components: {strong}")
