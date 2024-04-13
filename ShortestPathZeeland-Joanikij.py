import networkx as nx
import matplotlib.pyplot as plt

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
start_town = 'Terneuzen'
end_town = 'Westkapelle'

# Find the shortest path between the input towns
shortest_path = nx.shortest_path(G, source=start_town, target=end_town, weight='weight')
shortest_distance = nx.shortest_path_length(G, source=start_town, target=end_town, weight='weight')

# Plot the graph with the shortest path highlighted
pos = nx.spring_layout(G)  # Layout for better visualization
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, font_size=8, edge_color='gray')

# Highlight the shortest path
path_edges = [(shortest_path[i], shortest_path[i + 1]) for i in range(len(shortest_path) - 1)]
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

# Highlight start node with green and end node with red
node_colors = ['green' if node == start_town else 'red' if node == end_town else 'skyblue' for node in G.nodes()]
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=700)

# Add edge labels (distances)
edge_labels = {(edge[0], edge[1]): edge[2] for edge in G.edges(data='weight')}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Display the graph
plt.title(f'Shortest Path from {start_town} to {end_town}')
plt.show()

# Print the shortest path and distance
print(f"Shortest Path from {start_town} to {end_town}:", shortest_path)
print(f"Shortest Distance from {start_town} to {end_town}:", shortest_distance, "km")
