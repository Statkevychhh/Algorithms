import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


# Матриця суміжності з вагами ребер
adj_matrix = np.array([
    [0, 5, 3, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0],
    [5, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0],
    [3, 0, 0, 0, 0, 3, 0, 3, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [3, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0],
    [0, 2, 3, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 2, 0, 1, 2, 0, 0, 0, 0, 2, 0, 2, 0],
    [0, 0, 3, 1, 1, 0, 0, 0, 0, 0, 2, 2, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 4],
    [0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 4],
    [0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 4],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 4, 4, 4, 0]
])

# Створення графа з матриці суміжності з вагами
G = nx.from_numpy_array(adj_matrix)

# Визначення Мінімального Остова графа
spanning_tree = nx.minimum_spanning_tree(G)

# Вивід графа та остова графа з вагами
plt.figure(figsize=(12, 6))

plt.subplot(121)
pos = nx.spring_layout(G)  # позиції вузлів для виводу графа
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=800, node_color='lightblue', edge_color='black')
edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Граф з вагами")

plt.subplot(122)
nx.draw(spanning_tree, pos, with_labels=True, font_weight='bold', node_size=800, node_color='lightgreen', edge_color='black')
edge_labels_tree = {(u, v): d['weight'] for u, v, d in spanning_tree.edges(data=True)}
nx.draw_networkx_edge_labels(spanning_tree, pos, edge_labels=edge_labels_tree)
plt.title("Мінімальний Остов графа")

plt.tight_layout()
plt.show()
