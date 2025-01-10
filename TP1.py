import networkx as nx
def creategraph():
    G = nx.Graph()

    edges1 = [(1,2),(2,5)]
    G.add_edges_from(edges1)

    edges2 = [(3,6),(6,4),(6,7),(4,7)]
    G.add_edges_from(edges2)

    return G

def path_exists(graph, node1, node2):
    try:
          return nx.has_path(graph, node1, node2)
    except nx.NetworkXError:
        # Handle the case where nodes are not in the graph
        return False

if __name__ == "__main__":
    # Create the graph
    G = creategraph()

    # Take user input for nodes to check
    try:
        node1 = int(input("Enter the first node: "))
        node2 = int(input("Enter the second node: "))

        # Check if a path exists and print the result
        if path_exists(G, node1, node2):
            print(f"A path exists between node {node1} and node {node2}.")
        else:
            print(f"No path exists between node {node1} and node {node2}.")
    except ValueError:
        print("Invalid input. Please enter integer node values.")

# import networkx as nx

# def create_graph():
#     """
#     Creates the graph based on the described structure as a directed graph.
#     Returns:
#         G (networkx.DiGraph): The directed graph object.
#     """
#     G = nx.DiGraph()

#     # Add edges based on the input structure
#     edges = [
#         (1, 2), (1, 4),
#         (2, 3), (2, 6),
#         (6, 3), (6, 4),
#         (5, 4), (5, 5), (5, 9),
#         (7, 3), (7, 5), (7, 6), (7, 8),
#         (8, 3), (8, 9)
#     ]
#     G.add_edges_from(edges)

#     return G

# def path_exists(graph, node1, node2):
#     """
#     Checks if a path exists between two nodes in the directed graph.

#     Args:
#         graph (networkx.DiGraph): The directed graph object.
#         node1 (int): The starting node.
#         node2 (int): The target node.

#     Returns:
#         bool: True if a path exists, False otherwise.
#     """
#     try:
#         # Use NetworkX's built-in method to check for a path
#         return nx.has_path(graph, node1, node2)
#     except nx.NetworkXError:
#         # Handle the case where nodes are not in the graph
#         return False

# def find_all_paths(graph, source, target, path=None):
#     """
#     Finds all possible paths between two nodes in a directed graph.

#     Args:
#         graph (networkx.DiGraph): The directed graph object.
#         source (int): The starting node.
#         target (int): The target node.
#         path (list): The current path being explored (used for recursion).

#     Returns:
#         list: A list of all paths, where each path is represented as a list of nodes.
#     """
#     if path is None:
#         path = []

#     path = path + [source]

#     if source == target:
#         return [path]

#     if source not in graph:
#         return []

#     paths = []
#     for neighbor in graph.neighbors(source):
#         if neighbor not in path:  # Avoid cycles
#             new_paths = find_all_paths(graph, neighbor, target, path)
#             for p in new_paths:
#                 paths.append(p)

#     return paths

# def path_sequence(graph, source, target):
#     """
#     Returns all possible paths from source to target.

#     Args:
#         graph (networkx.DiGraph): The directed graph object.
#         source (int): The starting node.
#         target (int): The target node.

#     Returns:
#         list: A list of all paths, where each path is represented as a list of nodes.
#     """
#     paths = find_all_paths(graph, source, target)
#     if paths:
#         print(f"All paths from {source} to {target}:")
#         for path in paths:
#             print(path)
#     else:
#         print(f"No path exists from {source} to {target}.")
#     return paths

# if __name__ == "__main__":
#     # Create the graph
#     G = create_graph()

#     # Take user input for nodes to check
#     try:
#         source = int(input("Enter the source node: "))
#         target = int(input("Enter the target node: "))

#         # Get all possible paths
#         path_sequence(G, source, target)
#     except ValueError:
#         print("Invalid input. Please enter integer node values.")
