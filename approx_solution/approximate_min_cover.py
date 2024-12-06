import random
import time

def remove_highest_degree(adj_matrix):
    """Removes the vertex with the highest degree and its associated edges from the adjacency matrix.
    Breaks ties randomly if multiple vertices have the same degree.

    Args:
        adj_matrix ({[]}): adjacency matrix containing the graph

    Returns:
        (vertex, adj_matrix): vertex with the highest degree, 
                              adjacency matrix with the highest degree vertex removed
    """
    # Calculate degrees of vertices
    degrees = {v: len(neighbors) for v, neighbors in adj_matrix.items()}
    max_degree = max(degrees.values())
    
    # Find vertices with the maximum degree
    candidates = [v for v, d in degrees.items() if d == max_degree]
    
    # Randomly select one vertex from the list of highest degrees
    selected_vertex = random.choice(candidates)
    
    # Remove the selected vertex and all of its edges
    new_adj_matrix = {v: [neighbor for neighbor in neighbors if neighbor != selected_vertex]
                      for v, neighbors in adj_matrix.items() if v != selected_vertex}
    
    # print("SELECTED: ", selected_vertex)
    # print("NEW MATRIX: ", new_adj_matrix)
    
    return selected_vertex, new_adj_matrix

def check_edges(adj_matrix):
    """Checks if there are any edges left in the adjacency matrix.
    Returns True if no edges remain, False otherwise.

    Args:
        adj_matrix ({[]}): adjacency matrix containing the graph

    Returns:
        boolean: True if no edges are present, False if an edge is found
    """
    for neighbors in adj_matrix.values():
        if neighbors:
            # Vertex still has uncovered edges
            return False
    return True

def find_min_cover(adj_matrix):
    """Recursive function to find the minimum vertex cover using the greedy approach.
    Finds the minimum amount of vertices required to touch every edge.

    Args:
        adj_matrix ({[]}): adjacency matrix containing the graph

    Returns:
        [vertices]: contains the list of vertices in the minimum vertex cover
    """
    result = set()

    # Get the vertex with the highest degree and updated graph
    removed_vertex, updated_matrix = remove_highest_degree(adj_matrix)

    # Add the removed vertex to the result
    result.add(removed_vertex)

    # Check if there are any edges left
    if check_edges(updated_matrix):
        return result
    else:
        # Recursive call with the updated matrix
        result.update(find_min_cover(updated_matrix))
        return result

def np_verifier(adj_matrix, cover):
    """Verifies if the provided set is a valid vertex cover.

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
    start_time = time.time()  # Record start time
    min_cover = find_min_cover(adj_matrix)
    end_time = time.time()    # Record end time
    
    print("Time taken: {:.4f} seconds".format(end_time - start_time))
    
    # print("Minimum Vertex Cover:", min_cover)
    print(min_cover)

    # Verify the result using the NP-verifier
    # is_valid = np_verifier(adj_matrix, min_cover)
    # print("Is valid vertex cover?", is_valid)

if __name__ == "__main__":
    main()
