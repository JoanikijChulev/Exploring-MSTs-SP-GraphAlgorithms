import networkx as nx
import matplotlib.pyplot as plt
import time
import pandas as pd


# Existing and new towns and distances data
all_connections = [
    ('Middelburg', 'Oost-Souburg', 4),
    ('Middelburg', 'Arnemuiden', 4.5),
    ('Oost-Souburg', 'Vlissingen', 3),
    ('Vlissingen', 'Middelburg', 7),
    ('Vlissingen', 'Domburg', 15),
    ('Middelburg', 'Domburg', 13),
    ('Domburg', 'Arnemuiden', 14),
    ('Goes', 'Arnemuiden', 24),
    ('Middelburg', 'Goes', 28),
    ('Goes', 'Kapelle', 6),
    ('Oostburg', 'Kapelle', 40),
    ('Oostburg', 'Goes', 35),
    ('Oostburg', 'Middelburg', 23),
    ('Oostburg', 'Vlissingen', 16),
    ('Oostburg', 'Terneuzen', 30),
    ('Terneuzen', 'Kapelle', 21),
    ('Terneuzen', 'Goes', 22),
    ('Terneuzen', 'Middelburg', 28),
    ('Terneuzen', 'Arnemuiden', 24),
    ('Westkapelle', 'Domburg', 7),
    ('Westkapelle', 'Vlissingen', 16)
]

# Create a weighted graph
G = nx.Graph()

# Add connections as weighted edges
for connection in all_connections:
    G.add_edge(connection[0], connection[1], weight=connection[2])

# Input towns we want to find
start_town = 'Oost-Souburg'
end_town = 'Kapelle'

# Function to perform sensitivity analysis on the impact of edge removal
def edge_removal_sensitivity(graph, algorithm):
    edge_weights = nx.get_edge_attributes(graph, 'weight')
    all_edges = list(edge_weights.keys())
    sensitivity_results = []

    for edge in all_edges:
        temp_graph = graph.copy()
        temp_graph.remove_edge(*edge)

        # Re-run the MST algorithm
        if algorithm == 'prim':
            mst = nx.minimum_spanning_tree(temp_graph, weight='weight', algorithm='prim')
        elif algorithm == 'kruskal':
            mst = nx.minimum_spanning_tree(temp_graph, weight='weight', algorithm='kruskal')

        # Compute the impact on shortest path
        shortest_path_after_removal = nx.shortest_path(temp_graph, source=start_town, target=end_town, weight='weight')
        shortest_distance_after_removal = nx.shortest_path_length(temp_graph, source=start_town, target=end_town, weight='weight')

        # Record the results
        sensitivity_results.append({
            'Removed Edge': edge,
            'MST': mst,
            'Shortest Path': shortest_path_after_removal,
            'Shortest Distance': shortest_distance_after_removal
        })

    return sensitivity_results

# Perform sensitivity analysis for Prim's algorithm
sensitivity_results_prim = edge_removal_sensitivity(G, algorithm='prim')

# Perform sensitivity analysis for Kruskal's algorithm
sensitivity_results_kruskal = edge_removal_sensitivity(G, algorithm='kruskal')

# Display results
for algorithm, results in [('Prim', sensitivity_results_prim), ('Kruskal', sensitivity_results_kruskal)]:
    print(f"\nResults for {algorithm}'s Algorithm Sensitivity Analysis:")
    for i, result in enumerate(results):
        print(f"\nScenario {i + 1}:")
        print("Removed Edge:", result['Removed Edge'])
        print("MST Edges:", result['MST'].edges())
        print("Shortest Path after Removal:", result['Shortest Path'])
        print("Shortest Distance after Removal:", result['Shortest Distance'], "km")
