from itertools import combinations
import time

def find_min_cover_exact(adj_matrix):
    """
    Finds the exact minimum vertex cover using brute force.
    """
    
    vertices = list(adj_matrix.keys())
    n = len(vertices)

    # Start with the smallest possible cover size and incrementally increase
    for size in range(1, n + 1):
        for subset in combinations(vertices, size):
            subset_set = set(subset)
            if np_verifier(adj_matrix, subset_set):
                return subset_set
    # print("error")

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
    #  # Example input without user input
    # edges = [(1, 2), (2, 3), (3, 5), (3, 4)]
    # nonoptimal_edges = [(1, 2), (1, 3), (1, 4), (2, 5), (3, 6), (4, 7)]
    
    num_edges = int(input())
    edges = []

    for _ in range(num_edges):
        u, v = map(int, input().split())
        edges.append((u, v))

    # Construct adjacency matrix (using a dictionary of lists for simplicity)
    adj_matrix = {}
    for u, v in edges:
        adj_matrix.setdefault(u, []).append(v)
        adj_matrix.setdefault(v, []).append(u)

    # print("Adjacency Matrix:", adj_matrix)

    # Find the minimum vertex cover
    min_cover = find_min_cover_exact(adj_matrix)
    # print("Minimum Vertex Cover:", min_cover)
    print(min_cover)

    # Verify the result using the NP-verifier
    is_valid = np_verifier(adj_matrix, min_cover)
    # print("Is valid vertex cover?", is_valid)

if __name__ == "__main__":
    main()
