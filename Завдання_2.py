import networkx as nx

from cities import swiss_cities


def dfs(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for neighbor in graph.neighbors(start):
        if neighbor not in path:
            new_paths = dfs(graph, neighbor, end, path)
            for p in new_paths:
                paths.append(p)
    return paths


def bfs(graph, start, end):
    queue = [(start, [start])]
    paths = []
    while queue:
        current, path = queue.pop(0)
        for neighbor in graph.neighbors(current):
            if neighbor not in path:
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))
                if neighbor == end:
                    paths.append(new_path)
    return paths


def main():
    swiss_cities_graph = nx.Graph()
    swiss_cities_graph.add_edges_from(swiss_cities)

    dfs_alg = dfs(swiss_cities_graph, "Geneve", "St.Gallen")
    print(dfs_alg, len(dfs_alg))
    bfs_alg = bfs(swiss_cities_graph, "Geneve", "St.Gallen")
    print(bfs_alg, len(bfs_alg))


if __name__ == "__main__":
    main()