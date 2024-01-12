import networkx as nx

from cities import swiss_cities_with_weight


def dijkstra(graph, start):
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.nodes)

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float("infinity"):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight["weight"]

            if distance < distances[neighbor]:
                distances[neighbor] = distance

        unvisited.remove(current_vertex)

    return distances


swiss_cities_graph = nx.Graph()
swiss_cities_graph.add_edges_from(swiss_cities_with_weight)

for start in swiss_cities_graph.nodes:
    paths = dijkstra(swiss_cities_graph, start)
    print(f"Найкоротший шлях в розробленому графі від`{start}` до інших станцій: {paths}")