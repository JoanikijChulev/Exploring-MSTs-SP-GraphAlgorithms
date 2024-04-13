import networkx as nx
import matplotlib.pyplot as plt
import time



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



num_iterations = 1000000

# Run Prim's algorithm multiple times
total_time_prim = 0
for _ in range(num_iterations):
    start_time_prim = time.time()
    mst_prim = nx.minimum_spanning_tree(G, weight='weight')
    end_time_prim = time.time()
    total_time_prim += end_time_prim - start_time_prim

# Calculate average time for Prim's algorithm
avg_time_prim = total_time_prim / num_iterations

# Run Kruskal's algorithm multiple times
total_time_kruskal = 0
for _ in range(num_iterations):
    start_time_kruskal = time.time()
    mst_kruskal = nx.minimum_spanning_tree(G, algorithm='kruskal', weight='weight')
    end_time_kruskal = time.time()
    total_time_kruskal += end_time_kruskal - start_time_kruskal

# Calculate average time for Kruskal's algorithm
avg_time_kruskal = total_time_kruskal / num_iterations

# Print average execution times
print(f"Average Prim's Algorithm Execution Time (over {num_iterations} iterations): {avg_time_prim} seconds")
print(f"Average Kruskal's Algorithm Execution Time (over {num_iterations} iterations): {avg_time_kruskal} seconds")
