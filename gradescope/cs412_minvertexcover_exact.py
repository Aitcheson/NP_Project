from itertools import combinations

def find_min_cover_exact(adj_matrix):
    """
    Finds the exact minimum vertex cover using brute force.
    """
    vertices = list(adj_matrix.keys())
    n = len(vertices)

    for size in range(1, n + 1):
        for subset in combinations(vertices, size):
            subset_set = set(subset)
            if np_verifier(adj_matrix, subset_set):
                return subset_set
    return set()

def np_verifier(adj_matrix, cover):
    """
    Verifies if the provided set is a valid vertex cover.

    Args:
        adj_matrix ({[]}): adjacency matrix containing the graph
        cover ([]): list of vertices containing a possible minimum vertex cover solution

    Returns:
        boolean: True if the solution is valid, False otherwise
    """
    for v, neighbors in adj_matrix.items():
        for neighbor in neighbors:
            if v not in cover and neighbor not in cover:
                return False
    return True

def main():
    """
    Main function to take input, construct adjacency matrix, find the vertex cover, and verify it.
    """
    num_edges = int(input())
    edges = []

    for _ in range(num_edges):
        u, v = map(int, input().split())
        edges.append((u, v))

    adj_matrix = {}
    for u, v in edges:
        adj_matrix.setdefault(u, []).append(v)
        adj_matrix.setdefault(v, []).append(u)

    min_cover = find_min_cover_exact(adj_matrix)

    # Verify the result using the NP-verifier 
    if min_cover:
        print(" ".join(map(str, sorted(min_cover))))
    else:
        print("No valid vertex cover found.")

if __name__ == "__main__":
    main()
