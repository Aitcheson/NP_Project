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
    print("error")

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

def read_graph_from_file(file_path):
    """
    Reads a graph from a file and constructs the adjacency matrix.
    
    Args:
        file_path (str): Path to the input file.

    Returns:
        dict: Adjacency matrix of the graph.
    """
    adj_matrix = {}
    with open(file_path, 'r') as f:
        # num_edges = int(f.readline().strip())  # First line contains the number of edges
        for line in f:
            u, v = map(int, line.strip().split())
            adj_matrix.setdefault(u, []).append(v)
            adj_matrix.setdefault(v, []).append(u)
    return adj_matrix

def main():
    """
    Main function to read a graph from a file, find the vertex cover, and verify it.
    """
    # Read file path from command-line arguments
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        return

    file_path = sys.argv[1]

    # Read adjacency matrix from file
    adj_matrix = read_graph_from_file(file_path)
    print("Adjacency Matrix:", adj_matrix)

    # Measure runtime for the exact solution
    start_time = time.time()
    min_cover = find_min_cover_exact(adj_matrix)
    end_time = time.time()

    # Output results
    print("Minimum Vertex Cover:", min_cover)
    print("Size of Minimum Vertex Cover:", len(min_cover))
    print("Execution Time: {:.2f} seconds".format(end_time - start_time))

    # Verify the result using the NP-verifier
    is_valid = np_verifier(adj_matrix, min_cover)
    print("Is valid vertex cover?", is_valid)

if __name__ == "__main__":
    main()
