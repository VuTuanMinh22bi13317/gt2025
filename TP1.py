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