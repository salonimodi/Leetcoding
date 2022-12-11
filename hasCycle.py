
def hasPath(src, des, graph, visited=set()) -> bool:
    if src == des:
        return True
    if src in visited:
        return False

    visited.add(src)

    for val in graph[src]:
        if hasPath(val, des, graph):
            return True
    return False


def adjustancyList(edges):
    graph = {}
    for (a, b) in edges:
        if a not in graph.keys():
            graph[a] = []
        if b not in graph.keys():
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)

    for k in graph:
        print("key " + str(k) + " :" + str(graph[k]))
    return graph


edges = [
    ["i", "j"],
    ["k", "i"],
    ["m", "k"],
    ["k", "l"],
    ["o", "n"]
]
print(hasPath("i", "o", adjustancyList(edges)))
