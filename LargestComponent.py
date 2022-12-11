
def visitGraph(k, adjusancyGraph, visited) -> int:
    size = 0
    if k not in visited:
        size = 1
        for neightbour in adjusancyGraph[k]:
            visited.add(k)
            size += visitGraph(neightbour, adjusancyGraph, visited)
    return size


def largestComponent(adjusancyGraph) -> int:
    visited = set()
    longestComp = 0
    for node in adjusancyGraph:
        size = visitGraph(node, adjusancyGraph, visited)
        if size > longestComp:
            longestComp = size
    return longestComp


def adjustancyList(edges) -> set:
    graph = {}
    for a, b in edges:
        if a not in graph:
            graph[a] = []
        if b not in graph:
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


print(largestComponent(adjustancyList(edges)))


