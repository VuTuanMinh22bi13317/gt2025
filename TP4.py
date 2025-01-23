import heapq
from collections import defaultdict


vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
edges = {
    (1, 2): 4, (1, 5): 1, (1, 7): 2,
    (2, 3): 7, (2, 6): 5,
    (3, 4): 1, (3, 6): 8,
    (4, 6): 6, (4, 7): 4, (4, 8): 3,
    (5, 6): 9, (5, 7): 10,
    (6, 9): 2,
    (7, 7): 2, (7, 9): 8,
    (8, 9): 1
}


adjacency_list = defaultdict(list)
for (u, v), weight in edges.items():
    adjacency_list[u].append((v, weight))
    adjacency_list[v].append((u, weight))  


def prim(start_node):
    mst_edges = []
    visited = set()
    min_heap = [(0, start_node, -1)]  
    total_weight = 0

    while min_heap:
        weight, current_node, previous_node = heapq.heappop(min_heap)
        if current_node in visited:
            continue

        visited.add(current_node)
        if previous_node != -1:
            mst_edges.append((previous_node, current_node, weight))
            total_weight += weight

        for neighbor, edge_weight in adjacency_list[current_node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, current_node))

    return mst_edges, total_weight


def kruskal():
    mst_edges = []
    total_weight = 0
    parent = {v: v for v in vertices}
    rank = {v: 0 for v in vertices}

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])  
        return parent[node]

    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)

        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1

    sorted_edges = sorted(edges.items(), key=lambda x: x[1])

    for (u, v), weight in sorted_edges:
        if find(u) != find(v):
            union(u, v)
            mst_edges.append((u, v, weight))
            total_weight += weight

    return mst_edges, total_weight

if __name__ == "__main__":
   
    try:
        root = int(input(f"Enter root node for Prim's algorithm (choose from {vertices}): "))
        if root not in vertices:
            raise ValueError("Root node must be in the list of vertices.")
    except ValueError as e:
        print(f"Invalid input: {e}")
    else:
        print("\nPrim's Algorithm:")
        prim_mst, prim_weight = prim(root)
        print("Edges in MST:", prim_mst)
        print("Total weight of MST:", prim_weight)

   
    print("\nKruskal's Algorithm:")
    kruskal_mst, kruskal_weight = kruskal()
    print("Edges in MST:", kruskal_mst)
    print("Total weight of MST:", kruskal_weight)
