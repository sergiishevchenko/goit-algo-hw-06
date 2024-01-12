import networkx as nx
import matplotlib.pyplot as plt

from cities import swiss_cities

swiss_cities_graph = nx.Graph()

swiss_cities_graph.add_edges_from(swiss_cities)

pos = nx.spring_layout(swiss_cities_graph)

nx.draw(
    swiss_cities_graph,
    pos,
    with_labels=True,
    font_size=10,
    node_size=1000,
    node_color="red",
    font_color="blue",
    font_weight="bold",
    arrowsize=5,
)

plt.title("Swiss cities")
plt.show()

nodes = swiss_cities_graph.number_of_nodes()
edges = swiss_cities_graph.number_of_edges()

print(f"Кількість вершин: {nodes}")
print(f"Кількість ребер: {edges}")
degree_dict = dict(swiss_cities_graph.degree())
print("\nСтупінь кожної вершини:")

for node, degree in degree_dict.items():
    print(f"{node}: {degree}")