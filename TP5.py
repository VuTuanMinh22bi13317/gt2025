import sys
import heapq

def build_adjacency_matrix(vertices, edges):
    size = len(vertices)
    vertex_to_index = {vertex: idx for idx, vertex in enumerate(vertices)}
    matrix = [[float('inf')] * size for _ in range(size)]

    for i in range(size):
        matrix[i][i] = 0  

    for (start, end), weight in edges.items():
        start_idx, end_idx = vertex_to_index[start], vertex_to_index[end]
        matrix[start_idx][end_idx] = weight
        matrix[end_idx][start_idx] = weight  

    return matrix, vertex_to_index

def find_shortest_path(matrix, vertex_map, start, end):
    size = len(matrix)
    distances = [float('inf')] * size
    previous = [None] * size
    start_idx = vertex_map[start]
    end_idx = vertex_map[end]
    distances[start_idx] = 0

    priority_queue = [(0, start_idx)]  

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_vertex == end_idx:
            break

        if current_distance > distances[current_vertex]:
            continue

        for neighbor in range(size):
            edge_weight = matrix[current_vertex][neighbor]
            if edge_weight < float('inf'):
                new_distance = current_distance + edge_weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = current_vertex
                    heapq.heappush(priority_queue, (new_distance, neighbor))

    path = []
    current = end_idx
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()

    index_to_vertex = {idx: vertex for vertex, idx in vertex_map.items()}
    path = [index_to_vertex[idx] for idx in path]

    return path, distances[end_idx]

vertices = ["A", "B", "C", "D", "E", "F", "G", "H", "L", "M"]
edges = {
    ("A", "B"): 4, ("A", "C"): 1, ("B", "F"): 3, ("C", "D"): 8,
    ("C", "F"): 7, ("D", "H"): 1, ("E", "F"): 1, ("E", "H"): 2,
    ("E", "L"): 2, ("F", "H"): 1, ("H", "G"): 3, ("H", "M"): 7,
    ("H", "L"): 6, ("G", "M"): 4, ("G", "L"): 4, ("L", "M"): 1
}

adj_matrix, vertex_map = build_adjacency_matrix(vertices, edges)


print(f"Available vertices: {', '.join(vertices)}")

source_vertex = input("Enter the source vertex: ").strip().upper()
target_vertex = input("Enter the target vertex: ").strip().upper()

if source_vertex not in vertex_map or target_vertex not in vertex_map:
    print("Invalid source or target vertex. Please check your input.")
    sys.exit(1)

shortest_path, total_cost = find_shortest_path(adj_matrix, vertex_map, source_vertex, target_vertex)

if total_cost == float('inf'):
    print(f"No path exists between {source_vertex} and {target_vertex}.")
else:
    print(f"Shortest path from {source_vertex} to {target_vertex}: {' -> '.join(shortest_path)}")
    print(f"Total path weight: {total_cost}")
